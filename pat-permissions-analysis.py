#!/usr/bin/env python3
"""
Personal Access Token Permissions Analysis
Complete analysis of required PAT permissions for GitHub automation system
"""

import os
import re
import json
from pathlib import Path

def analyze_github_api_operations():
    """Analyze all GitHub API operations in the repository"""
    
    api_operations = []
    github_cli_operations = []
    files_analyzed = []
    
    # Define patterns to search for
    api_patterns = [
        r'gh api.*?-X\s+(GET|POST|PUT|PATCH|DELETE)',
        r'https://api\.github\.com/[\w/\-\{\}]+',
        r'requests\.(get|post|put|patch|delete)\(',
        r'Authorization.*token',
    ]
    
    github_cli_patterns = [
        r'gh\s+(\w+)',
        r'gh api.*?[\'"](.*?)[\'"]',
        r'gh repo view',
        r'gh workflow',
    ]
    
    def analyze_file(file_path):
        """Analyze a single file for GitHub operations"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            file_operations = []
            
            # Search for GitHub API operations
            for pattern in api_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
                if matches:
                    file_operations.extend([f"API: {match}" for match in matches])
            
            # Search for GitHub CLI operations
            for pattern in github_cli_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
                if matches:
                    file_operations.extend([f"CLI: {match}" for match in matches])
            
            # Look for specific endpoint patterns
            endpoints = re.findall(r'/repos/.*?["\s]', content)
            if endpoints:
                file_operations.extend([f"Endpoint: {ep.strip('\"\\s')}" for ep in endpoints])
            
            return file_operations
            
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return []
    
    # Analyze all relevant files
    analysis_paths = [
        '.github/workflows/',
        '.github/actions/',
        '.github/scripts/',
        '.',  # Root directory scripts
    ]
    
    for path in analysis_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(('.yml', '.yaml', '.py', '.js', '.sh', '.json')):
                        file_path = os.path.join(root, file)
                        operations = analyze_file(file_path)
                        if operations:
                            files_analyzed.append({
                                'file': file_path,
                                'operations': operations
                            })
    
    return files_analyzed

def extract_permissions_from_operations(operations_data):
    """Extract required permissions from identified operations"""
    
    required_permissions = {
        'classic_pat_scopes': set(),
        'fine_grained_permissions': set(),
        'api_endpoints': set(),
        'justifications': []
    }
    
    # Mapping of operations to required permissions
    operation_to_permissions = {
        # Repository operations
        'repos/.*/vulnerability-alerts': {
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Enable/disable Dependabot vulnerability alerts'
        },
        '/repos/.*': {
            'classic': ['repo'],
            'fine_grained': ['Contents: Write', 'Metadata: Read'],
            'reason': 'Repository information and modification'
        },
        'private_vulnerability_reporting': {
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Enable private vulnerability reporting'
        },
        'dependency_graph_enabled': {
            'classic': ['repo'],
            'fine_grained': ['Administration: Write'],
            'reason': 'Enable dependency graph'
        },
        'dependency_submission_enabled': {
            'classic': ['repo'],
            'fine_grained': ['Administration: Write'],
            'reason': 'Enable dependency submission'
        },
        'vulnerability_alerts': {  
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Enable vulnerability alerts'
        },
        'secret_scanning': {
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Configure secret scanning'
        },
        'secret_scanning_push_protection': {
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Configure push protection'
        },
        'advanced_security': {
            'classic': ['repo', 'security_events'],
            'fine_grained': ['Administration: Write', 'Security events: Write'],
            'reason': 'Enable GitHub Advanced Security'
        },
        # GitHub CLI operations
        'gh repo': {
            'classic': ['repo'],
            'fine_grained': ['Metadata: Read'],
            'reason': 'Repository information via CLI'
        },
        'gh api': {
            'classic': ['repo'],
            'fine_grained': ['Contents: Write'],
            'reason': 'Direct API access via CLI'
        },
        'gh workflow': {
            'classic': ['workflow', 'repo'],
            'fine_grained': ['Actions: Write', 'Contents: Write'],
            'reason': 'Workflow management via CLI'
        },
        # File operations
        'CODEOWNERS': {
            'classic': ['repo'],
            'fine_grained': ['Contents: Write'],
            'reason': 'Create and update CODEOWNERS file'
        },
        'dependabot.yml': {
            'classic': ['repo'],
            'fine_grained': ['Contents: Write'],  
            'reason': 'Create and update Dependabot configuration'
        },
        'pull_request_template': {
            'classic': ['repo'],
            'fine_grained': ['Contents: Write'],
            'reason': 'Create and update PR templates'
        },
        # Organization operations (for team-based CODEOWNERS)
        'read:org': {
            'classic': ['read:org'],
            'fine_grained': [],  # Handled at org level
            'reason': 'Read organization and team membership for CODEOWNERS'
        }
    }
    
    # Analyze operations and map to permissions
    for file_data in operations_data:
        file_path = file_data['file']
        operations = file_data['operations']
        
        for operation in operations:
            # Check against known patterns
            for pattern, perms in operation_to_permissions.items():
                if pattern in operation.lower() or re.search(pattern, operation, re.IGNORECASE):
                    required_permissions['classic_pat_scopes'].update(perms['classic'])
                    required_permissions['fine_grained_permissions'].update(perms['fine_grained'])
                    required_permissions['justifications'].append({
                        'file': file_path,
                        'operation': operation,
                        'reason': perms['reason'],
                        'classic_scopes': perms['classic'],
                        'fine_grained': perms['fine_grained']
                    })
            
            # Extract API endpoints
            if 'api.github.com' in operation or '/repos/' in operation:
                required_permissions['api_endpoints'].add(operation)
    
    # Add essential permissions that are always needed
    essential_permissions = {
        'classic': ['repo', 'admin:repo_hook', 'security_events', 'read:org'],
        'fine_grained': [
            'Administration: Write',
            'Contents: Write', 
            'Issues: Write',
            'Metadata: Read',
            'Pull requests: Write',
            'Security events: Write'
        ]
    }
    
    required_permissions['classic_pat_scopes'].update(essential_permissions['classic'])
    required_permissions['fine_grained_permissions'].update(essential_permissions['fine_grained'])
    
    # Add workflow scope if workflow files are modified
    workflow_files = [f for f in operations_data if '.github/workflows' in f['file']]
    if workflow_files:
        required_permissions['classic_pat_scopes'].add('workflow')
        required_permissions['fine_grained_permissions'].add('Actions: Write')
        required_permissions['justifications'].append({
            'file': 'Multiple workflow files',
            'operation': 'Workflow modification',
            'reason': 'Required to update GitHub Actions workflows',
            'classic_scopes': ['workflow'],
            'fine_grained': ['Actions: Write']
        })
    
    return required_permissions

def generate_permissions_report(permissions_data):
    """Generate a comprehensive permissions report"""
    
    report = []
    report.append("# 🔑 Complete Personal Access Token Permissions Analysis")
    report.append("## Repository: GitHub Assessment Automation System")
    report.append("")
    report.append("Based on comprehensive analysis of all workflows, scripts, and API operations.")
    report.append("")
    
    # Classic PAT Scopes
    report.append("## 📋 Classic Personal Access Token Scopes")
    report.append("")
    report.append("### Required Scopes (All Essential)")
    report.append("")
    
    scope_descriptions = {
        'repo': 'Full control of private repositories - Essential for all repository operations',
        'admin:repo_hook': 'Full control of repository hooks - Required for webhook management',
        'security_events': 'Read and write security events - Critical for security feature automation',
        'read:org': 'Read org and team membership - Needed for CODEOWNERS team references',
        'workflow': 'Update GitHub Action workflows - Required if modifying workflow files'
    }
    
    for scope in sorted(permissions_data['classic_pat_scopes']):
        description = scope_descriptions.get(scope, 'Required for automation operations')
        report.append(f"- ✅ **`{scope}`** - {description}")
    
    report.append("")
    
    # Fine-grained PAT permissions  
    report.append("## 🎯 Fine-grained Personal Access Token Permissions")
    report.append("")
    report.append("If using fine-grained tokens, ensure these permissions:")
    report.append("")
    report.append("### Repository Permissions")
    
    repo_permissions = [p for p in permissions_data['fine_grained_permissions'] if ':' in p]
    for permission in sorted(repo_permissions):
        report.append(f"- ✅ **{permission}**")
    
    report.append("")
    
    # API Endpoints
    report.append("## 🌐 GitHub API Endpoints Used")
    report.append("")
    report.append("The automation system interacts with these GitHub API endpoints:")
    report.append("")
    
    unique_endpoints = set()
    for endpoint in permissions_data['api_endpoints']:
        if '/repos/' in endpoint:
            # Normalize endpoint
            normalized = re.sub(r'\$\{\{.*?\}\}', '{repository}', endpoint)
            normalized = re.sub(r'ajeetchouksey/github_assessment', '{repository}', normalized)
            unique_endpoints.add(normalized)
    
    for endpoint in sorted(unique_endpoints):
        report.append(f"- `{endpoint}`")
    
    report.append("")
    
    # Security Features Matrix
    report.append("## 🔒 Security Features Automation Matrix")
    report.append("")
    report.append("| Security Feature | API Endpoint | Required Permissions |")
    report.append("|------------------|--------------|---------------------|")
    
    security_features = [
        ("Dependabot Vulnerability Alerts", "/repos/{repo}/vulnerability-alerts", "repo, security_events"),
        ("Private Vulnerability Reporting", "/repos/{repo}", "repo, security_events"),
        ("Dependency Graph", "/repos/{repo}", "repo"),
        ("Secret Scanning", "/repos/{repo}", "repo, security_events"),
        ("Push Protection", "/repos/{repo}", "repo, security_events"),
        ("Advanced Security", "/repos/{repo}", "repo, security_events"),
    ]
    
    for feature, endpoint, perms in security_features:
        report.append(f"| {feature} | `{endpoint}` | `{perms}` |")
    
    report.append("")
    
    # Justifications
    report.append("## 📝 Permission Justifications")
    report.append("")
    report.append("Detailed explanation of why each permission is required:")
    report.append("")
    
    # Group justifications by file
    files_with_justifications = {}
    for justification in permissions_data['justifications']:
        file_path = justification['file']
        if file_path not in files_with_justifications:
            files_with_justifications[file_path] = []
        files_with_justifications[file_path].append(justification)
    
    for file_path, justifications in sorted(files_with_justifications.items()):
        report.append(f"### 📄 `{file_path}`")
        report.append("")
        for j in justifications:
            report.append(f"- **Operation**: {j['operation']}")
            report.append(f"  - **Purpose**: {j['reason']}")
            report.append(f"  - **Classic Scopes**: `{', '.join(j['classic_scopes'])}`")
            if j['fine_grained']:
                report.append(f"  - **Fine-grained**: `{', '.join(j['fine_grained'])}`")
            report.append("")
    
    # Summary
    report.append("## 📊 Summary")
    report.append("")
    report.append(f"- **Total Classic Scopes Required**: {len(permissions_data['classic_pat_scopes'])}")
    report.append(f"- **Total Fine-grained Permissions**: {len(permissions_data['fine_grained_permissions'])}")
    report.append(f"- **API Endpoints Used**: {len(permissions_data['api_endpoints'])}")
    report.append(f"- **Files Analyzed**: {len(set(j['file'] for j in permissions_data['justifications']))}")
    report.append("")
    
    # Quick Setup Guide
    report.append("## 🚀 Quick PAT Setup Guide")
    report.append("")
    report.append("### Step 1: Create Classic PAT")
    report.append("1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)")
    report.append("2. Click 'Generate new token (classic)'")
    report.append("3. Set expiration to 90+ days")
    report.append("4. Select these scopes:")
    report.append("")
    
    for scope in sorted(permissions_data['classic_pat_scopes']):
        report.append(f"   - ✅ `{scope}`")
    
    report.append("")
    report.append("### Step 2: Add to Repository")
    report.append("1. Go to your repository → Settings → Secrets and variables → Actions")
    report.append("2. Click 'New repository secret'")
    report.append("3. Name: `GH_ADMIN_TOKEN`")
    report.append("4. Value: Paste your generated PAT")
    report.append("5. Click 'Add secret'")
    report.append("")
    
    report.append("### Step 3: Verify Setup")
    report.append("```bash")
    report.append("# Run the diagnostic script")
    report.append("python diagnose-automation.py")
    report.append("")
    report.append("# Should show: ✅ Ready to run")
    report.append("```")
    report.append("")
    
    report.append("---")
    report.append("")
    report.append("**✨ Once configured with proper permissions, all automation features will work seamlessly!**")
    
    return "\n".join(report)

def main():
    """Main analysis function"""
    print("🔍 Analyzing GitHub automation system for PAT permissions...")
    print("=" * 60)
    
    # Analyze operations
    operations_data = analyze_github_api_operations()
    print(f"📁 Analyzed {len(operations_data)} files with GitHub operations")
    
    # Extract permissions
    permissions_data = extract_permissions_from_operations(operations_data)
    print(f"🔑 Found {len(permissions_data['classic_pat_scopes'])} required classic scopes")
    print(f"🎯 Found {len(permissions_data['fine_grained_permissions'])} fine-grained permissions")
    
    # Generate report
    report = generate_permissions_report(permissions_data)
    
    # Save report
    with open('PAT_PERMISSIONS_ANALYSIS.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\n✅ Analysis complete!")
    print("📄 Report saved to: PAT_PERMISSIONS_ANALYSIS.md")
    
    # Display summary
    print("\n📋 SUMMARY - Required Classic PAT Scopes:")
    for scope in sorted(permissions_data['classic_pat_scopes']):
        print(f"   ✅ {scope}")
    
    print(f"\n🌐 Total API endpoints analyzed: {len(permissions_data['api_endpoints'])}")
    print("🚀 The system requires full repository admin permissions for complete automation.")

if __name__ == '__main__':
    main()
