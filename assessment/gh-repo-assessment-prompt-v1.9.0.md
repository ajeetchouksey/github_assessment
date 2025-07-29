# GitHub Repository Assessment Prompt v1.9.0

## Assessment Framework Instructions

Conduct a comprehensive GitHub repository assessment using the following methodology and instructions. This prompt provides assessment guidelines only - all structure and formatting is defined in the template.


## Template Usage Instructions

**CRITICAL: Template-First Approach**

- **ALWAYS use the latest template** from: `assessment_compliance/repository/template/gh-repo-assessment-template-v{LATEST_VERSION}.md`
- **Follow template structure exactly** - do not modify or create custom sections
- **Fill template placeholders** with assessment findings using the methodology below
- **Replace ALL metadata placeholders (e.g., [REPO_NAME], [REPO_TYPE], [TECH_STACK], [COMPLIANCE_LEVEL], [SECURITY_PRIORITY], [AUTOMATION_PRIORITY], [ASSESSMENT_VERSION], [ASSESSMENT_DATE], [REPO_URL], [PUBLIC/PRIVATE], [OWNER_NAME], [DEFAULT_BRANCH]) in the template with actual repository values. Do not leave any metadata placeholder unreplaced.**
- **DO NOT hardcode any structure** in this prompt - template is the single source of truth
 - **Use icons or emojis only when necessary and keep them to a minimum. Only use professional icons as appropriate, and only if explicitly defined in the template.**

---

## Copilot Archiving Script (Mandatory)

**After generating the latest assessment report, Copilot must perform the following steps in order:**

1. Identify all markdown files in `assessment_compliance_reports/repository/` matching `gh-repo-assessment-v*.md`.
2. Determine the latest assessment report by version number.
3. For every other assessment report markdown file (except the latest version), move it to `assessment_compliance_reports/repository/archive/`.
4. Only the most recent assessment report must remain in the main report directory.
5. This archiving process is mandatory and must be executed every time a new assessment is generated.

---
- **Use text-only status indicators** (e.g., "COMPLIANT", "NON-COMPLIANT", "PARTIAL", "NOT APPLICABLE")
- **Dynamically determine latest template version** from available files

## Path References for Reusability

**IMPORTANT: Output Path Configuration**

- **Assessment Reports**: Save to `assessment_compliance_reports/repository/` (relative to repository root)
- **Archive Reports**: Move old reports to `assessment_compliance_reports/repository/archive/`
- **Template Location**: Use template from `assessment_compliance/repository/template/gh-repo-assessment-template-v{LATEST_VERSION}.md`
- **Framework Documentation**: Reference `assessment_compliance/` folder for usage instructions

## Assessment Version Management

**IMPORTANT: Assessment Versioning Requirements**

- Use semantic versioning format: MAJOR.MINOR.PATCH
- MAJOR: Significant framework changes or complete restructuring
- MINOR: New analysis categories, significant template changes, or additional features
- PATCH: Bug fixes, minor improvements, or clarifications
- Assessment version MUST be updated on every run based on the nature of changes
- **Assessment report filename format**: `gh-repo-assessment-v{ASSESSMENT_VERSION}.md` (WITHOUT date or repository name)
- **Assessment frequency**: Use "weekly (recommended) / fortnight" format
- Framework version must be dynamically determined from latest available version

## Assessment Methodology

...existing code...

### Quality Assurance Checklist

**Before finalizing the assessment, you must:**

1. Ensure all compliance scores are calculated using the defined weighting methodology.
2. Populate every required template section with complete, relevant findings.
3. Provide recommendations that are specific, actionable, and prioritized by risk and impact.
4. Maintain correct markdown formatting and strictly follow the template structure.
5. Confirm all findings, scores, and recommendations are consistent and cross-referenced.
6. Apply technology-specific guidance that matches the detected stack.
7. Replace every metadata placeholder in the template (such as [REPO_NAME], [REPO_TYPE], [TECH_STACK], [COMPLIANCE_LEVEL], [SECURITY_PRIORITY], [AUTOMATION_PRIORITY], [ASSESSMENT_VERSION], [ASSESSMENT_DATE], [REPO_URL], [PUBLIC/PRIVATE], [OWNER_NAME], [DEFAULT_BRANCH]) with the actual repository value. Do not leave any placeholder unreplaced.
8. For every assessment outcome, the status must be one of the following (case-insensitive): COMPLIANT, NON-COMPLIANT, PARTIAL, or NOT APPLICABLE. No other status values are permitted. Ensure this is enforced throughout the report.
9. After generating the latest assessment report markdown file, Copilot must move all previous assessment report markdown files (except the latest version) into the archive directory (`assessment_compliance_reports/repository/archive/`). Only the most recent assessment report must remain in the main report directory. This is a mandatory Copilot action and not optional.

### Report Generation Instructions

1. **Use Latest Template**: Locate and use the most recent template version from the template directory
2. **Fill All Placeholders**: Replace all template placeholders with actual assessment data
3. **Maintain Structure**: Do not modify template structure or create custom sections
4. **Apply Methodology**: Use the assessment criteria and scoring methodology defined above
5. **Technology Customization**: Adapt findings and recommendations to the specific technology stack
6. **Prioritize Actions**: Ensure recommendations are properly prioritized by risk and impact

### Output Requirements

**Assessment Report Generation:**
- Save assessment report to: `assessment_compliance_reports/repository/gh-repo-assessment-v{ASSESSMENT_VERSION}.md`
- Archive any existing reports to: `assessment_compliance_reports/repository/archive/`
- Use semantic versioning for assessment version based on changes made
- Include comprehensive findings for all assessment categories
- Provide specific, actionable recommendations with implementation guidance
- Calculate accurate compliance scores using defined weighting methodology

### Final Notes

- This prompt focuses on methodology and assessment criteria only
- All output structure and formatting is controlled by the template
- Assessment version should be incremented based on the nature of framework changes
- Template version and assessment version may differ - template controls structure, assessment version tracks methodology changes
- Regular assessment schedules should be recommended based on repository criticality and change frequency

## Assessment Methodology

### Repository Analysis Process

1. **Repository Discovery & Context Gathering**
   - Examine repository structure, files, and configuration
   - Identify technology stack and repository type
   - Determine repository visibility and ownership
   - Assess repository size, activity, and maturity

2. **Security Configuration Review**
   - Check GitHub security settings and policies
   - Evaluate branch protection rules and access controls
   - Assess secret management and vulnerability scanning
   - Review security policy documentation and practices

3. **Code Quality & Standards Assessment**
   - Evaluate code standards, formatting, and consistency
   - Assess testing coverage and quality practices
   - Review documentation and code comments
   - Check dependency management and review processes

4. **Automation & Workflow Analysis**
   - Assess CI/CD pipeline implementation and effectiveness
   - Review GitHub Actions workflows and automation
   - Evaluate deployment processes and strategies
   - Check monitoring, observability, and error handling

5. **Documentation & Knowledge Management**
   - Review documentation quality, completeness, and organization
   - Assess README, API docs, and project documentation
   - Evaluate wiki usage and knowledge sharing practices
   - Check documentation maintenance and version control

### Assessment Categories & Weighting

**Core Assessment Areas (Used in Overall Compliance Calculation):**
- **Repository Structure & Organization**: 20% weight
- **Security & Access Control**: 25% weight (highest priority)
- **Code Quality & Standards**: 20% weight
- **Workflows & Automation**: 20% weight
- **Documentation & Knowledge Management**: 10% weight
- **Collaboration & Community Features**: Optional enhancement (not counted in overall)

### Scoring Methodology

**Evaluation Criteria for Each Category:**
- Use checklist-based scoring where each completed item earns points
- Calculate percentage compliance for each category
- Apply category weights to determine overall compliance
- Identify Critical, High, Medium, and Low priority issues
- Provide specific, actionable recommendations for each finding

**Rating Scale:**
- 90-100%: Excellent
- 80-89%: Good
- 70-79%: Acceptable
- 60-69%: Needs Improvement
- Below 60%: Critical Issues

### Technology-Specific Analysis Guidelines

**For Each Detected Technology Stack, Provide:**
- Language-specific best practices and security considerations
- Framework-specific guidelines and recommendations
- Tooling recommendations for the technology
- Performance optimization opportunities
- Configuration examples and reference documentation

### Repository Structure Assessment Criteria

**Evaluate the following elements:**
- Clear project organization and logical file structure
- Comprehensive README with project description, setup, and usage
- Proper documentation hierarchy and organization
- Configuration files properly organized (.gitignore, package files, etc.)
- License file present and appropriate for project
- Contributing guidelines and code of conduct (where applicable)
- Issue and PR templates configured appropriately
- Security policy and governance documentation

### Security Assessment Criteria

**GitHub Security Features to Evaluate:**
- Branch protection rules configured for default branch
- Required reviews setup for protected branches with appropriate reviewers
- Status checks required before merging with proper configuration
- Force pushes and deletions restricted appropriately
- Secret scanning enabled and configured
- Vulnerability alerts and Dependabot security updates enabled
- Code scanning (CodeQL/SAST) implemented where applicable
- Private vulnerability reporting enabled for public repositories
- Two-factor authentication enforcement for contributors
- Repository permissions and access control properly managed

### Code Quality Assessment Criteria

**Code Standards and Review Process:**
- Consistent code formatting and style across the codebase
- Comprehensive test coverage with quality test practices
- Adequate documentation and meaningful code comments
- Dependency management following best practices
- Code review process documented and enforced
- Linting and formatting tools configured and automated
- Pre-commit hooks setup where appropriate
- Quality gates integrated into CI/CD pipeline

### Workflow & Automation Assessment Criteria

**CI/CD and Automation Evaluation:**
- CI/CD pipeline implemented with appropriate stages
- Automated testing on pull requests with comprehensive coverage
- Automated deployments configured with proper environments
- GitHub Actions workflows following security best practices
- Workflow permissions following least privilege principle
- Automated dependency updates and security scanning
- Performance monitoring and error tracking integrated
- Rollback capabilities and deployment safety measures

### Documentation Assessment Criteria

**Documentation Quality and Completeness:**
- Comprehensive project documentation covering all aspects
- API documentation available and up-to-date (if applicable)
- Clear setup and installation guides for different environments
- Architecture documentation explaining system design
- Changelog maintained with version history
- Wiki utilized effectively for additional documentation
- Documentation kept current with code changes
- Multiple documentation formats supported as needed

### Risk Assessment Framework

**Identify and classify risks in these categories:**
- **Security Risks**: Vulnerabilities, access control issues, exposed secrets
- **Operational Risks**: Process gaps, automation failures, deployment issues
- **Compliance Risks**: Policy violations, governance gaps, audit findings
- **Technical Debt**: Code quality issues, outdated dependencies, maintenance burden

### Implementation Roadmap Guidelines

**Create prioritized action plan with phases:**
- **Phase 1 (Critical)**: Security vulnerabilities and compliance issues requiring immediate attention
- **Phase 2 (High Priority)**: Process improvements, automation gaps, and significant quality issues
- **Phase 3 (Medium Priority)**: Enhancement opportunities, optimization, and workflow improvements
- **Phase 4 (Low Priority)**: Long-term repository maturity and community features

### GitHub-Specific Recommendations

**Focus on GitHub-native features and integrations:**
- Advanced security features (Advanced Security, CodeQL, secret scanning)
- GitHub Apps and marketplace tools integration
- Actions and automation opportunities specific to GitHub
- Project management features (Projects, Issues, Milestones)
- Community and collaboration features (Discussions, Wiki, Pages)

### Quality Assurance Checklist

**Before finalizing the assessment, you must:**
1. Ensure all compliance scores are calculated using the defined weighting methodology.
2. Populate every required template section with complete, relevant findings.
3. Provide recommendations that are specific, actionable, and prioritized by risk and impact.
4. Maintain correct markdown formatting and strictly follow the template structure.
5. Confirm all findings, scores, and recommendations are consistent and cross-referenced.
6. Apply technology-specific guidance that matches the detected stack.
7. Replace every metadata placeholder in the template (such as [REPO_NAME], [REPO_TYPE], [TECH_STACK], [COMPLIANCE_LEVEL], [SECURITY_PRIORITY], [AUTOMATION_PRIORITY], [ASSESSMENT_VERSION], [ASSESSMENT_DATE], [REPO_URL], [PUBLIC/PRIVATE], [OWNER_NAME], [DEFAULT_BRANCH]) with the actual repository value. Do not leave any placeholder unreplaced.
8. For every assessment outcome, the status must be one of the following (case-insensitive): COMPLIANT, NON-COMPLIANT, PARTIAL, or NOT APPLICABLE. No other status values are permitted. Ensure this is enforced throughout the report.
9. After generating the latest assessment report markdown file, Copilot must move all previous assessment report markdown files (except the latest version) into the archive directory (`assessment_compliance_reports/repository/archive/`). Only the most recent assessment report must remain in the main report directory. This is a mandatory Copilot action and not optional.

### Report Generation Instructions

1. **Use Latest Template**: Locate and use the most recent template version from the template directory
2. **Fill All Placeholders**: Replace all template placeholders with actual assessment data
3. **Maintain Structure**: Do not modify template structure or create custom sections
4. **Apply Methodology**: Use the assessment criteria and scoring methodology defined above
5. **Technology Customization**: Adapt findings and recommendations to the specific technology stack
6. **Prioritize Actions**: Ensure recommendations are properly prioritized by risk and impact

### Output Requirements

**Assessment Report Generation:**
- Save assessment report to: `assessment_compliance_reports/repository/gh-repo-assessment-v{ASSESSMENT_VERSION}.md`
- Archive any existing reports to: `assessment_compliance_reports/repository/archive/`
- Use semantic versioning for assessment version based on changes made
- Include comprehensive findings for all assessment categories
- Provide specific, actionable recommendations with implementation guidance
- Calculate accurate compliance scores using defined weighting methodology

### Final Notes

- This prompt focuses on methodology and assessment criteria only
- All output structure and formatting is controlled by the template
- Assessment version should be incremented based on the nature of framework changes
- Template version and assessment version may differ - template controls structure, assessment version tracks methodology changes
- Regular assessment schedules should be recommended based on repository criticality and change frequency

---

*This assessment prompt is specifically designed for GitHub repositories and focuses on GitHub-native features, security controls, and collaboration tools. The prompt provides methodology only - all structure is defined in the referenced template.*
