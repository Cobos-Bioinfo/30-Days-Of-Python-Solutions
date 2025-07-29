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

### 5. Push to GitHub
```bash
git push -u origin main
```
- Uploads code to GitHub
- `-u` sets `main` as default branch (only needed first time)

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `git status` | Shows changed/untracked files |
| `git log` | Displays commit history |
| `git clone URL` | Downloads a repository |

---

## Troubleshooting

### ❌ "Remote origin already exists"
```bash
git remote remove origin
git remote add origin NEW_URL
```

### ❌ Authentication Failed
- Use [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) instead of password