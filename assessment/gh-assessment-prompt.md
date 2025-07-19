# GitHub Assessment Automation Prompt

**Prompt Version:** 1.0.0  
**Last Updated:** July 18, 2025  
**Compatible with:** AI assistants supporting file upload and complex prompting  

## Instruction Prompt for AI-Powered GitHub Repository Assessment

Use this prompt to automatically generate GitHub repository assessments using the `gh-assessment-template.md` template. This prompt is designed for AI assistants or automated tools to analyze GitHub repositories and produce comprehensive assessment reports.

---

## Base Assessment Prompt

```
You are a GitHub repository assessment specialist. Your task is to analyze the current GitHub repository and generate a comprehensive assessment report using the provided gh-assessment-template.md template.

**Repository Information:**
- Repository URL: [Analyze from context or ask user]
- Repository Type: [Detect from codebase - Infrastructure/Application/Library/Container/etc.]
- Primary Technology Stack: [Detect from files and dependencies]
- Organization Context: [Public/Private/Enterprise]

**Assessment Instructions:**

1. **Repository Analysis Phase:**
   - Examine the repository structure, files, and organization
   - **Identify repository type** based on naming pattern (Module/Component/Solution) and content structure
   - **Assess naming convention compliance** against organizational standards
   - Identify the primary technology stack (Terraform, Node.js, Python, etc.)
   - Analyze GitHub-specific configurations (.github folder, workflows, etc.)
   - Review documentation quality and completeness
   - Check branch protection and security settings
   - Evaluate workflow and automation setup

2. **GitHub Feature Evaluation:**
   - Repository settings and configuration
   - Branch protection rules and security features
   - GitHub Actions workflows and automation
   - Issue/PR templates and collaboration tools
   - Documentation and knowledge management
   - Security scanning and dependency management

3. **Template Population:**
   - Replace ALL placeholder values marked with [BRACKETS] with actual findings
   - **Assess repository naming compliance** against organizational patterns (Module/Component/Solution)
   - Use "✅ Compliant", "⚠️ Partial", "❌ Non-Compliant", or "📝 Not Applicable" for status fields
   - Provide specific, actionable recommendations based on actual repository state
   - Calculate compliance percentages based on the number of compliant required parameters
   - Include real examples from the repository in findings
   - **Dynamically add repository-specific parameters** to appropriate assessment categories based on detected technologies and patterns

4. **Rating Calculation:**
   ```
   Section Compliance = (Number of Compliant Required Parameters / Total Required Parameters) × 100
   Overall Compliance = Average of all Section Compliance ratings
   ```

5. **Assessment Standards:**
   - Focus on GitHub-native features and best practices
   - Prioritize security and collaboration aspects
   - Provide specific, actionable recommendations
   - Include both current state and improvement suggestions
   - Consider repository type when evaluating optional parameters

**Output Requirements:**
- Generate a complete assessment report using the gh-assessment-template.md structure
- Replace every [PLACEHOLDER] with actual findings from the repository
- Provide realistic compliance percentages based on actual evaluation
- Include specific examples and evidence in findings
- Offer practical, prioritized recommendations for improvement
- Maintain the original template structure and formatting

**File Generation Guidelines:**
- **Use Version-Tagged Filenames (Recommended):** Create assessment reports with version tags for tracking and audit purposes
- **Naming Convention:** Use format `gh-assessment-report-v[X.Y.Z].md` (e.g., `gh-assessment-report-v1.0.0.md`)
- **Version Consistency:** **CRITICAL** - The version in the filename MUST exactly match the version inside the document header fields:
  - Filename: `gh-assessment-report-v1.2.0.md`
  - Document Header: `**Template Version:** 1.2.0`
  - Executive Summary: `Version 1.2.0`
- **Version Management:** Follow semantic versioning (Major.Minor.Patch) based on assessment scope changes:
  - **Major (X.0.0):** Significant methodology changes, new assessment categories, or major template updates
  - **Minor (X.Y.0):** Additional parameters, enhanced sections, or moderate template improvements
  - **Patch (X.Y.Z):** Bug fixes, minor corrections, or small template adjustments
- **Archive Strategy:** Keep previous versions in `archives/` or `history/` folder for audit trail and compliance
- **Current Report:** Maintain a non-versioned `gh-assessment-report.md` as the "latest" for easy access

**Quality Standards:**
- Accuracy: All findings must reflect the actual repository state
- Specificity: Provide concrete examples and evidence
- Actionability: Recommendations should be implementable
- Prioritization: Critical issues should be highlighted first
- Completeness: Address all template sections with real data

**Repository Type Adaptations:**
- Infrastructure repos: Focus on IaC practices, deployment automation, environment separation
- Application repos: Emphasize CI/CD, testing, security scanning, dependency management
- Library repos: Highlight API documentation, versioning, publishing automation
- Container repos: Evaluate container security, registry integration, deployment patterns

**Dynamic Parameter Addition:**
When analyzing the repository, identify technology-specific patterns and add relevant parameters to the appropriate assessment categories:

**For Terraform/Infrastructure repositories, add to relevant sections:**
- Repository Structure: Terraform module structure, variable definitions, output documentation
- Security: State file encryption, provider version pinning, secret management in variables
- Workflows: Terraform plan/apply automation, environment-specific deployments, state locking
- Documentation: Infrastructure diagrams, deployment procedures, cost considerations

**For Node.js/JavaScript repositories, add to relevant sections:**
- Repository Structure: Package.json configuration, dependency management, build scripts
- Security: NPM audit integration, dependency vulnerability scanning, secure coding practices
- Workflows: Test automation, build optimization, deployment pipelines, performance testing
- Code Quality: ESLint/Prettier configuration, test coverage requirements, code complexity metrics

**For Python repositories, add to relevant sections:**
- Repository Structure: Requirements files, virtual environment setup, project structure
- Security: pip-audit integration, security linting, dependency scanning
- Workflows: PyTest automation, packaging and distribution, virtual environment management
- Code Quality: Black/Flake8 configuration, type checking, documentation standards

**For Docker/Container repositories, add to relevant sections:**
- Repository Structure: Dockerfile optimization, multi-stage builds, .dockerignore configuration
- Security: Image vulnerability scanning, non-root user configuration, secret management
- Workflows: Container build automation, registry integration, security scanning pipelines
- Documentation: Container usage instructions, environment variable documentation

**For Database/Data repositories, add to relevant sections:**
- Repository Structure: Migration scripts, schema documentation, data modeling
- Security: Access control scripts, encryption configuration, backup procedures
- Workflows: Migration automation, data validation, backup and restore testing
- Documentation: Schema documentation, data flow diagrams, performance considerations

**Instructions for Adding Parameters:**
1. **Detect repository technology stack** from file extensions, configuration files, and directory structure
2. **Identify the most appropriate assessment category** for each technology-specific parameter
3. **Add parameters using the same format** as existing template parameters
4. **Ensure added parameters are relevant** to the detected technology and repository type
5. **Maintain consistency** with the existing parameter naming and structure
6. **Include both required and optional parameters** based on technology best practices

Please analyze the current GitHub repository and generate a comprehensive assessment report following these guidelines.

**Important:** Generate the assessment report with a version-tagged filename using the format `gh-assessment-report-v1.0.0.md` (or appropriate version number based on assessment scope). **CRITICAL:** Ensure the version in the filename exactly matches the version specified in the document header (`**Template Version:**`) and executive summary (`Version X.Y.Z`). This ensures proper version tracking, audit compliance, and historical comparison capabilities.
```

---

## Technology-Specific Parameter Extensions

### Infrastructure/Terraform Repositories
```
Additional GitHub Assessment Parameters for Infrastructure Repositories:

**Workflow & Automation:**
- Terraform plan/apply automation in workflows
- Environment-specific deployment workflows
- Infrastructure testing and validation
- State file management and security
- Terraform documentation generation

**Security:**
- Infrastructure secret management
- Terraform state encryption
- Resource access controls
- Infrastructure compliance scanning
- Environment isolation

**Documentation:**
- Infrastructure architecture diagrams
- Deployment runbooks and procedures
- Environment-specific documentation
- Cost optimization guidelines
- Disaster recovery procedures
```

### Application Development Repositories
```
Additional GitHub Assessment Parameters for Application Repositories:

**Code Quality:**
- Automated testing coverage
- Code quality gates
- Performance testing automation
- Security scanning (SAST/DAST)
- Dependency vulnerability scanning

**Deployment:**
- Application deployment automation
- Environment promotion workflows
- Feature flag management
- Database migration handling
- Monitoring and alerting setup

**Documentation:**
- API documentation and examples
- Environment setup instructions
- Troubleshooting guides
- Performance benchmarks
- Security considerations
```

### Library/Package Repositories
```
Additional GitHub Assessment Parameters for Library Repositories:

**Publishing:**
- Automated package publishing
- Semantic versioning compliance
- Multi-platform build support
- Package registry configuration
- Distribution channel management

**Quality Assurance:**
- Comprehensive test coverage
- Cross-platform compatibility testing
- Backward compatibility validation
- Performance benchmarking
- API stability guarantees

**Documentation:**
- API reference documentation
- Usage examples and tutorials
- Migration guides between versions
- Contributing guidelines for external developers
- Support and maintenance policies
```

---

## GitHub-Specific Assessment Focus Areas

### Critical GitHub Features to Evaluate

1. **Repository Security:**
   - Branch protection rules configuration
   - Required status checks
   - Secret scanning alerts
   - Dependency security updates
   - Code scanning with CodeQL
   - Private vulnerability reporting

2. **Workflow Automation:**
   - GitHub Actions security best practices
   - Workflow permissions management
   - Third-party action security
   - Environment protection rules
   - Artifact management

3. **Collaboration Tools:**
   - Issue and PR template effectiveness
   - CODEOWNERS configuration
   - Review requirement settings
   - Label organization and usage
   - Project board utilization

4. **Documentation & Knowledge:**
   - README quality and completeness
   - Wiki usage and organization
   - GitHub Pages documentation
   - Inline code documentation
   - Troubleshooting guides

---

## Common GitHub Repository Issues to Check

### Security Issues
- Missing branch protection on default branch
- Overly permissive workflow permissions
- Unverified third-party actions in workflows
- Exposed secrets in workflow logs
- Disabled security scanning features
- Missing required status checks
- Inadequate review requirements

### Workflow Issues
- Workflows running with excessive permissions
- Missing environment protection for production deployments
- Inadequate secret management
- Missing workflow status badges
- Poor artifact management
- Lack of deployment automation

### Collaboration Issues
- Missing or inadequate issue templates
- No pull request templates
- Missing CODEOWNERS file
- Inconsistent labeling system
- Poor project board organization
- Inadequate contributor guidelines

### Documentation Issues
- Incomplete or outdated README
- Missing API documentation
- No troubleshooting guides
- Inadequate setup instructions
- Missing architecture documentation

---

## File Organization and Version Management

### Recommended File Structure

When generating GitHub assessment reports, organize files using this recommended structure:

```
docs/
├── assessments/
│   ├── gh-assessment-report.md                           # Current/Latest (symlink or copy)
│   ├── gh-assessment-template.md                         # Template (no versioning needed)
│   ├── gh-assessment-prompt.md                          # Automation prompt (no versioning needed)
│   ├── gh-assessment-report-v1.0.0.md                   # Initial assessment
│   ├── gh-assessment-report-v1.1.0.md                   # Minor updates/improvements
│   ├── gh-assessment-report-v2.0.0.md                   # Major methodology changes
│   └── archives/
│       ├── gh-assessment-report-v1.0.0-2025-01-15.md    # Archived with dates
│       └── gh-assessment-report-v1.1.0-2025-03-20.md    # Historical versions
```

### Version Management Examples

**When to increment versions:**

**Patch Version (X.Y.Z → X.Y.Z+1):**
- Correcting spelling/grammar errors
- Fixing calculation errors in compliance ratings
- Minor clarifications in findings
- Small formatting improvements

**Minor Version (X.Y.Z → X.Y+1.0):**
- Adding new technology-specific parameters
- Enhancing existing assessment sections
- Including additional best practices
- Expanding recommendation details

**Major Version (X.Y.Z → X+1.0.0):**
- Adding new assessment categories
- Changing compliance calculation methodology
- Significant template structure changes
- Major organizational policy updates

### File Naming Examples

**Repository-Specific Reports:**
```
gh-assessment-solution-tf-azure-global-linux-vm-v1.0.0.md
gh-assessment-webapp-frontend-react-v2.1.0.md
gh-assessment-api-backend-nodejs-v1.3.2.md
```

**General Assessment Reports:**
```
gh-assessment-report-v1.0.0.md
gh-assessment-report-v1.1.0.md
gh-assessment-report-v2.0.0.md
```

**Date-Based Archival (Optional):**
```
gh-assessment-report-v1.0.0-2025-01-15.md
gh-assessment-report-v1.1.0-2025-03-20.md
gh-assessment-report-v2.0.0-2025-07-18.md
```

### Version Tracking in Document Header

**CRITICAL REQUIREMENT:** Always ensure version consistency between filename and document content:

```markdown
**Repository Name:** solution-tf-azure-global-linux-vm
**Date of Assessment:** 2025-07-18
**Author:** Assessment Team
**Repository URL:** https://github.com/Mohawk-Industries/solution-tf-azure-global-linux-vm
**Visibility:** Private
**Owner:** Mohawk-Industries
**Default Branch:** main
**Template Version:** 2.0.0
```

**Executive Summary Version Reference:**
```markdown
> **GitHub Repository Assessment (2025-07-18, Version 2.0.0):** [SUMMARY]
```

**Filename Must Match:**
- Document shows `**Template Version:** 2.0.0`
- Executive Summary shows `Version 2.0.0`
- Filename MUST be: `gh-assessment-report-v2.0.0.md`

**Version Mismatch Prevention:**
- ❌ **WRONG:** Filename `gh-assessment-report-v1.0.0.md` with document showing `Template Version: 2.0.0`
- ✅ **CORRECT:** Filename `gh-assessment-report-v2.0.0.md` with document showing `Template Version: 2.0.0`

### Assessment Quality Checklist

Before finalizing the GitHub assessment report, verify:

- [ ] **VERSION CONSISTENCY:** Filename version exactly matches document header version and executive summary version
- [ ] All [PLACEHOLDER] values have been replaced with actual findings
- [ ] Compliance percentages are based on actual parameter evaluation
- [ ] Recommendations are specific and actionable for the repository
- [ ] Security issues are prioritized appropriately
- [ ] GitHub-specific features are thoroughly evaluated
- [ ] Repository type considerations are applied correctly
- [ ] Examples and evidence support all findings
- [ ] The report structure follows the template exactly
- [ ] Critical issues are highlighted in priority recommendations
- [ ] Contact information and metadata are updated
- [ ] Document version in header matches the assessment scope and changes made

---

## Dynamic Parameter Addition Examples

### Example: Adding Terraform-Specific Parameters

When you detect a Terraform repository (presence of .tf files, terraform/ directory, etc.), add these parameters to the appropriate sections:

**Repository Structure & Configuration section:**
```
| Terraform module structure follows best practices | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Variable definitions are well documented | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Output values are properly defined | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Provider version constraints are specified | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

**GitHub Security Assessment section:**
```
| Terraform state file security | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Secrets management in Terraform variables | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Provider authentication security | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

**GitHub Workflows & Automation section:**
```
| Terraform plan automation in workflows | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Terraform apply automation with approvals | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| State locking mechanism configured | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Environment-specific deployment workflows | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

### Example: Adding Docker-Specific Parameters

When you detect a Docker repository (presence of Dockerfile, docker-compose.yml, etc.), add these parameters:

**Repository Structure & Configuration section:**
```
| Dockerfile follows multi-stage build best practices | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| .dockerignore file is properly configured | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Docker Compose configuration for development | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

**GitHub Security Assessment section:**
```
| Container image vulnerability scanning | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Non-root user configuration in containers | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Container secrets management | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

**GitHub Workflows & Automation section:**
```
| Container build automation | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Container registry integration | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
| Container security scanning in CI/CD | [STATUS] | [FINDINGS] | [RECOMMENDATIONS] |
```

### Parameter Addition Guidelines

1. **Technology Detection Patterns:**
   - Terraform: .tf files, .terraform/ directory, terraform.tfstate
   - Node.js: package.json, package-lock.json, node_modules/
   - Python: requirements.txt, setup.py, pyproject.toml, .python-version
   - Docker: Dockerfile, docker-compose.yml, .dockerignore
   - .NET: .csproj, .sln, packages.config, Program.cs
   - Java: pom.xml, build.gradle, src/main/java/
   - Go: go.mod, go.sum, main.go
   - Rust: Cargo.toml, Cargo.lock, src/lib.rs

2. **Section Mapping Guidelines:**
   - **Repository Structure**: File organization, configuration files, dependency management
   - **Security**: Technology-specific security practices, vulnerability scanning, secrets management
   - **Workflows**: Build automation, testing, deployment pipelines, technology-specific CI/CD
   - **Code Quality**: Language-specific linting, testing frameworks, code standards
   - **Documentation**: Technology-specific documentation, API docs, setup guides

3. **Parameter Naming Convention:**
   - Use descriptive, specific parameter names
   - Include technology name when applicable
   - Follow the existing parameter format in the template
   - Ensure parameters are measurable and actionable

---

## Repository Patterns and Naming Conventions

When assessing repository naming compliance, use these organizational standards to evaluate whether the repository follows proper naming conventions:

### 1. Module Repository
**Definition:** The smallest, reusable unit (e.g., VNet, subnet, storage account).
**Purpose:** Encapsulates a single resource or function, designed for maximum reusability and composability.
**Best Practices:**
- Use semantic versioning (e.g., v1.2.3) for releases
- Keep modules generic, well-documented, and independently testable
**Naming pattern:** `module-<tooling>-<provider>-<service>-<resource>`
**Example:** `module-tf-azurerm-storage-container`

### 2. Component Repository
**Definition:** Aggregates multiple modules to deliver a higher-level resource (e.g., a VM with networking, disks, monitoring, and security).
**Purpose:** Encapsulates orchestration logic and cross-module dependencies for complex resources that require tight integration.
**Best Practices:**
- Use only when multiple modules must always be deployed together
- Maintain clear, minimal orchestration logic to avoid monolithic components
**Naming pattern:** `component-tf-<resource>`
**Example:** `component-tf-linux-virtual-machine`

### 3. Solution Repository
**Definition:** The top-level repo for an environment or application, referencing modules and/or components to deliver complete infrastructure.
**Purpose:**
- Contains environment definitions for a project (e.g., development, staging, production)
- References modules and/or components via repository URLs and specific tags, ensuring stability and repeatability
- Supports infrastructure deployment workflows and automation pipelines
**Best Practices:**
- Use a consistent prefix for related resources (e.g., all resources for a project in the same resource group)
- Include environment and application names to differentiate between stages (dev, test, prod) and applications
- Be mindful of character limits and naming restrictions of the underlying cloud provider
**Naming pattern:** `solution-<tooling>-<provider>-<org/project>-<env/app>-<resource>` or `central-<tooling>-<provider>-<service/resource>`
**Examples:**
- `solution-tf-azure-frow-digops-managed-grafana`
- `central-tf-azure-global-linux-vm`

### Repository Type Detection and Assessment

When analyzing a repository, determine its type based on the naming pattern and content:

**Module Repository Assessment:**
- Verify single-purpose functionality
- Check for semantic versioning in releases
- Assess module documentation quality
- Evaluate reusability and composability

**Component Repository Assessment:**
- Verify multi-module integration
- Check for clear orchestration logic
- Assess dependency management
- Evaluate component-level documentation

**Solution Repository Assessment:**
- Verify complete infrastructure definition
- Check for environment separation
- Assess deployment automation
- Evaluate solution-level documentation

**General Repository Assessment:**
- Evaluate against general best practices
- Check for appropriate structure and documentation
- Assess security and quality standards
- Provide recommendations for improvement

---

## Usage Examples

### For Infrastructure Repository:
```
"Analyze this Terraform repository focusing on infrastructure deployment workflows, state management security, environment separation, and GitHub Actions automation for infrastructure provisioning."
```

### For Application Repository:
```
"Assess this application repository with emphasis on CI/CD pipeline security, automated testing workflows, dependency management, and deployment automation practices."
```

### For Library Repository:
```
"Evaluate this library repository considering package publishing automation, semantic versioning compliance, API documentation quality, and community contribution workflows."
```

---

**Note:** This prompt is designed to work with the gh-assessment-template.md file. Ensure both files are available when conducting automated assessments. The assessment should be tailored to the specific repository type and organizational requirements while maintaining consistency with GitHub best practices.

**Template Version:** 1.0.0  
**Last Updated:** [Current Date]  
**Compatible with:** GitHub Free, GitHub Pro, GitHub Team, GitHub Enterprise
