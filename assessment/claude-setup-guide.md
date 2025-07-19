# Claude Sonnet Assessment Setup Guide

## Overview

This guide explains how to configure GitHub Actions to use Claude Sonnet for automated repository assessments. The workflow leverages Claude's advanced analysis capabilities to generate comprehensive repository assessments.

## Prerequisites

### 1. Anthropic API Access
- **Claude API Key**: You need access to Claude via Anthropic's API
- **Recommended Model**: Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)
- **API Limits**: Ensure adequate token limits for repository analysis

### 2. GitHub Repository Setup
- **Repository Access**: Admin access to configure secrets and workflows
- **Assessment Framework**: The repository must contain:
  - `docs/gh-assessment-template.md`
  - `docs/gh-assessment-prompt.md`
  - `docs/usage-instructions.md`

### 3. GitHub Actions Permissions
- **Contents**: Read (to analyze repository)
- **Issues**: Write (to create assessment issues)
- **Pull Requests**: Write (for assessment PRs)
- **Security Events**: Read (for security analysis)

## Setup Instructions

### Step 1: Configure Claude API Secret

1. **Obtain Claude API Key**:
   - Visit [Anthropic Console](https://console.anthropic.com/)
   - Create or access your account
   - Generate an API key with sufficient credits

2. **Add GitHub Secret**:
   ```
   Repository Settings → Secrets and variables → Actions → New repository secret
   
   Name: ANTHROPIC_API_KEY
   Value: [Your Claude API key]
   ```

### Step 2: Deploy Workflow File

1. **Create Workflow Directory**:
   ```
   .github/workflows/
   ```

2. **Add Workflow File**:
   - Copy `claude-assessment.yml` to `.github/workflows/`
   - Commit and push to your repository

### Step 3: Configure Workflow Permissions

1. **Repository Settings → Actions → General**
2. **Workflow permissions**:
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

### Step 4: Test the Setup

1. **Manual Trigger**:
   ```
   Actions → Claude Sonnet Repository Assessment → Run workflow
   ```

2. **Choose Parameters**:
   - **Assessment Type**: comprehensive
   - **Output Version**: 1.0.0
   - **Claude Model**: claude-3-5-sonnet-20241022

3. **Monitor Execution**:
   - Check workflow logs for successful completion
   - Verify assessment report generation
   - Confirm issue creation

## Configuration Options

### Claude Models Available

1. **Claude 3.5 Sonnet** (Recommended)
   - **Model ID**: `claude-3-5-sonnet-20241022`
   - **Strengths**: Excellent analysis, balanced performance
   - **Use Case**: Comprehensive assessments

2. **Claude 3 Sonnet**
   - **Model ID**: `claude-3-sonnet-20240229`
   - **Strengths**: Strong reasoning, detailed analysis
   - **Use Case**: In-depth technical assessments

3. **Claude 3 Haiku**
   - **Model ID**: `claude-3-haiku-20240307`
   - **Strengths**: Fast, cost-effective
   - **Use Case**: Quick assessments, frequent monitoring

### Assessment Types

1. **Comprehensive** (Default)
   - Full repository analysis
   - All assessment categories
   - Complete recommendations

2. **Security-Focused**
   - Emphasis on security findings
   - Branch protection analysis
   - Vulnerability assessment

3. **Compliance-Audit**
   - Regulatory compliance focus
   - Documentation requirements
   - Audit trail evaluation

4. **Migration-Readiness**
   - Technology migration assessment
   - Compatibility analysis
   - Migration planning

### Scheduling Options

**Current Schedule**: Weekly on Mondays at 9 AM UTC

**Customize Schedule**:
```yaml
schedule:
  - cron: '0 9 * * 1'  # Weekly Monday 9 AM
  - cron: '0 18 * * 5' # Weekly Friday 6 PM
  - cron: '0 12 1 * *' # Monthly 1st day at noon
```

**Trigger Conditions**:
```yaml
push:
  branches: [main, master]
  paths:
    - '.github/workflows/**'
    - 'security/**'
    - '*.tf'  # Terraform files
    - '*.py'  # Python files
    - 'Dockerfile'
```

## Usage Scenarios

### Scenario 1: Regular Monitoring

**Purpose**: Continuous repository health monitoring

**Configuration**:
- **Schedule**: Weekly assessments
- **Type**: Comprehensive
- **Model**: Claude 3.5 Sonnet
- **Automation**: Full automation with issue creation

**Benefits**:
- Early detection of issues
- Trend analysis over time
- Automated compliance monitoring

### Scenario 2: Security-First Assessments

**Purpose**: Security-focused repository evaluation

**Configuration**:
- **Trigger**: Security file changes
- **Type**: Security-focused
- **Model**: Claude 3.5 Sonnet
- **Priority**: Critical/Major findings only

**Benefits**:
- Immediate security feedback
- Compliance verification
- Risk mitigation

### Scenario 3: Pre-Deployment Checks

**Purpose**: Validate repository before major deployments

**Configuration**:
- **Trigger**: Manual before releases
- **Type**: Comprehensive
- **Model**: Claude 3.5 Sonnet
- **Output**: Detailed deployment readiness report

**Benefits**:
- Deployment risk assessment
- Quality gate validation
- Stakeholder confidence

### Scenario 4: Cost-Effective Monitoring

**Purpose**: Frequent monitoring with budget constraints

**Configuration**:
- **Schedule**: Daily quick checks
- **Type**: Comprehensive
- **Model**: Claude 3 Haiku
- **Focus**: Critical issues only

**Benefits**:
- Low-cost monitoring
- Fast feedback loops
- Budget-friendly automation

## Advanced Configuration

### Custom Prompts for Specific Technologies

**Terraform-Focused Assessment**:
```yaml
env:
  ASSESSMENT_FOCUS: "terraform"
  TECH_SPECIFIC_PARAMS: |
    - Azure resource best practices
    - Terraform state management
    - Infrastructure security
    - Resource naming conventions
```

**Python Application Assessment**:
```yaml
env:
  ASSESSMENT_FOCUS: "python"
  TECH_SPECIFIC_PARAMS: |
    - Dependency management
    - Code quality standards
    - Testing coverage
    - Security scanning
```

### Multi-Repository Assessment

**Organization-wide Workflow**:
```yaml
strategy:
  matrix:
    repository: 
      - repo1
      - repo2
      - repo3
    assessment_type:
      - comprehensive
      - security-focused
```

### Integration with Existing Tools

**Combine with Security Scanning**:
```yaml
- name: Run Security Scan
  uses: github/super-linter@v4
  
- name: Run Claude Assessment
  # Include security scan results in context
```

**Slack Notifications**:
```yaml
- name: Notify Slack
  if: steps.claude-assessment.outputs.critical_count > 0
  uses: 8398a7/action-slack@v3
  with:
    status: 'Critical issues found in assessment'
```

## Troubleshooting

### Common Issues

**1. API Key Issues**
```
Error: Invalid API key or insufficient credits
```
**Solution**:
- Verify `ANTHROPIC_API_KEY` secret is correct
- Check Anthropic account credits and limits
- Ensure API key has necessary permissions

**2. Assessment Framework Missing**
```
Error: gh-assessment-template.md not found
```
**Solution**:
- Ensure framework files exist in `docs/` folder
- Verify file names match exactly
- Check file paths in workflow configuration

**3. Permission Errors**
```
Error: Resource not accessible by integration
```
**Solution**:
- Enable workflow write permissions
- Check repository settings for Actions permissions
- Verify secret access in repository settings

**4. Claude Model Errors**
```
Error: Model not found or unavailable
```
**Solution**:
- Use supported model IDs
- Check Anthropic API status
- Verify model availability in your region

### Debug Mode

**Enable Detailed Logging**:
```yaml
env:
  RUNNER_DEBUG: 1
  ACTIONS_STEP_DEBUG: true
```

**Validate Inputs**:
```yaml
- name: Debug Information
  run: |
    echo "Model: ${{ env.CLAUDE_MODEL }}"
    echo "Assessment Type: ${{ env.ASSESSMENT_TYPE }}"
    echo "Repository: ${{ github.repository }}"
    echo "Trigger: ${{ github.event_name }}"
```

### Performance Optimization

**Reduce Analysis Scope**:
```yaml
# Limit file analysis for large repositories
- name: Generate Repository Context
  run: |
    find . -name "*.tf" -o -name "*.py" -o -name "*.js" | head -50
```

**Parallel Processing**:
```yaml
strategy:
  matrix:
    assessment_section: [security, quality, documentation]
```

**Caching Dependencies**:
```yaml
- name: Cache Python Dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

## Cost Management

### Token Usage Estimation

**Repository Size Impact**:
- Small Repository (< 100 files): ~2,000-5,000 tokens
- Medium Repository (100-500 files): ~5,000-15,000 tokens  
- Large Repository (500+ files): ~15,000-50,000 tokens

**Model Cost Comparison** (Approximate):
- Claude 3.5 Sonnet: $3-15 per assessment
- Claude 3 Sonnet: $3-15 per assessment
- Claude 3 Haiku: $0.25-1.25 per assessment

### Cost Optimization Strategies

**1. Smart Scheduling**:
- Weekly full assessments
- Daily security-only checks with Haiku
- Event-triggered assessments for critical changes

**2. Context Filtering**:
- Focus on modified files for push triggers
- Exclude non-essential files from analysis
- Use targeted assessment types

**3. Batch Processing**:
- Combine multiple small repositories
- Process similar repositories together
- Use matrix strategies efficiently

## Security Considerations

### API Key Protection

**Best Practices**:
- Use GitHub repository secrets (never commit keys)
- Rotate API keys regularly
- Monitor API key usage and access logs
- Restrict API key permissions if possible

### Workflow Security

**Access Controls**:
- Limit workflow execution to authorized users
- Review workflow changes in pull requests
- Monitor workflow execution logs
- Use branch protection for workflow files

### Data Privacy

**Repository Content**:
- Assessment data is sent to Anthropic Claude API
- Consider data sensitivity in repository context
- Review Anthropic's data usage policies
- Implement data filtering for sensitive content

## Support and Maintenance

### Regular Updates

**Monthly Tasks**:
- [ ] Review Claude model performance and costs
- [ ] Update assessment framework files if needed
- [ ] Check for new Claude model versions
- [ ] Analyze assessment report quality and accuracy

**Quarterly Tasks**:
- [ ] Review and optimize workflow configuration
- [ ] Update assessment parameters for organizational changes
- [ ] Evaluate cost vs. value analysis
- [ ] Train team on assessment interpretation

### Monitoring and Alerting

**Key Metrics to Track**:
- Assessment completion rate
- Claude API response times
- Cost per assessment
- Critical findings detection rate

**Alert Conditions**:
- Assessment failures
- High critical finding counts
- API cost spikes
- Model performance degradation

---

## Contact Information

**For Technical Support**:
- **Workflow Issues**: Repository administrators
- **Claude API Issues**: Anthropic support
- **Assessment Framework**: DevOps engineering team

**For Assessment Interpretation**:
- **Security Findings**: Information security team
- **Compliance Issues**: Compliance team
- **Technical Recommendations**: Engineering team leads

---

**Last Updated**: July 18, 2025  
**Framework Version**: 1.0.0  
**Workflow Version**: 1.0.0
