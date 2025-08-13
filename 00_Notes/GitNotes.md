# How to Upload Code from VSCode to GitHub

## Basic Steps

### 1. Initialize Git
```bash
git init
```
- Turns your project folder into a Git repository  
- Run this **once per project**

### 2. Stage Files
```bash
git add .
```
- Prepares all files for commit (use `git add filename` for specific files)

### 3. Commit Changes
```bash
git commit -m "Descriptive message"
```
- Saves a snapshot with your changes  
- Always write clear messages (e.g., "Fixed login page styling")

### 4. Connect to GitHub
```bash
git remote add origin https://github.com/username/repo.git
```
- Links local project to GitHub  
- Replace URL with your actual repository

### 5. Sync with Remote (Before Pushing or Pulling)
```bash
git fetch origin
git status
```
- `git fetch origin` retrieves any changes from the remote (e.g., commits, branches) without merging them  
- `git status` shows if there are any changes from the remote that haven't been incorporated locally

### 6. Push to GitHub
```bash
git push -u origin main
```
- Uploads code to GitHub  
- `-u` sets `main` as default branch (only needed first time)

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `git status` | Shows changed/untracked files and remote sync status |
| `git log` | Displays commit history |
| `git fetch origin` | Retrieves new commits/branches from remote without merging |
| `git clone URL` | Downloads a repository |
| `git reset` | Undoes commits (see troubleshooting below) |

---

## Troubleshooting

### ❌ "Remote origin already exists"
```bash
git remote remove origin
git remote add origin NEW_URL
```
### ❌ Need to undo local commits
```bash
git reset --soft HEAD~1  # Keeps changes staged
git reset --hard HEAD~1  # Discards changes completely
git reset <commit-hash>  # Reverts to specific commit
```