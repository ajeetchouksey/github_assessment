#!/usr/bin/env python3
"""
GitHub Automation Diagnostics Script
Diagnoses common issues with the main automation workflow
"""

import requests
import os
import sys
import json
import subprocess

def diagnose_environment():
    """Diagnose local environment for common issues"""
    print("🔍 GitHub Automation Diagnostics")
    print("=" * 50)
    
    issues_found = []
    
    # Check if running in GitHub Actions
    if os.environ.get('GITHUB_ACTIONS'):
        print("✅ Running in GitHub Actions environment")
        return diagnose_github_actions()
    else:
        print("📍 Running in local environment")
        return diagnose_local_environment()

def diagnose_local_environment():
    """Diagnose local environment setup"""
    issues_found = []
    
    # Check GitHub CLI installation
    print("\n1. GitHub CLI Installation Check")
    print("-" * 30)
    
    try:
        result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ GitHub CLI is installed")
            print(f"   Version: {result.stdout.strip()}")
        else:
            print("❌ GitHub CLI not working properly")
            issues_found.append("Install GitHub CLI from https://cli.github.com/")
    except FileNotFoundError:
        print("❌ GitHub CLI (gh) is not installed")
        issues_found.append("Install GitHub CLI from https://cli.github.com/")
    
    # Check GitHub CLI authentication
    print("\n2. GitHub CLI Authentication Check")
    print("-" * 35)
    
    try:
        result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ GitHub CLI is authenticated")
            print(f"   {result.stdout.strip()}")
        else:
            print("❌ GitHub CLI is not authenticated")
            print(f"   Error: {result.stderr.strip()}")
            issues_found.append("Run 'gh auth login' to authenticate GitHub CLI")
    except FileNotFoundError:
        print("❌ Cannot check authentication - GitHub CLI not found")
    
    # Check environment variables
    print("\n3. Environment Variables Check")
    print("-" * 32)
    
    gh_token = os.environ.get('GH_ADMIN_TOKEN')
    if gh_token:
        print("✅ GH_ADMIN_TOKEN environment variable is set")
        print(f"   Length: {len(gh_token)} characters")
        
        # Validate token
        if validate_github_token(gh_token):
            print("✅ Token appears to be valid")
        else:
            print("❌ Token validation failed")
            issues_found.append("Check GH_ADMIN_TOKEN validity and permissions")
    else:
        print("❌ GH_ADMIN_TOKEN environment variable not set")
        issues_found.append("Set GH_ADMIN_TOKEN environment variable with your PAT")
    
    return issues_found

def diagnose_github_actions():
    """Diagnose GitHub Actions environment"""
    issues_found = []
    
    print("\n1. GitHub Actions Environment Check")
    print("-" * 35)
    
    # Check required environment variables
    required_vars = ['GITHUB_REPOSITORY', 'GITHUB_TOKEN', 'GITHUB_ACTOR']
    for var in required_vars:
        if os.environ.get(var):
            print(f"✅ {var} is available")
        else:
            print(f"❌ {var} is missing")
            issues_found.append(f"Missing environment variable: {var}")
    
    # Check secrets
    print("\n2. Repository Secrets Check")
    print("-" * 28)
    
    gh_admin_token = os.environ.get('GH_ADMIN_TOKEN')
    if gh_admin_token:
        print("✅ GH_ADMIN_TOKEN secret is available")
        
        # Validate token permissions
        if validate_github_token(gh_admin_token):
            print("✅ Token has valid permissions")
        else:
            print("❌ Token validation failed or insufficient permissions")
            issues_found.append("Check GH_ADMIN_TOKEN secret permissions")
    else:
        print("❌ GH_ADMIN_TOKEN secret is not available")
        issues_found.append("Add GH_ADMIN_TOKEN secret to repository")
    
    return issues_found

def validate_github_token(token):
    """Validate GitHub token and check permissions"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    
    try:
        # Test basic API access
        response = requests.get('https://api.github.com/user', headers=headers)
        if response.status_code != 200:
            print(f"   Token validation failed: HTTP {response.status_code}")
            return False
        
        user_data = response.json()
        print(f"   Token belongs to: {user_data.get('login', 'Unknown')}")
        
        # Check token scopes
        scopes = response.headers.get('X-OAuth-Scopes', '').split(', ')
        required_scopes = ['repo', 'admin:repo_hook', 'security_events']
        
        print(f"   Available scopes: {', '.join(scopes) if scopes[0] else 'None'}")
        
        missing_scopes = [scope for scope in required_scopes if scope not in scopes]
        if missing_scopes:
            print(f"   ⚠️  Missing recommended scopes: {', '.join(missing_scopes)}")
            return False
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"   Token validation error: {e}")
        return False

def print_solutions(issues_found):
    """Print solutions for identified issues"""
    if not issues_found:
        print("\n🎉 No issues found! Your automation should work correctly.")
        return
    
    print(f"\n❌ Found {len(issues_found)} issue(s) that need attention:")
    print("=" * 60)
    
    for i, issue in enumerate(issues_found, 1):
        print(f"{i}. {issue}")
    
    print("\n💡 Quick Solutions:")
    print("=" * 20)
    
    if any('GitHub CLI' in issue for issue in issues_found):
        print("📥 Install GitHub CLI:")
        print("   Windows: winget install --id GitHub.cli")
        print("   macOS: brew install gh")
        print("   Linux: https://github.com/cli/cli/blob/trunk/docs/install_linux.md")
        print()
    
    if any('authenticate' in issue for issue in issues_found):
        print("🔐 Authenticate GitHub CLI:")
        print("   Run: gh auth login")
        print("   Follow the interactive prompts")
        print()
    
    if any('GH_ADMIN_TOKEN' in issue for issue in issues_found):
        print("🔑 Setup Personal Access Token:")
        print("   1. Go to GitHub → Settings → Developer settings → Personal access tokens")
        print("   2. Create a new token with these scopes:")
        print("      - repo (Full control of private repositories)")
        print("      - admin:repo_hook (Full control of repository hooks)") 
        print("      - security_events (Read and write security events)")
        print("   3. For local use: $env:GH_ADMIN_TOKEN='your-token-here'")
        print("   4. For GitHub Actions: Add as repository secret named 'GH_ADMIN_TOKEN'")
        print()
    
    print("📚 For detailed setup instructions, see: SETUP_INSTRUCTIONS.md")

def main():
    """Main diagnostic function"""
    issues = diagnose_environment()
    print_solutions(issues)
    
    print(f"\n📊 Diagnostic Summary:")
    print(f"   Environment: {'GitHub Actions' if os.environ.get('GITHUB_ACTIONS') else 'Local'}")
    print(f"   Issues found: {len(issues)}")
    print(f"   Status: {'❌ Needs attention' if issues else '✅ Ready to run'}")
    
    return len(issues) == 0

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
