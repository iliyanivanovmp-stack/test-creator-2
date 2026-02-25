---
description: Pull latest changes from main and rebase if needed
---

Pull the latest changes from main and get the local branch up to date.

1. Run `git fetch origin main` to check for new changes on the remote.
2. Run `git status` to see if there are any local uncommitted changes. If there are, warn the user and stop — they should run `/finish-work` first.
3. Compare the local main with origin/main using `git rev-list --left-right --count main...origin/main`.
   - If local is already up to date, tell the user: "You're all set — you already have the latest changes."
   - If the remote is ahead (there are new changes to pull), run `git pull --rebase origin main`.
   - If local is ahead (unpushed commits), tell the user: "You have unpushed commits on main. Run `/finish-work` or `git push` to push them before starting new work."
4. If a rebase was needed, explain to the user in simple, non-technical language:

   > Someone on the team pushed new changes while you were working. I pulled those in and replayed your work on top of them — think of it like inserting new pages into a shared notebook before your pages, so everything stays in order. Nothing was lost or overwritten.

5. If the rebase encounters a conflict, stop and explain:

   > There's a conflict — two people edited the same part of a file. I'll need your help deciding which version to keep. Let me show you what's conflicting.

   Then show the conflicting files and ask the user how they want to resolve each one.

6. Confirm when done: "You're up to date and ready to work."
