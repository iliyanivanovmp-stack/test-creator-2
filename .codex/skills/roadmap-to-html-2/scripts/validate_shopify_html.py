#!/usr/bin/env python3
"""Preflight a roadmap fragment. This is not a Shopify save/sanitizer test."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

# Internal paste-size budget, not a claim about Shopify's universal API limit.
MAX_BYTES = 64_000

class Fragment(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.ids = set()
        self.references = []
        self.svg_depth = 0
        self.desktop = self.mobile = self.slots = 0
        self.root = False

    def handle_decl(self, decl):
        self.errors.append('Document declarations are not allowed.')

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'svg':
            self.svg_depth += 1
        if tag in {'html', 'head', 'body', 'meta', 'script', 'iframe', 'object', 'embed'}:
            self.errors.append(f'Unsupported fragment tag: {tag}.')
        if tag == 'title' and not self.svg_depth:
            self.errors.append('Document titles are not allowed; SVG titles are fine.')
        ident = a.get('id')
        if ident:
            if ident in self.ids:
                self.errors.append(f'Duplicate id: {ident}.')
            self.ids.add(ident)
        if tag == 'div' and ident == 'cvrt-roadmap':
            self.root = True
        classes = a.get('class', '').split()
        if any(not c.startswith('cvrt-') for c in classes):
            self.errors.append('All classes must use the cvrt- prefix.')
        self.slots += 'cvrt-slot' in classes
        if tag == 'svg':
            self.desktop += 'cvrt-desktop' in classes
            self.mobile += 'cvrt-mobile' in classes
        for name, value in attrs:
            if name.startswith('on'):
                self.errors.append(f'Inline event handler: {name}.')
            if name not in {'href', 'xlink:href', 'src'} or not value:
                continue
            if value.startswith('#'):
                if tag == 'use':
                    self.references.append(value[1:])
            elif not value.startswith('https://'):
                self.errors.append(f'{tag} {name} must be an HTTPS URL or fragment reference.')

    def handle_endtag(self, tag):
        if tag == 'svg':
            self.svg_depth -= 1


def validate(path):
    raw = Path(path).read_bytes()
    errors = []
    if len(raw) > MAX_BYTES:
        errors.append(f'{len(raw):,} bytes exceeds the {MAX_BYTES:,}-byte internal paste budget.')
    try:
        source = raw.decode('ascii')
    except UnicodeDecodeError:
        errors.append('HTML must be ASCII-only; encode other characters as numeric references.')
        source = raw.decode('utf-8')
    if re.search(r'(?:data|blob|file):|;base64,', source, re.I):
        errors.append('Embedded data, blob, and local-file URLs are forbidden in page exports.')
    if not source.lstrip().startswith('<link'):
        errors.append('Expected font links at the start of the fragment.')
    parsed = Fragment()
    parsed.feed(source)
    errors += parsed.errors
    if not parsed.root:
        errors.append('Missing div#cvrt-roadmap.')
    if not parsed.slots or parsed.desktop != parsed.slots or parsed.mobile != parsed.slots:
        errors.append('Each slot needs one desktop SVG and one mobile SVG.')
    for ref in parsed.references:
        if ref not in parsed.ids:
            errors.append(f'Unresolved SVG reference: {ref}.')
    return len(raw), errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', type=Path)
    args = parser.parse_args()
    size, errors = validate(args.html)
    print(f'{args.html}: {size:,} bytes / {MAX_BYTES:,}-byte internal budget')
    for error in dict.fromkeys(errors):
        print('FAIL:', error)
    if not errors:
        print('PASS: compact fragment, public assets, scoped classes, and complete SVG references.')
        print('Shopify save and post-save rendering still require verification in the target store.')
    raise SystemExit(bool(errors))
