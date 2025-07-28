# GitHub Repository Automation - Setup Guide
*Generated on 2025-07-28 at 18:24:15*

## Setup Status: ⚠️ Setup Required

### Issues Found:
1. Missing environment variable: GITHUB_TOKEN
2. Add GH_ADMIN_TOKEN secret to repository

## Required Personal Access Token Permissions

### Classic PAT Scopes (All Required)
- ✅ `admin:repo_hook`
- ✅ `read:org`
- ✅ `repo`
- ✅ `security_events`
- ✅ `workflow`

## Quick Setup Steps

1. **Create Personal Access Token**
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Create new token with all scopes listed above

2. **Add to Repository Secrets**
   - Go to repository → Settings → Secrets and variables → Actions
   - Add secret named `GH_ADMIN_TOKEN` with your token

3. **Install GitHub CLI** (for local use)
   - Windows: `winget install --id GitHub.cli`
   - macOS: `brew install gh`
   - Linux: See https://cli.github.com/

4. **Run Automation**
   - Go to Actions tab → Main Repository Automation → Run workflow

## Verification
```bash
# Run this toolkit again to verify setup
python tools/github-automation-toolkit.py --diagnose
```

---
*This is an automated GitHub repository management tool*