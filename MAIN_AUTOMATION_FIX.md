# Main Automation Fix Guide

## ✅ Issues Identified

The diagnostic script found the following issues with your GitHub automation:

### 1. 🔧 GitHub CLI Not Installed
**Problem**: The workflows use `gh` commands but GitHub CLI is not installed on your system.

**Solution**: Install GitHub CLI using one of these methods:
```powershell
# Option 1: Using winget (recommended)
winget install --id GitHub.cli

# Option 2: Using chocolatey
choco install gh

# Option 3: Download from https://cli.github.com/
```

### 2. 🔑 Invalid Personal Access Token
**Problem**: Your GH_ADMIN_TOKEN is either invalid or lacks required permissions.

**Solution**: Create a new Personal Access Token with proper permissions:

1. Go to [GitHub Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select these scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `admin:repo_hook` (Full control of repository hooks)
   - ✅ `security_events` (Read and write security events)
   - ✅ `read:org` (Read org and team membership)
4. Set expiration to 90 days or longer
5. Copy the generated token

### 3. 📝 Update Repository Secret
After creating the new token:

1. Go to your repository: https://github.com/ajeetchouksey/github_assessment
2. Navigate to Settings → Secrets and variables → Actions
3. Find `GH_ADMIN_TOKEN` and click "Update" (or create new if missing)
4. Paste your new token
5. Click "Update secret"

## 🚀 Quick Fix Commands

After installing GitHub CLI and updating your token, run these commands:

```powershell
# 1. Set your token locally for testing
$env:GH_ADMIN_TOKEN = "your-new-token-here"

# 2. Test GitHub CLI authentication
gh auth login

# 3. Test the diagnostic script again
python diagnose-automation.py

# 4. Once everything passes, trigger the main automation workflow on GitHub
```

## ✨ What Happens After the Fix

Once you fix these issues:

1. **Main Automation Workflow** will run successfully
2. **Security Features** will be properly enabled
3. **All Component Workflows** will work correctly
4. **Weekly Monitoring** will start functioning

## 🔍 Verification Steps

1. Run `python diagnose-automation.py` - should show "✅ Ready to run"
2. Go to your GitHub repository → Actions tab
3. Click "Main Repository Automation" → "Run workflow"
4. Watch the workflow complete successfully
5. Check that all security features are enabled in Settings → Security & analysis

## 📚 Additional Resources

- [Complete Setup Guide](SETUP_INSTRUCTIONS.md)
- [Automation Guide](GITHUB_AUTOMATION_GUIDE.md) 
- [Troubleshooting Section](GITHUB_AUTOMATION_GUIDE.md#troubleshooting)

---

**Need Help?** The issues are common setup problems that are easily fixable. Once you install GitHub CLI and update your token with proper permissions, everything should work perfectly!
