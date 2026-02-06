
---

# Team Git Workflow Guidelines

This repository uses a two-branch workflow to keep work organized, stable, and easy to review.

## Branches

**main**
Stable branch used for demos and final submissions.
Protected: pull requests only.

**development**
Integration branch where all work is merged first.
Protected: pull requests only.

Direct pushes to `main` or `development` are restricted.

---

## One-time setup (everyone)

Configure your Git identity so individual contributions are visible:

```
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"
```

---

## Daily workflow

### 1. Sync `development` before starting work

```
git switch development
git pull --ff-only
```

### 2. Create a work branch

```
git switch -c <short-task-name>
```

Example: `result-page`

### 3. Make changes and commit

Commit as often as makes sense.

```
git add -A
git commit -m "Clear description of change"
```

---

## Commit message guidelines

Use [Chris Beams' seven rules](https://chris.beams.io/git-commit#seven-rules) as the required standard to keep the history readable and consistent.

Short version:

* Start with a capital letter.
* Do not include a trailing period.
* Keep it to one concise line.

Examples:

```
Add contribution guidelines
Handle missing passenger age
Add survival prediction endpoint
```

### 4. Sync again before pushing

This reduces conflicts.

```
git switch development
git pull --ff-only
git switch <task-branch>
git merge development
```

### 5. Push and open a pull request

```
git push -u origin <task-branch>
```

Open a pull request from `<task-branch>` to `development`.

---

## Pull request rules

* Review pull requests when possible.
* Merge method: **Create a merge commit** (do not squash).
  This preserves the full commit history for each contributor.
* Delete the work branch after merging.

---

## Releases (`development` → `main`)

Only merge to `main` at agreed milestones (demos, checkpoints, final submission).

1. Open a pull request from `development` to `main`.
2. Merge using **Create a merge commit**.
3. Immediately open a pull request from `main` back to `development` and merge it.
   This keeps `development` in sync with `main`.

---

## Hard rules

* Always run `git pull --ff-only` before starting work and before pushing.
* Never rebase `development` or `main`.
* If `git pull --ff-only` fails, stop and ask for help before proceeding.

Following these rules keeps the history clear, avoids unnecessary conflicts, and ensures contributions are easy to review.
