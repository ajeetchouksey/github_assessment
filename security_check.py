#!/usr/bin/env python3
"""
GitHub Security Status Checker
Verifies that all security features are properly enabled
"""

import requests
import os
import sys
import json

def check_security_status(repo_owner, repo_name, token):
    """Check the current security status of the repository"""
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    # Get repository information
    repo_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
    
    try:
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()
        
        print("🔍 Repository Security Status Check")
        print("=" * 50)
        print(f"Repository: {repo_data['full_name']}")
        print(f"Visibility: {repo_data['visibility']}")
        print(f"Private: {repo_data['private']}")
        print()
        
        # Check security features
        security_analysis = repo_data.get('security_and_analysis', {})
        
        print("🔒 Security Features Status:")
        print("-" * 30)
        
        # Advanced Security
        advanced_security = security_analysis.get('advanced_security', {})
        print(f"Advanced Security: {'✅ Enabled' if advanced_security.get('status') == 'enabled' else '❌ Disabled'}")
        
        # Secret Scanning
        secret_scanning = security_analysis.get('secret_scanning', {})
        print(f"Secret Scanning: {'✅ Enabled' if secret_scanning.get('status') == 'enabled' else '❌ Disabled'}")
        
        # Secret Scanning Push Protection
        secret_scanning_push = security_analysis.get('secret_scanning_push_protection', {})
        print(f"Push Protection: {'✅ Enabled' if secret_scanning_push.get('status') == 'enabled' else '❌ Disabled'}")
        
        # Dependabot
        print(f"Vulnerability Alerts: {'✅ Enabled' if repo_data.get('has_vulnerability_alerts') else '❌ Disabled'}")
        
        # Additional checks
        print()
        print("📊 Additional Repository Features:")
        print("-" * 35)
        print(f"Issues: {'✅ Enabled' if repo_data.get('has_issues') else '❌ Disabled'}")
        print(f"Wiki: {'✅ Enabled' if repo_data.get('has_wiki') else '❌ Disabled'}")
        print(f"Projects: {'✅ Enabled' if repo_data.get('has_projects') else '❌ Disabled'}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error checking repository status: {e}")
        return False

if __name__ == '__main__':
    # You would typically get these from environment variables or command line
    REPO_OWNER = 'ajeetchouksey'
    REPO_NAME = 'github_assessment'
    
    # In a real scenario, this would come from environment variable
    # TOKEN = os.environ.get('GITHUB_TOKEN')
    
    print("To use this script:")
    print("1. Set GITHUB_TOKEN environment variable with your PAT")
    print("2. Run: python security_check.py")
    print()
    print("Or run via GitHub Actions with the GH_ADMIN_TOKEN secret")
    
    # Uncomment below when ready to use
    # if not TOKEN:
    #     print("❌ GITHUB_TOKEN environment variable not set")
    #     sys.exit(1)
    # 
    # success = check_security_status(REPO_OWNER, REPO_NAME, TOKEN)
    # sys.exit(0 if success else 1)
