#!/usr/bin/env python3
"""
GitHub Repository Automation Toolkit - Enterprise Edition
Complete toolkit for GitHub repository automation setup, diagnostics, and analysis

🏢 ENTERPRISE DEPLOYMENT NOTICE:
This toolkit provides comprehensive, enterprise-grade automation capabilities.
Organizations must conduct thorough assessment and customization before deployment.
Evaluate all components against your specific security policies, compliance requirements,
and operational procedures. Professional implementation and pilot testing strongly recommended.

Author: GitHub Copilot Automation System
Version: 2.0 (Enterprise Edition)
License: MIT
"""

import os
import sys
import re
import json
import requests
import subprocess
from pathlib import Path
from datetime import datetime

class GitHubAutomationToolkit:
    """Complete toolkit for GitHub automation management"""
    
    def __init__(self):
        self.repo_root = Path.cwd()
        self.issues_found = []
        
    def print_header(self, title, char="="):
        """Print formatted header"""
        print(f"\n{title}")
        print(char * len(title))
    
    def print_section(self, title, char="-"):
        """Print formatted section"""
        print(f"\n{title}")
        print(char * len(title))
    
    def validate_github_token(self, token):
        """Validate GitHub token and check permissions"""
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github+json'
        }
        
        try:
            response = requests.get('https://api.github.com/user', headers=headers)
            if response.status_code != 200:
                print(f"   ❌ Token validation failed: HTTP {response.status_code}")
                return False
            
            user_data = response.json()
            print(f"   ✅ Token belongs to: {user_data.get('login', 'Unknown')}")
            
            # Check token scopes
            scopes = response.headers.get('X-OAuth-Scopes', '').split(', ')
            required_scopes = ['repo', 'admin:repo_hook', 'security_events', 'read:org', 'workflow']
            
            print(f"   📋 Available scopes: {', '.join(scopes) if scopes[0] else 'None'}")
            
            missing_scopes = [scope for scope in required_scopes if scope not in scopes]
            if missing_scopes:
                print(f"   ⚠️  Missing required scopes: {', '.join(missing_scopes)}")
                return False
            
            print("   ✅ Token has all required permissions")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Token validation error: {e}")
            return False
    
    def detect_github_server_type(self):
        """Detect GitHub server type and capabilities"""
        self.print_header("🏢 GitHub Server Type Detection")
        
        # Get environment variables
        api_url = os.environ.get('GITHUB_API_URL', 'https://api.github.com')
        server_url = os.environ.get('GITHUB_SERVER_URL', 'https://github.com')
        
        print(f"🌐 API URL: {api_url}")
        print(f"🏠 Server URL: {server_url}")
        
        # Determine server type
        if api_url == "https://api.github.com":
            if server_url == "https://github.com":
                server_type = "github-com"
                server_description = "GitHub.com"
            else:
                server_type = "ghec"
                server_description = "GitHub Enterprise Cloud"
        else:
            server_type = "ghes"
            server_description = "GitHub Enterprise Server"
        
        print(f"📍 Detected: {server_description}")
        
        # Try to get server version for GHES
        server_version = "unknown"
        if server_type == "ghes":
            print("\n🔍 Attempting to detect GHES version...")
            gh_token = os.environ.get('GH_ADMIN_TOKEN') or os.environ.get('GITHUB_TOKEN')
            
            if gh_token:
                try:
                    headers = {
                        'Authorization': f'token {gh_token}',
                        'Accept': 'application/vnd.github+json'
                    }
                    response = requests.get(f'{api_url}/meta', headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        meta_data = response.json()
                        server_version = meta_data.get('installed_version', 'unknown')
                        print(f"📋 GHES Version: {server_version}")
                    else:
                        print(f"⚠️  Could not fetch server meta (HTTP {response.status_code})")
                        
                except requests.exceptions.RequestException as e:
                    print(f"⚠️  Error fetching server meta: {e}")
            else:
                print("⚠️  No GitHub token available for version detection")
        
        # Determine feature support
        capabilities = self._determine_server_capabilities(server_type, server_version)
        
        # Display results
        self.print_section("Server Capabilities")
        print(f"   🏢 Server Type: {server_type}")
        print(f"   📋 Version: {server_version}")
        print(f"   🔒 Advanced Security: {'✅' if capabilities['advanced_security'] else '❌'}")
        print(f"   🔍 Secret Scanning: {'✅' if capabilities['secret_scanning'] else '❌'}")
        print(f"   📊 Code Scanning: {'✅' if capabilities['code_scanning'] else '❌'}")
        print(f"   📈 Dependency Review: {'✅' if capabilities['dependency_review'] else '❌'}")
        
        return {
            'server_type': server_type,
            'server_description': server_description,
            'api_url': api_url,
            'server_url': server_url,
            'version': server_version,
            'capabilities': capabilities
        }
    
    def _determine_server_capabilities(self, server_type, server_version):
        """Determine what features are supported based on server type and version"""
        
        if server_type in ["github-com", "ghec"]:
            # GitHub.com and GHEC support all features
            return {
                'advanced_security': True,
                'secret_scanning': True,
                'code_scanning': True,
                'dependency_review': True
            }
        
        elif server_type == "ghes":
            # GHES feature support depends on version
            capabilities = {
                'advanced_security': False,
                'secret_scanning': False,
                'code_scanning': False,
                'dependency_review': False
            }
            
            if server_version and server_version != "unknown":
                try:
                    # Extract major.minor version
                    version_parts = server_version.split('.')
                    if len(version_parts) >= 2:
                        major = int(version_parts[0])
                        minor = int(version_parts[1])
                        version_float = major + (minor / 10.0)
                        
                        # GitHub Advanced Security available since GHES 3.0
                        if version_float >= 3.0:
                            capabilities['advanced_security'] = True
                            capabilities['secret_scanning'] = True
                            capabilities['code_scanning'] = True
                        
                        # Dependency review available since GHES 3.2
                        if version_float >= 3.2:
                            capabilities['dependency_review'] = True
                            
                except (ValueError, IndexError):
                    print(f"⚠️  Could not parse version: {server_version}")
            
            return capabilities
        
        # Default to no advanced features for unknown server types
        return {
            'advanced_security': False,
            'secret_scanning': False,
            'code_scanning': False,
            'dependency_review': False
        }

    def diagnose_environment(self):
        """Diagnose environment setup"""
        self.print_header("🔍 GitHub Automation Environment Diagnostics")
        
        self.issues_found = []
        
        if os.environ.get('GITHUB_ACTIONS'):
            print("✅ Running in GitHub Actions environment")
            self._diagnose_github_actions()
        else:
            print("📍 Running in local environment")
            self._diagnose_local_environment()
        
        return self.issues_found
    
    def _diagnose_local_environment(self):
        """Diagnose local environment setup"""
        
        # Check GitHub CLI installation
        self.print_section("1. GitHub CLI Installation Check")
        
        try:
            result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ GitHub CLI is installed")
                print(f"   Version: {result.stdout.strip()}")
            else:
                print("❌ GitHub CLI not working properly")
                self.issues_found.append("Install GitHub CLI from https://cli.github.com/")
        except FileNotFoundError:
            print("❌ GitHub CLI (gh) is not installed")
            self.issues_found.append("Install GitHub CLI from https://cli.github.com/")
        
        # Check GitHub CLI authentication
        self.print_section("2. GitHub CLI Authentication Check")
        
        try:
            result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ GitHub CLI is authenticated")
                print(f"   {result.stdout.strip()}")
            else:
                print("❌ GitHub CLI is not authenticated")
                print(f"   Error: {result.stderr.strip()}")
                self.issues_found.append("Run 'gh auth login' to authenticate GitHub CLI")
        except FileNotFoundError:
            print("❌ Cannot check authentication - GitHub CLI not found")
        
        # Check environment variables
        self.print_section("3. Environment Variables Check")
        
        gh_token = os.environ.get('GH_ADMIN_TOKEN')
        if gh_token:
            print("✅ GH_ADMIN_TOKEN environment variable is set")
            print(f"   Length: {len(gh_token)} characters")
            
            if self.validate_github_token(gh_token):
                print("✅ Token appears to be valid")
            else:
                print("❌ Token validation failed")
                self.issues_found.append("Check GH_ADMIN_TOKEN validity and permissions")
        else:
            print("❌ GH_ADMIN_TOKEN environment variable not set")
            self.issues_found.append("Set GH_ADMIN_TOKEN environment variable with your PAT")
    
    def _diagnose_github_actions(self):
        """Diagnose GitHub Actions environment"""
        
        self.print_section("1. GitHub Actions Environment Check")
        
        required_vars = ['GITHUB_REPOSITORY', 'GITHUB_TOKEN', 'GITHUB_ACTOR']
        for var in required_vars:
            if os.environ.get(var):
                print(f"✅ {var} is available")
            else:
                print(f"❌ {var} is missing")
                self.issues_found.append(f"Missing environment variable: {var}")
        
        self.print_section("2. Repository Secrets Check")
        
        gh_admin_token = os.environ.get('GH_ADMIN_TOKEN')
        if gh_admin_token:
            print("✅ GH_ADMIN_TOKEN secret is available")
            
            if self.validate_github_token(gh_admin_token):
                print("✅ Token has valid permissions")
            else:
                print("❌ Token validation failed or insufficient permissions")
                self.issues_found.append("Check GH_ADMIN_TOKEN secret permissions")
        else:
            print("❌ GH_ADMIN_TOKEN secret is not available")
            self.issues_found.append("Add GH_ADMIN_TOKEN secret to repository")
    
    def analyze_permissions(self):
        """Analyze all GitHub API operations for PAT permissions"""
        self.print_header("🔑 Personal Access Token Permissions Analysis")
        
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
        
        files_analyzed = []
        
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
                            operations = self._analyze_file_operations(file_path, api_patterns, github_cli_patterns)
                            if operations:
                                files_analyzed.append({
                                    'file': file_path,
                                    'operations': operations
                                })
        
        # Extract and display permissions
        permissions_data = self._extract_permissions(files_analyzed)
        
        print(f"\n📁 Analyzed {len(files_analyzed)} files with GitHub operations")
        print(f"🔑 Required Classic PAT Scopes: {len(permissions_data['classic_scopes'])}")
        print(f"🎯 Fine-grained Permissions: {len(permissions_data['fine_grained'])}")
        print(f"🌐 API Endpoints: {len(permissions_data['endpoints'])}")
        
        self.print_section("Required Classic PAT Scopes")
        for scope in sorted(permissions_data['classic_scopes']):
            print(f"   ✅ {scope}")
        
        return permissions_data
    
    def _analyze_file_operations(self, file_path, api_patterns, github_cli_patterns):
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
    
    def _extract_permissions(self, files_analyzed):
        """Extract required permissions from operations"""
        classic_scopes = set()
        fine_grained = set()
        endpoints = set()
        
        # Essential scopes for GitHub automation
        classic_scopes.update([
            'repo',  # Full control of repositories
            'admin:repo_hook',  # Repository hooks
            'security_events',  # Security events
            'read:org',  # Organization read
            'workflow'  # Workflow management
        ])
        
        fine_grained.update([
            'Administration: Write',
            'Contents: Write',
            'Metadata: Read',
            'Security events: Write',
            'Actions: Write',
            'Pull requests: Write',
            'Issues: Write'
        ])
        
        # Collect all endpoints
        for file_data in files_analyzed:
            for operation in file_data['operations']:
                if operation.startswith('Endpoint:'):
                    endpoint = operation.replace('Endpoint:', '').strip()
                    if '/repos/' in endpoint:
                        endpoints.add(endpoint)
        
        return {
            'classic_scopes': classic_scopes,
            'fine_grained': fine_grained,
            'endpoints': endpoints
        }
    
    def generate_setup_report(self):
        """Generate comprehensive setup and permissions report"""
        self.print_header("📄 Generating Setup Report")
        
        # Run diagnostics
        issues = self.diagnose_environment()
        
        # Analyze permissions
        permissions = self.analyze_permissions()
        
        # Generate report content
        report = self._create_setup_report(issues, permissions)
        
        # Save report
        report_file = self.repo_root / 'AUTOMATION_SETUP_GUIDE.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Setup report saved to: {report_file}")
        return report_file
    
    def _create_setup_report(self, issues, permissions):
        """Create comprehensive setup report"""
        report = []
        
        report.append("# GitHub Repository Automation - Setup Guide")
        report.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*")
        report.append("")
        
        # Status summary
        status = "✅ Ready" if not issues else "⚠️ Setup Required"
        report.append(f"## Setup Status: {status}")
        report.append("")
        
        if issues:
            report.append("### Issues Found:")
            for i, issue in enumerate(issues, 1):
                report.append(f"{i}. {issue}")
            report.append("")
        
        # Required PAT permissions
        report.append("## Required Personal Access Token Permissions")
        report.append("")
        report.append("### Classic PAT Scopes (All Required)")
        for scope in sorted(permissions['classic_scopes']):
            report.append(f"- ✅ `{scope}`")
        report.append("")
        
        # Quick setup instructions
        report.append("## Quick Setup Steps")
        report.append("")
        report.append("1. **Create Personal Access Token**")
        report.append("   - Go to GitHub → Settings → Developer settings → Personal access tokens")
        report.append("   - Create new token with all scopes listed above")
        report.append("")
        report.append("2. **Add to Repository Secrets**")
        report.append("   - Go to repository → Settings → Secrets and variables → Actions")
        report.append("   - Add secret named `GH_ADMIN_TOKEN` with your token")
        report.append("")
        report.append("3. **Install GitHub CLI** (for local use)")
        report.append("   - Windows: `winget install --id GitHub.cli`")
        report.append("   - macOS: `brew install gh`")
        report.append("   - Linux: See https://cli.github.com/")
        report.append("")
        report.append("4. **Run Automation**")
        report.append("   - Go to Actions tab → Main Repository Automation → Run workflow")
        report.append("")
        
        # Verification
        report.append("## Verification")
        report.append("```bash")
        report.append("# Run this toolkit again to verify setup")
        report.append("python tools/github-automation-toolkit.py --diagnose")
        report.append("```")
        report.append("")
        
        report.append("---")
        report.append("*This is an automated GitHub repository management tool*")
        
        return "\n".join(report)
    
    def print_solutions(self, issues):
        """Print solutions for identified issues"""
        if not issues:
            print("\n🎉 No issues found! Your automation should work correctly.")
            return
        
        print(f"\n❌ Found {len(issues)} issue(s) that need attention:")
        print("=" * 60)
        
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
        
        print("\n💡 Quick Solutions:")
        print("=" * 20)
        
        if any('GitHub CLI' in issue for issue in issues):
            print("📥 Install GitHub CLI:")
            print("   Windows: winget install --id GitHub.cli")
            print("   macOS: brew install gh")
            print("   Linux: https://github.com/cli/cli/blob/trunk/docs/install_linux.md")
            print()
        
        if any('authenticate' in issue for issue in issues):
            print("🔐 Authenticate GitHub CLI:")
            print("   Run: gh auth login")
            print("   Follow the interactive prompts")
            print()
        
        if any('GH_ADMIN_TOKEN' in issue for issue in issues):
            print("🔑 Setup Personal Access Token:")
            print("   1. Go to GitHub → Settings → Developer settings → Personal access tokens")
            print("   2. Create a new token with these scopes:")
            print("      - repo (Full control of private repositories)")
            print("      - admin:repo_hook (Full control of repository hooks)")
            print("      - security_events (Read and write security events)")
            print("      - read:org (Read org membership)")
            print("      - workflow (Update workflows)")
            print("   3. For local use: $env:GH_ADMIN_TOKEN='your-token-here'")
            print("   4. For GitHub Actions: Add as repository secret named 'GH_ADMIN_TOKEN'")
            print()
    
    def validate_workflows(self):
        """Validate GitHub workflow files"""
        self.print_header("🔧 Workflow Validation")
        
        workflows_dir = self.repo_root / '.github' / 'workflows'
        if not workflows_dir.exists():
            print("❌ No .github/workflows directory found")
            return False
        
        issues_found = []
        workflow_files = list(workflows_dir.glob('*.yml')) + list(workflows_dir.glob('*.yaml'))
        
        for workflow_file in workflow_files:
            self.print_section(f"Validating {workflow_file.name}")
            
            try:
                with open(workflow_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for common issues
                if 'on:\n\non:' in content or 'on:\n\n\non:' in content:
                    issues_found.append(f"Duplicate 'on:' declarations in {workflow_file.name}")
                    print(f"   ❌ Found duplicate 'on:' declarations")
                
                if '--raw-field' in content and ('=' in content or '[]' in content):
                    if 'required_status_checks' in content or 'restrictions' in content:
                        issues_found.append(f"Incorrect --raw-field usage for complex objects in {workflow_file.name}")
                        print(f"   ❌ Using --raw-field for complex objects (should use --input)")
                
                if 'set -e' in content and 'set +e' not in content:
                    print(f"   ⚠️  Using 'set -e' without error handling")
                
                if '${{ secrets.GH_ADMIN_TOKEN }}' not in content and 'workflow_call' in content:
                    print(f"   ⚠️  Workflow may need GH_ADMIN_TOKEN secret")
                
                print(f"   ✅ Basic validation passed")
                
            except Exception as e:
                issues_found.append(f"Error reading {workflow_file.name}: {e}")
                print(f"   ❌ Error reading file: {e}")
        
        if issues_found:
            self.print_section("Workflow Issues Found")
            for issue in issues_found:
                print(f"   • {issue}")
            return False
        
        print(f"\n✅ All {len(workflow_files)} workflow files validated successfully")
        return True
    
    def cleanup_repository(self):
        """Remove unnecessary files and consolidate structure"""
        self.print_header("🧹 Repository Cleanup & Optimization")
        
        files_to_remove = [
            # Sample application files (not part of automation tool)
            'app.py',
            'index.js',
            'package.json',
            'requirements.txt',
            
            # Redundant documentation and analysis files
            'COPILOT_INSPECTION.md',
            'COPILOT_INSTRUCTION.md',
            'MAIN_AUTOMATION_FIX.md',
            'PAT_SETUP_COMPLETE.md',
            'SETUP_INSTRUCTIONS.md',
            
            # Old diagnostic scripts (replaced by this toolkit)
            'diagnose-automation.py',
            'pat-permissions-analysis.py',
            'enable_security_features.py',
            'security_check.py'
        ]
        
        removed_files = []
        for file in files_to_remove:
            file_path = self.repo_root / file
            if file_path.exists():
                file_path.unlink()
                removed_files.append(file)
                print(f"   🗑️  Removed: {file}")
        
        print(f"\n✅ Cleanup complete! Removed {len(removed_files)} redundant files")
        
        # Move remaining documentation to docs folder
        docs_to_move = [
            'GITHUB_AUTOMATION_GUIDE.md',
            'PAT_PERMISSIONS_ANALYSIS.md'
        ]
        
        docs_dir = self.repo_root / 'docs'
        for doc in docs_to_move:
            src = self.repo_root / doc
            if src.exists():
                dst = docs_dir / doc
                src.rename(dst)
                print(f"   📁 Moved to docs/: {doc}")
        
        return removed_files
        """Remove unnecessary files and consolidate structure"""
        self.print_header("🧹 Repository Cleanup & Optimization")
        
        files_to_remove = [
            # Sample application files (not part of automation tool)
            'app.py',
            'index.js',
            'package.json',
            'requirements.txt',
            
            # Redundant documentation and analysis files
            'COPILOT_INSPECTION.md',
            'COPILOT_INSTRUCTION.md',
            'MAIN_AUTOMATION_FIX.md',
            'PAT_SETUP_COMPLETE.md',
            'SETUP_INSTRUCTIONS.md',
            
            # Old diagnostic scripts (replaced by this toolkit)
            'diagnose-automation.py',
            'pat-permissions-analysis.py',
            'enable_security_features.py',
            'security_check.py'
        ]
        
        removed_files = []
        for file in files_to_remove:
            file_path = self.repo_root / file
            if file_path.exists():
                file_path.unlink()
                removed_files.append(file)
                print(f"   🗑️  Removed: {file}")
        
        print(f"\n✅ Cleanup complete! Removed {len(removed_files)} redundant files")
        
        # Move remaining documentation to docs folder
        docs_to_move = [
            'GITHUB_AUTOMATION_GUIDE.md',
            'PAT_PERMISSIONS_ANALYSIS.md'
        ]
        
        docs_dir = self.repo_root / 'docs'
        for doc in docs_to_move:
            src = self.repo_root / doc
            if src.exists():
                dst = docs_dir / doc
                src.rename(dst)
                print(f"   📁 Moved to docs/: {doc}")
        
        return removed_files

def main():
    """Main function with command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description='GitHub Repository Automation Toolkit')
    parser.add_argument('--diagnose', action='store_true', help='Run environment diagnostics')
    parser.add_argument('--analyze', action='store_true', help='Analyze PAT permissions')
    parser.add_argument('--setup-report', action='store_true', help='Generate setup report')
    parser.add_argument('--cleanup', action='store_true', help='Clean up repository structure')
    parser.add_argument('--validate', action='store_true', help='Validate workflow files')
    parser.add_argument('--detect-server', action='store_true', help='Detect GitHub server type and capabilities')
    parser.add_argument('--all', action='store_true', help='Run all operations')
    
    args = parser.parse_args()
    
    toolkit = GitHubAutomationToolkit()
    
    if args.all or len(sys.argv) == 1:  # Default to all if no args
        # Run complete toolkit
        print("🚀 GitHub Automation Toolkit - Complete Analysis")
        print("=" * 52)
        
        # Display enterprise notice
        print("\n🏢 ENTERPRISE DEPLOYMENT ADVISORY")
        print("═" * 35)
        print("This toolkit provides comprehensive automation capabilities designed for")
        print("enterprise environments. Organizations should carefully evaluate and")
        print("customize all components to align with specific security policies,")
        print("compliance requirements, and operational procedures before deployment.")
        print("Professional pilot testing strongly recommended.")
        print("═" * 70)
        
        # Server type detection
        server_info = toolkit.detect_github_server_type()
        
        # Validation workflows
        toolkit.validate_workflows()
        
        # Diagnose environment
        issues = toolkit.diagnose_environment()
        toolkit.print_solutions(issues)
        
        # Analyze permissions
        toolkit.analyze_permissions()
        
        # Generate report
        toolkit.generate_setup_report()
        
        # Cleanup repository
        toolkit.cleanup_repository()
        
        print(f"\n📊 Toolkit Summary:")
        print(f"   Server Type: {server_info['server_description']}")
        print(f"   Issues found: {len(issues)}")
        print(f"   Status: {'❌ Needs attention' if issues else '✅ Ready to run'}")
        
        return len(issues) == 0
    
    # Individual operations
    if args.detect_server:
        toolkit.detect_github_server_type()
        return True
    
    if args.diagnose:
        issues = toolkit.diagnose_environment()
        toolkit.print_solutions(issues)
        return len(issues) == 0
    
    if args.analyze:
        toolkit.analyze_permissions()
        return True
    
    if args.setup_report:
        toolkit.generate_setup_report()
        return True
    
    if args.cleanup:
        toolkit.cleanup_repository()
        return True
    
    if args.validate:
        return toolkit.validate_workflows()

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
