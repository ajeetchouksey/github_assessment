# GitHub Repository Assessment Usage Instructions

**Instructions Version:** 1.0.0  
**Last Updated:** July 18, 2025  
**Framework Dependencies:** gh-assessment-template.md v1.0.0, gh-assessment-prompt.md v1.0.0  

## Overview

This guide provides step-by-step instructions for using the GitHub assessment framework to evaluate any repository. The framework consists of two main components:

- **`gh-assessment-template.md`** - Comprehensive assessment template with standardized parameters
- **`gh-assessment-prompt.md`** - AI automation prompt for generating assessments

**Recommended Execution Platforms:**

- **GitHub Copilot in VS Code** (Primary recommendation)
- **GitHub Copilot in GitHub UI** (Web-based alternative)
- **External AI with VS Code context** (Fallback option)

---

## Quick Start Guide

### Prerequisites

**Platform Requirements:**
1. **VS Code** with GitHub Copilot extension (recommended)
   - OR **GitHub.com** with Copilot Chat access
2. **GitHub repository access** (local clone or web access)
3. **Assessment framework files** in your repository:
   - `gh-assessment-template.md`
   - `gh-assessment-prompt.md`

**Account Requirements:**
- GitHub Copilot subscription (individual or organization)
- Repository access permissions (read minimum, write for saving reports)

### Basic Assessment Workflow

1. **Open repository** in VS Code or GitHub.com
2. **Launch GitHub Copilot Chat**
3. **Upload assessment files** (template and prompt)
4. **Execute assessment** using provided prompts
5. **Review and save report** with proper versioning (e.g., `gh-assessment-report-v1.0.0.md`)

---

## Detailed Usage Instructions

### Step 1: Repository Preparation

Before starting the assessment, ensure you have:

- [ ] **Repository access** - Clone or browse the target repository
- [ ] **Repository context** - Understand the repository's purpose and type
- [ ] **Assessment scope** - Decide if this is initial, follow-up, or compliance assessment

### Step 2: AI Assistant Setup

#### Option A: GitHub Copilot Chat in VS Code (Recommended)

1. **Open VS Code** with the repository you want to assess
2. **Open GitHub Copilot Chat** (Ctrl+Shift+I or Cmd+Shift+I)
3. **Upload assessment files** using the attachment feature:
   - Attach `gh-assessment-template.md`
   - Attach `gh-assessment-prompt.md`
4. **Reference the current repository** - Copilot automatically has access to your workspace

#### Option B: GitHub Copilot Chat in GitHub UI

1. **Navigate to the repository** on GitHub.com
2. **Open GitHub Copilot Chat** (if available in your organization)
3. **Reference the repository** directly in your prompt
4. **Provide assessment context** through the chat interface

#### Option C: VS Code with Claude (Alternative)

1. **Install Claude extension** in VS Code (if available)
2. **Open the repository** in VS Code workspace
3. **Upload assessment files** to Claude extension
4. **Reference workspace context** in your assessment request

### Step 3: Repository Context Provision

Provide AI assistant with repository information using these methods based on your chosen platform:

#### Method A: VS Code GitHub Copilot (Recommended)

**Advantages:** Direct workspace access, file context, integrated development environment

**Setup Process:**

1. **Open repository in VS Code**
2. **Open GitHub Copilot Chat** (Ctrl+Shift+I or Cmd+Shift+I)
3. **Attach assessment files** using the paperclip icon:
   - `gh-assessment-template.md`
   - `gh-assessment-prompt.md`
4. **Use this prompt:**

```text
I need to assess this GitHub repository using the attached assessment template and prompt. Please analyze the current workspace and generate a comprehensive GitHub assessment report.

Repository Context:
- Current workspace: [automatically detected by Copilot]
- Repository type: [detected from naming pattern]
- Technology stack: [detected from files]

Please follow the instructions in gh-assessment-prompt.md to generate a complete assessment using gh-assessment-template.md.
```

#### Method B: GitHub UI Copilot Chat

**Advantages:** Direct GitHub integration, repository visibility, web-based access

**Setup Process:**
1. **Navigate to repository** on GitHub.com
2. **Open GitHub Copilot Chat** (if available)
3. **Reference the current repository** directly
4. **Use this prompt:**

```text
Please assess this GitHub repository: [current repository URL will be auto-detected]

I need a comprehensive assessment using the GitHub assessment framework. Please:
1. Analyze the repository structure and configuration
2. Evaluate security settings and workflows
3. Assess code quality and documentation
4. Generate a complete assessment report

Focus on GitHub-native features and provide specific, actionable recommendations.
```

#### Method C: VS Code with External AI (Fallback)

**For cases where GitHub Copilot is not available:**

1. **Open repository in VS Code**
2. **Copy repository structure** using VS Code file explorer
3. **Export key files** (README, workflows, configuration files)
4. **Use external AI tool** with this context:

```text
Please assess this repository based on the following information:

Repository: [name from VS Code workspace]
Structure: [paste from VS Code file explorer]
Key Files: [attach or paste content of main files]
Technology Stack: [describe based on file extensions and dependencies]

Use the attached gh-assessment-template.md and gh-assessment-prompt.md to generate a comprehensive assessment report.
```

### Step 4: Assessment Execution

Choose the execution method based on your platform:

#### VS Code GitHub Copilot Assessment

**Standard Assessment Request:**

```text
Please conduct a comprehensive GitHub repository assessment of this workspace using the attached template and prompt files. 

Assessment Requirements:
1. Analyze the current repository structure and organization
2. Evaluate GitHub-specific security configurations and workflows
3. Assess code quality, documentation, and collaboration features
4. Generate a complete assessment report with version v1.0.0
5. Provide specific findings with evidence from the workspace
6. Include actionable recommendations prioritized by severity

Please follow the gh-assessment-prompt.md instructions and use the gh-assessment-template.md structure for the final report.
```

**Technology-Specific Assessment (Auto-Detection):**

```text
I can see this is a [Terraform/Node.js/Python/etc.] repository based on the workspace files. Please:

1. Apply the technology-specific parameters from the assessment prompt
2. Focus on [technology]-specific best practices and security
3. Evaluate [technology]-specific workflows and automation
4. Include relevant tooling and dependency management assessment

Generate a comprehensive assessment with technology-specific enhancements automatically detected from the workspace.
```

#### GitHub UI Copilot Assessment

**Repository Analysis Request:**

```text
Please analyze this GitHub repository for comprehensive assessment. Focus on:

1. Repository configuration and settings
2. Branch protection and security features
3. GitHub Actions workflows and automation
4. Issue/PR templates and collaboration tools
5. Documentation and project management

Provide specific findings with evidence and actionable recommendations. Generate assessment report with proper versioning (v1.0.0 for initial assessment).
```

#### VS Code Manual Process (Fallback)

**When GitHub Copilot is not available:**

1. **Gather repository information** using VS Code:
   - Copy file structure from Explorer
   - Export key configuration files
   - Document workflows and automation setup
   
2. **Use external AI tool** with collected context:
   - Upload or paste repository structure
   - Attach key files (README, workflows, config)
   - Reference the assessment template and prompt

3. **Generate assessment** using external AI with repository context

### Step 5: Review and Customization

After Claude generates the initial assessment:

1. **Review all findings** for accuracy and completeness
2. **Verify compliance ratings** match actual repository state
3. **Check recommendation relevance** to your organization
4. **Validate version consistency** between filename and document content
5. **Customize parameters** if needed for your specific requirements

#### Common Customizations

**Severity Adjustments:**
```
Please adjust the severity of [parameter name] from [current] to [desired] because [reason].
```

**Additional Parameters:**
```
Please add assessment parameters for [specific technology/requirement] in the [section name] section.
```

**Organizational Standards:**
```
Please evaluate against our organization's specific requirements for [area] which include [requirements].
```

### Step 6: Final Report Generation

Request the final report with proper formatting:

```
Please generate the final assessment report with:

1. **Version-tagged filename**: gh-assessment-report-v1.0.0.md
2. **Consistent versioning**: Ensure filename version matches document header
3. **Complete findings**: All placeholders replaced with actual data
4. **Proper formatting**: Maintain template structure and markdown formatting
5. **Actionable recommendations**: Specific, prioritized improvement suggestions

**Critical**: Verify that the version in the filename exactly matches the version in the document header and executive summary.
```

---

## Advanced Usage Scenarios

### Scenario 1: Compliance Assessment for Multiple Repositories

**Use Case:** Assessing multiple repositories for organizational compliance

**Process:**
1. **Create assessment baseline** using the first repository
2. **Standardize parameters** based on organizational requirements
3. **Batch assess** similar repositories using the same criteria
4. **Compare results** across repositories for consistency

**Claude Prompt:**
```
I need to assess multiple repositories for compliance. Please:

1. Use this repository as a baseline for [repository type]
2. Generate a standardized assessment approach
3. Create reusable assessment criteria for similar repositories
4. Highlight areas for organizational standardization

Focus on consistency and comparative analysis across repositories.
```

### Scenario 2: Progressive Assessment (Follow-up)

**Use Case:** Re-assessing a repository after implementing recommendations

**Process:**
1. **Reference previous assessment** version and findings
2. **Focus on improvement areas** from previous recommendations
3. **Track progress** against previous compliance ratings
4. **Update version** appropriately (minor/major based on changes)

**Claude Prompt:**
```
This is a follow-up assessment. Previous version: v1.2.0

Previous key issues:
- [issue 1]
- [issue 2]
- [issue 3]

Please:
1. Assess current state against previous findings
2. Track improvement progress
3. Identify remaining issues
4. Generate v1.3.0 report focusing on changes
5. Compare compliance ratings with previous assessment
```

### Scenario 3: Pre-Deployment Assessment

**Use Case:** Assessing repository readiness before production deployment

**Process:**
1. **Focus on critical parameters** for production readiness
2. **Emphasize security** and reliability aspects
3. **Validate deployment workflows** and automation
4. **Check compliance** with production standards

**Claude Prompt:**
```
This is a pre-deployment assessment for production readiness. Please:

1. Emphasize Critical and Major severity items
2. Focus on security, reliability, and operational aspects
3. Validate deployment automation and workflows
4. Check compliance with production standards
5. Provide go/no-go recommendation based on findings

Critical areas for production readiness:
- Security configurations
- Branch protection and access controls
- Automated testing and validation
- Monitoring and alerting setup
- Incident response procedures
```

### Scenario 4: Technology Migration Assessment

**Use Case:** Assessing repository during technology stack migration

**Process:**
1. **Assess current state** with existing technology parameters
2. **Identify migration gaps** and requirements
3. **Evaluate migration readiness** and blockers
4. **Plan assessment updates** for post-migration

**Claude Prompt:**
```
This repository is undergoing migration from [old technology] to [new technology]. Please:

1. Assess current state using [old technology] parameters
2. Identify gaps for [new technology] adoption
3. Evaluate migration readiness and blockers
4. Suggest assessment parameter updates for post-migration
5. Create migration-specific recommendations

Migration context:
- Current: [describe current setup]
- Target: [describe target setup]
- Timeline: [migration timeline]
```

---

## Best Practices and Tips

### Working with GitHub Copilot and VS Code

**Optimal Prompting in VS Code:**
- **Leverage workspace context** - Copilot automatically understands your repository structure
- **Use specific file references** - Mention specific files by name for targeted analysis
- **Attach template files** - Use the paperclip icon to upload assessment template and prompt
- **Request iterative analysis** - Ask for section-by-section review for complex repositories

**GitHub UI Copilot Best Practices:**
- **Reference repository directly** - Copilot has access to the current repository context
- **Focus on GitHub features** - Emphasize repository settings, workflows, and security features
- **Use repository navigation** - Switch between files/folders during conversation for context
- **Leverage GitHub integration** - Reference issues, PRs, and repository insights

**VS Code Integration Tips:**
- **Use Copilot Chat sidebar** - Keep assessment conversation persistent while working
- **Reference open files** - Open relevant files in editor tabs for Copilot to analyze
- **Utilize workspace features** - Search, file explorer, and terminal integration
- **Save assessment directly** - Generate report files directly in VS Code workspace

**Quality Assurance in Both Platforms:**
- **Cross-reference findings** with actual repository state using platform navigation
- **Verify recommendations** against available GitHub features and VS Code extensions
- **Use integrated tools** for validation (GitHub security tab, VS Code problems panel)
- **Export results** directly to repository documentation folder

### Assessment Quality Guidelines

**Before Starting:**
- [ ] Clear understanding of repository purpose and type
- [ ] Access to complete repository content
- [ ] Defined assessment scope and objectives
- [ ] Organizational standards and requirements identified

**During Assessment:**
- [ ] Verify all findings against actual repository state
- [ ] Ensure recommendations are specific and actionable
- [ ] Check compliance calculations for accuracy
- [ ] Validate technology-specific parameter additions

**After Assessment:**
- [ ] Review final report for completeness and accuracy
- [ ] Verify version consistency across filename and content
- [ ] Ensure recommendations align with organizational priorities
- [ ] Save assessment with proper version control

### Common Pitfalls to Avoid

**Version Management Issues:**
- ❌ Mismatched versions between filename and document content
- ❌ Incorrect semantic versioning progression
- ❌ Missing version references in executive summary

**Assessment Quality Issues:**
- ❌ Generic recommendations not specific to the repository
- ❌ Compliance ratings not based on actual evaluation
- ❌ Missing technology-specific parameters for detected stack
- ❌ Incomplete replacement of template placeholders

**Organizational Alignment Issues:**
- ❌ Assessment criteria not aligned with organizational standards
- ❌ Missing consideration of repository type requirements
- ❌ Recommendations conflicting with existing policies

---

## Troubleshooting

### Common Issues and Solutions

**Issue: Claude generates generic assessments**
- **Solution:** Provide more specific repository context and upload key files
- **Prevention:** Include detailed technology stack and organizational requirements

**Issue: Compliance ratings seem inaccurate**
- **Solution:** Ask Claude to recalculate based on specific parameter evaluation
- **Prevention:** Explicitly request validation of calculations

**Issue: Missing technology-specific parameters**
- **Solution:** Explicitly request addition of parameters for detected technologies
- **Prevention:** Specify technology stack clearly in initial prompt

**Issue: Recommendations are not actionable**
- **Solution:** Ask for more specific, implementable recommendations
- **Prevention:** Provide context about current capabilities and constraints

**Issue: Version inconsistencies**
- **Solution:** Explicitly request version consistency check and correction
- **Prevention:** Always specify version requirements in final report request

### Getting Better Results

**Enhance Repository Context:**
```
Additional context for better assessment:
- Repository age: [new/mature/legacy]
- Team size: [small/medium/large]
- Deployment frequency: [daily/weekly/monthly]
- Compliance requirements: [SOC2/ISO27001/etc.]
- Technology constraints: [existing tools/limitations]
```

**Request Specific Focus:**
```
Please focus specifically on:
1. [area 1] - because [reason]
2. [area 2] - due to [organizational requirement]
3. [area 3] - for [compliance/security/quality] purposes
```

**Validate and Refine:**
```
Please review and validate:
1. All compliance percentages are based on actual parameter counts
2. All recommendations are specific to this repository
3. All examples reference actual repository content
4. Version consistency across filename and document content
```

---

## Assessment Templates for Common Scenarios

### Template 1: New Repository Initial Assessment
```
Subject: Initial GitHub Repository Assessment

Repository: [name]
Type: [Module/Component/Solution/Application/Library]
Technology: [primary stack]
Purpose: [brief description]

Please conduct an initial comprehensive assessment using gh-assessment-template.md and gh-assessment-prompt.md.

Generate: gh-assessment-report-v1.0.0.md

Focus areas:
- Basic structure and configuration compliance
- Security baseline establishment
- GitHub feature utilization
- Development workflow setup

Deliverable: Complete assessment with baseline recommendations for new repository.
```

### Template 2: Security-Focused Assessment
```
Subject: Security-Focused Repository Assessment

Repository: [name]
Assessment Type: Security Review
Previous Version: [if applicable]

Please conduct a security-focused assessment emphasizing:
- Branch protection and access controls
- Secret management and scanning
- Workflow security and permissions
- Dependency vulnerability management
- Code scanning and security automation

Generate: gh-assessment-report-v[x.y.z].md

Prioritize Critical and Major security findings with immediate action recommendations.
```

### Template 3: Compliance Audit Assessment
```
Subject: Compliance Audit Repository Assessment

Repository: [name]
Compliance Framework: [SOC2/ISO27001/etc.]
Audit Scope: [specific requirements]

Please conduct a compliance-focused assessment evaluating:
- Documentation and governance requirements
- Access control and audit logging
- Change management processes
- Security control implementation
- Incident response capabilities

Generate: gh-assessment-report-v[x.y.z].md

Include compliance evidence and gap analysis with remediation timeline.
```

### Template 4: Migration Readiness Assessment
```
Subject: Migration Readiness Assessment

Repository: [name]
Migration: From [current] to [target]
Timeline: [migration schedule]

Please assess migration readiness focusing on:
- Current state documentation
- Migration blocker identification
- Target state gap analysis
- Migration risk assessment
- Post-migration assessment planning

Generate: gh-assessment-report-v[x.y.z].md

Include migration-specific recommendations and readiness checklist.
```

---

## Contact and Support

**Framework Version:** 1.0.0  
**Instructions Version:** 1.0.0  
**Last Updated:** July 18, 2025  
**Maintained by:** DevOps Engineering Team  

**For questions or support regarding this assessment framework:**
- **Email:** [Contact information to be provided]
- **Documentation:** [Link to internal documentation]
- **Updates:** Check this repository for framework updates and improvements

**Recommended Execution Platforms:**
- **GitHub Copilot in VS Code** (Primary - integrated workspace experience)
- **GitHub Copilot in GitHub UI** (Secondary - web-based repository analysis)
- **External AI with VS Code context** (Fallback - when Copilot unavailable)

**Platform Compatibility:**

- VS Code with GitHub Copilot extension
- GitHub.com with Copilot Chat feature
- GitHub Free, Pro, Team, Enterprise (with Copilot subscription)

**Framework Dependencies:**

- `gh-assessment-template.md` v1.0.0
- `gh-assessment-prompt.md` v1.0.0

---

**Note:** This framework is designed to be technology-agnostic and can be adapted for various repository types and organizational requirements. Regular updates ensure alignment with GitHub feature evolution and industry best practices.
