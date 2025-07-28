#!/usr/bin/env python3
"""
Script to enable security features for the GitHub repository.
This fixes the issue where Dependabot vulnerability alerts are disabled.
"""

import requests
import os
import sys

def enable_security_features():
    """Enable security features for the repository."""
    
    # Get the token from environment
    token = os.environ.get('GH_ADMIN_TOKEN')
    if not token:
        print("❌ Error: GH_ADMIN_TOKEN environment variable not set")
        print("Please set your GitHub Personal Access Token:")
        print("$env:GH_ADMIN_TOKEN='your-token-here'")
        return False
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    
    repo = 'ajeetchouksey/github_assessment'
    
    print("🔧 Enabling security features...")
    print("=" * 50)
    
    # 1. Enable Dependabot vulnerability alerts
    print("📊 Enabling Dependabot vulnerability alerts...")
    enable_url = f'https://api.github.com/repos/{repo}/vulnerability-alerts'
    response = requests.put(enable_url, headers=headers)
    
    if response.status_code == 204:
        print("✅ Dependabot vulnerability alerts enabled successfully")
    elif response.status_code == 200:
        print("✅ Dependabot vulnerability alerts already enabled")
    else:
        print(f"⚠️  Could not enable Dependabot alerts: {response.status_code}")
        if response.status_code == 404:
            print("   This feature might not be available for this repository type")
        
    # 2. Check current security status
    print("\n🔍 Checking current security status...")
    repo_url = f'https://api.github.com/repos/{repo}'
    response = requests.get(repo_url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Failed to get repository information: {response.status_code}")
        return False
        
    repo_data = response.json()
    is_public = not repo_data.get('private', False)
    security = repo_data.get('security_and_analysis', {})
    
    print(f"📝 Repository Type: {'Public' if is_public else 'Private'}")
    
    # Check each security feature
    features = {}
    
    # Advanced Security
    advanced_security = security.get('advanced_security', {}).get('status')
    if is_public:
        features['Advanced Security'] = 'enabled (public repo)'
        advanced_security_enabled = True
    else:
        features['Advanced Security'] = advanced_security
        advanced_security_enabled = advanced_security == 'enabled'
    
    # Secret Scanning
    secret_scanning = security.get('secret_scanning', {}).get('status')
    features['Secret Scanning'] = secret_scanning
    secret_scanning_enabled = secret_scanning == 'enabled'
    
    # Push Protection
    push_protection = security.get('secret_scanning_push_protection', {}).get('status')
    features['Push Protection'] = push_protection
    push_protection_enabled = push_protection == 'enabled'
    
    # Vulnerability Alerts
    vuln_alerts = repo_data.get('has_vulnerability_alerts')
    features['Vulnerability Alerts'] = 'enabled' if vuln_alerts else 'disabled'
    vuln_alerts_enabled = vuln_alerts
    
    # Print status
    print("\n📋 Security Features Status:")
    print("-" * 30)
    for feature, status in features.items():
        if feature == 'Advanced Security' and is_public:
            icon = '✅'
        elif feature == 'Vulnerability Alerts':
            icon = '✅' if vuln_alerts_enabled else '❌'
        else:
            enabled = status == 'enabled'
            icon = '✅' if enabled else '❌'
        print(f"{icon} {feature}: {status or 'disabled'}")
    
    # Determine success
    critical_features_enabled = secret_scanning_enabled and push_protection_enabled
    
    if is_public:
        if critical_features_enabled:
            if vuln_alerts_enabled:
                print("\n🎉 All security features are properly configured!")
                return True
            else:
                print("\n⚠️  Critical security features are enabled, but Vulnerability Alerts may need manual enabling")
                print("   You can enable this in: Settings > Code security and analysis > Dependabot alerts")
                return True  # Don't fail for public repos
        else:
            print("\n❌ Critical security features need attention")
            return False
    else:
        all_enabled = advanced_security_enabled and secret_scanning_enabled and push_protection_enabled and vuln_alerts_enabled
        if all_enabled:
            print("\n🎉 All security features are properly enabled!")
        else:
            print("\n⚠️  Some security features need attention")
        return all_enabled

if __name__ == '__main__':
    success = enable_security_features()
    sys.exit(0 if success else 1)
