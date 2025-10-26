---
name: git-safety-skill
description: Master Git safety procedures and workflows. Use for: commit best practices, branch strategies, backup procedures, collaboration workflows, hook management, revert strategies, conflict resolution, and production-safe Git operations that prevent data loss and enable team collaboration.
---

# 🔐 Git Safety Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert
**Based on:** CLAUDE.md Git Safety Protocol

---

## 📋 Table of Contents

1. [Git Safety Protocol](#git-safety-protocol)
2. [Commit Best Practices](#commit-best-practices)
3. [Branch Strategies](#branch-strategies)
4. [Backup Procedures](#backup-procedures)
5. [Collaboration Workflows](#collaboration-workflows)
6. [Hook Management](#hook-management)
7. [Revert & Recovery](#revert-recovery)
8. [Conflict Resolution](#conflict-resolution)
9. [Production Safety](#production-safety)
10. [Git Commands Reference](#git-commands-reference)

---

## 🛡️ Git Safety Protocol

### Core Safety Rules (from CLAUDE.md)

**NEVER:**
- ❌ Update git config without permission
- ❌ Run destructive/irreversible commands (force push, hard reset)
- ❌ Skip hooks (--no-verify, --no-gpg-sign)
- ❌ Force push to main/master
- ❌ Use git commit --amend without checking authorship
- ❌ Commit changes unless explicitly asked

**ALWAYS:**
- ✅ Check authorship before amending: `git log -1 --format='%an %ae'`
- ✅ Verify not pushed before amending: `git status`
- ✅ Create backup branches before risky operations
- ✅ Ask user before committing
- ✅ Use meaningful commit messages
- ✅ Review changes before committing

---

### When to Commit

**❌ DON'T commit automatically:**
```bash
# Even if code is done, ASK FIRST
# User needs to control when commits happen
```

**✅ DO commit when:**
- User explicitly requests: "commit these changes"
- User says: "save this" or "create a commit"
- After completing requested changes AND user approves

---

## 📝 Commit Best Practices

### The Perfect Commit

**What Makes a Good Commit:**
1. **Atomic** - One logical change
2. **Complete** - Fully functional (tests pass)
3. **Documented** - Clear message explaining why
4. **Reviewed** - Changes verified before commit

---

### Commit Message Format (from CLAUDE.md)

```bash
git commit -m "$(cat <<'EOF'
[Summary of changes - focus on WHY, not WHAT]

[Optional: Additional context if needed]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Key Points:**
- Focus on WHY, not WHAT (code shows what changed)
- Concise summary (1-2 sentences)
- Use present tense ("Add feature" not "Added feature")
- Include attribution footer

---

### Commit Process (from CLAUDE.md)

**Step 1: Run git commands in parallel**
```bash
# Get status, diff, and recent commits simultaneously
git status &
git diff --staged &
git diff &
git log --oneline -10 &
wait
```

**Step 2: Analyze Changes**
```bash
# Review:
# - What changed? (git diff)
# - What's staged? (git status)
# - Commit style? (git log)
```

**Step 3: Draft Commit Message**
```bash
# Summarize nature of changes:
# - New feature? Enhancement? Bug fix? Refactor? Docs?
# - Ensure accuracy (add = new, update = enhancement, fix = bug)
# - Keep concise (1-2 sentences)
# - Focus on WHY
```

**Step 4: Add & Commit**
```bash
# Add relevant files
git add <files>

# Commit with message
git commit -m "$(cat <<'EOF'
Add systematic debugging methodology skill

Implements Codex debugging approach from CLAUDE.md:
- Step 0: Understand domain before assuming bug
- Trace execution, calculate expected values
- Validate assumptions, find root causes
- Includes case studies and practical examples

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

# Verify
git status
```

---

### Pre-Commit Hook Handling

**If commit fails due to pre-commit hook:**

```bash
# Hook modified files (e.g., auto-formatting)

# BEFORE amending, check:
# 1. Authorship
git log -1 --format='%an %ae'
# Must be YOUR commit, not someone else's

# 2. Not pushed yet
git status
# Should show "Your branch is ahead of 'origin/main' by 1 commit"

# If both true → safe to amend
git add <modified-files>
git commit --amend --no-edit

# If either false → create NEW commit
git add <modified-files>
git commit -m "Apply pre-commit hook changes"
```

**Key Rule:** NEVER amend other developers' commits!

---

## 🌳 Branch Strategies

### Branch Naming Conventions

**Format:**
```
<type>/<short-description>

Types:
- feature/  (new functionality)
- fix/      (bug fixes)
- refactor/ (code improvements)
- docs/     (documentation)
- test/     (testing)
- chore/    (maintenance)

Examples:
✅ feature/user-authentication
✅ fix/login-validation-bug
✅ refactor/database-queries
✅ docs/api-documentation
```

---

### Creating Safe Branches

**Before risky operations (from CLAUDE.md):**

```bash
# Create backup branch
git checkout -b feature-backup
git push origin feature-backup

# Now safe to experiment on original branch
git checkout feature-main

# If something goes wrong:
git reset --hard origin/feature-backup
```

---

### Branch Workflow

**Feature Branch Flow:**
```bash
# 1. Create branch from main
git checkout main
git pull origin main
git checkout -b feature/new-feature

# 2. Make changes and commit
git add .
git commit -m "Add new feature"

# 3. Push to remote
git push -u origin feature/new-feature

# 4. Create pull request (via GitHub/GitLab)

# 5. After merge, cleanup
git checkout main
git pull origin main
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

## 💾 Backup Procedures

### Before Risky Operations

**Always create backup:**
```bash
# Method 1: Backup branch
git checkout -b backup-$(date +%Y%m%d-%H%M%S)
git push origin backup-$(date +%Y%m%d-%H%M%S)

# Method 2: Tag
git tag backup-before-rebase
git push origin backup-before-rebase

# Method 3: Stash
git stash save "Backup before risky operation"
```

---

### Recovery from Backup

**Restore from branch:**
```bash
# If on wrong branch
git checkout backup-branch-name

# Or reset current branch
git reset --hard backup-branch-name
```

**Restore from tag:**
```bash
git reset --hard backup-before-rebase
```

**Restore from stash:**
```bash
git stash list
git stash apply stash@{0}
```

---

## 👥 Collaboration Workflows

### Pull Request Process

**Creating PR (from CLAUDE.md):**

**Step 1: Understand branch state**
```bash
# Run in parallel
git status &
git diff --staged &
git diff &
git log origin/main...HEAD &
wait
```

**Step 2: Analyze all changes**
```bash
# Review ALL commits in PR (not just latest!)
git log origin/main...HEAD --oneline

# Check full diff from base branch
git diff origin/main...HEAD
```

**Step 3: Draft PR summary**
```markdown
## Summary
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

## Test plan
- [ ] Test case 1
- [ ] Test case 2
- [ ] Test case 3

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

**Step 4: Create PR**
```bash
# Push if needed
git push -u origin feature-branch

# Create PR using GitHub CLI
gh pr create --title "Feature: Add user authentication" --body "$(cat <<'EOF'
## Summary
- Implement JWT-based authentication
- Add login/logout endpoints
- Create user session management

## Test plan
- [ ] Test login with valid credentials
- [ ] Test login with invalid credentials
- [ ] Test token expiration
- [ ] Test logout functionality

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

### Code Review Guidelines

**As Author:**
```bash
# Before requesting review:
✅ Self-review changes
✅ Run tests locally
✅ Check for console.log/debug code
✅ Update documentation
✅ Write clear PR description
```

**As Reviewer:**
```bash
# Review checklist:
✅ Understand what problem it solves
✅ Check logic correctness
✅ Look for edge cases
✅ Verify tests exist
✅ Check code style
✅ Suggest improvements (politely)
```

---

## 🪝 Hook Management

### Pre-Commit Hooks

**Common Pre-Commit Tasks:**
- Linting (ESLint, Pylint)
- Formatting (Prettier, Black)
- Type checking (TypeScript, mypy)
- Tests (unit tests)

**If Hook Modifies Files:**
```bash
# ❌ DON'T skip with --no-verify

# ✅ DO amend if safe:
# 1. Check authorship
git log -1 --format='%an %ae'

# 2. Check not pushed
git status | grep "ahead"

# 3. If both OK, amend
git add .
git commit --amend --no-edit

# 4. If not OK, new commit
git add .
git commit -m "Apply pre-commit hook changes"
```

---

### Managing Hooks

**Install hooks:**
```bash
# Using Husky (JavaScript)
npm install husky --save-dev
npx husky install

# Using pre-commit (Python)
pip install pre-commit
pre-commit install
```

**Temporarily disable (only if necessary):**
```bash
# Use with caution!
git commit --no-verify -m "Emergency fix"

# Document why in commit message
```

---

## ↩️ Revert & Recovery

### Safe Undo Operations

**Undo last commit (not pushed):**
```bash
# Keep changes in working directory
git reset --soft HEAD~1

# Discard changes (DANGEROUS!)
git reset --hard HEAD~1

# Recommended: Soft reset, review, recommit
git reset --soft HEAD~1
git status  # Review what will be uncommitted
git diff --staged  # See changes
# Make corrections
git commit -m "Corrected commit message"
```

---

### Undoing Pushed Commits

**Use revert (safe, creates new commit):**
```bash
# Revert last commit
git revert HEAD

# Revert specific commit
git revert <commit-hash>

# Revert multiple commits
git revert <oldest-hash>..<newest-hash>
```

**❌ NEVER force push to shared branches:**
```bash
# DON'T DO THIS on main/master or shared branches!
git reset --hard HEAD~1
git push --force

# Exception: Your own feature branch, no one else using
git push --force-with-lease  # Safer than --force
```

---

### Recovery Commands

**Find lost commits:**
```bash
# View reflog (history of HEAD)
git reflog

# Restore lost commit
git checkout <commit-hash>
git checkout -b recovered-work
```

**Recover deleted branch:**
```bash
# Find branch's last commit
git reflog | grep branch-name

# Recreate branch
git checkout -b branch-name <commit-hash>
```

**Recover deleted files:**
```bash
# Restore file from specific commit
git checkout <commit-hash> -- path/to/file

# Restore file from last commit
git checkout HEAD -- path/to/file
```

---

## ⚔️ Conflict Resolution

### Merge Conflicts

**When conflicts occur:**
```bash
# 1. See conflicted files
git status

# 2. Open conflicted file
# Look for conflict markers:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> branch-name

# 3. Resolve conflicts
# - Keep yours, theirs, or merge both
# - Remove conflict markers

# 4. Stage resolved files
git add <resolved-files>

# 5. Complete merge
git commit  # Or git merge --continue

# 6. Verify
git log --oneline --graph
```

---

### Conflict Resolution Strategies

**Strategy 1: Accept Theirs**
```bash
git checkout --theirs path/to/file
git add path/to/file
```

**Strategy 2: Accept Yours**
```bash
git checkout --ours path/to/file
git add path/to/file
```

**Strategy 3: Manual Merge**
```bash
# Edit file, keep best parts of both
# Remove <<<<<<, =======, >>>>>> markers
git add path/to/file
```

**Strategy 4: Abort and Start Over**
```bash
git merge --abort
# or
git rebase --abort
```

---

## 🏭 Production Safety

### Deploying to Production

**Pre-Deploy Checklist:**
```bash
✅ All tests pass
✅ Code reviewed and approved
✅ Staging environment tested
✅ Database migrations tested
✅ Rollback plan ready
✅ Monitoring in place
✅ Team notified
```

**Safe Deploy Process:**
```bash
# 1. Create release branch
git checkout -b release/v1.2.0 main

# 2. Final testing
npm test  # or your test command

# 3. Tag release
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0

# 4. Merge to main (via PR)

# 5. Deploy (pull on production server)
# ssh to production
git pull origin main
git checkout v1.2.0

# 6. Monitor
# Watch logs, metrics, errors
```

---

### Hotfix Workflow

**For urgent production fixes:**
```bash
# 1. Create hotfix branch from production tag
git checkout -b hotfix/critical-bug v1.2.0

# 2. Make minimal fix
git add .
git commit -m "Hotfix: Fix critical login bug"

# 3. Create hotfix tag
git tag -a v1.2.1 -m "Hotfix: Critical login bug"

# 4. Merge to main AND develop
git checkout main
git merge hotfix/critical-bug
git push origin main

git checkout develop
git merge hotfix/critical-bug
git push origin develop

# 5. Deploy hotfix
git push origin v1.2.1
```

---

## 📚 Git Commands Reference

### Essential Commands

**Status & Info:**
```bash
git status                    # Current state
git log --oneline -10         # Recent commits
git log --graph --all         # Visual branch history
git diff                      # Unstaged changes
git diff --staged             # Staged changes
git reflog                    # History of HEAD
```

**Branching:**
```bash
git branch                    # List branches
git branch <name>             # Create branch
git checkout <name>           # Switch branch
git checkout -b <name>        # Create and switch
git branch -d <name>          # Delete branch (safe)
git branch -D <name>          # Delete branch (force)
```

**Stashing:**
```bash
git stash                     # Stash changes
git stash save "message"      # Stash with message
git stash list                # List stashes
git stash apply               # Apply latest stash
git stash pop                 # Apply and delete stash
git stash drop                # Delete stash
```

**Remote:**
```bash
git remote -v                 # List remotes
git fetch origin              # Fetch changes
git pull origin main          # Fetch and merge
git push origin main          # Push to remote
git push -u origin branch     # Push and track
```

**Undoing:**
```bash
git reset --soft HEAD~1       # Undo commit, keep changes
git reset --hard HEAD~1       # Undo commit, discard changes
git revert HEAD               # Create revert commit
git clean -fd                 # Remove untracked files
```

---

### Advanced Commands

**Interactive Rebase:**
```bash
# Rewrite last 3 commits
git rebase -i HEAD~3

# In editor:
# pick = keep commit
# reword = change message
# squash = merge into previous
# drop = delete commit

# ⚠️ Only on unpushed commits!
```

**Cherry-Pick:**
```bash
# Copy commit from another branch
git cherry-pick <commit-hash>

# Multiple commits
git cherry-pick <hash1> <hash2>
```

**Bisect (find bug):**
```bash
# Start bisect
git bisect start
git bisect bad                 # Current is bad
git bisect good <commit>       # Known good commit

# Git checks out middle commit
# Test it
git bisect bad  # or git bisect good

# Repeat until bug found
git bisect reset  # When done
```

---

## 🎯 Quick Reference Checklist

**Before Every Commit:**
```bash
✅ git status          # Review changes
✅ git diff            # Check modifications
✅ git add <files>     # Stage selectively
✅ Test still passes
✅ Clear commit message ready
```

**Before Every Push:**
```bash
✅ git log -3          # Review commits
✅ git pull --rebase   # Get latest changes
✅ Tests pass
✅ No WIP commits
```

**Before Risky Operations:**
```bash
✅ Create backup branch
✅ Verify current branch
✅ git stash if needed
✅ Have rollback plan
```

---

## 🚨 Emergency Procedures

**"I committed to the wrong branch!"**
```bash
# On wrong branch
git log -1  # Get commit hash

# Switch to correct branch
git checkout correct-branch
git cherry-pick <commit-hash>

# Go back and remove from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

**"I pushed sensitive data!"**
```bash
# 1. Remove from all commits (REWRITE HISTORY)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive/file" \
  --prune-empty --tag-name-filter cat -- --all

# 2. Force push (everyone must re-clone!)
git push --force --all

# 3. Rotate compromised secrets immediately!
```

**"I deleted important code!"**
```bash
# Find when it existed
git log --all --full-history -- path/to/file

# Restore from commit
git checkout <commit-hash> -- path/to/file
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,000+
**Status:** Production Ready ✅
**Based on:** CLAUDE.md Git Safety Protocol
