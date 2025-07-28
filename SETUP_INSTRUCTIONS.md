# GitHub Security Setup Instructions

## 1. Create Personal Access Token (PAT)

### Steps:
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Set expiration to 90 days or longer
4. Select these scopes:
   - `repo` (Full control of private repositories)
   - `admin:repo_hook` (Full control of repository hooks)
   - `read:org` (Read org and team membership)
   - `security_events` (Read and write security events)

### Add to Repository Secrets:
1. Go to your repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GH_ADMIN_TOKEN`
4. Value: Paste your generated PAT
5. Click "Add secret"

## 2. Verify Security Features Status

After adding the PAT, run the main automation workflow to enable all security features.

## 3. Check Security Settings

Once PAT is configured, you should be able to access:
- Repository Settings → Security & analysis
- Code security and analysis features

## 4. Branch Protection (Recommended)

1. Go to Settings → Branches
2. Add rule for `main` branch:
   - Require pull request reviews
   - Require status checks to pass
   - Restrict pushes to matching branches
