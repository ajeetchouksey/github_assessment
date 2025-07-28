
# GitHub Copilot Usage Instructions

## Instruction Clarity and Pre-Commit Checks

- **All instructions must be clear and definitive.** Avoid ambiguity in prompts, code comments, and documentation. Write actionable, specific guidance for Copilot and contributors.
- **Before committing code, perform a thorough check to identify possible errors:**
	- Review all code changes for syntax, logic, and security issues.
	- Ensure automation and workflows are correctly configured and tested.
	- Validate that documentation is up to date and instructions are actionable.
	- Run all relevant tests and verify that workflows pass.
	- Double-check that Copilot-generated code is reviewed and meets repository standards.

## Overview
This document provides guidelines, best practices, and repo-specific tips for using GitHub Copilot in this repository.

---

## How to Use Copilot Effectively
- Use Copilot to generate code, documentation, and configuration files.
- Use Copilot to help maintain and extend automation workflows (see `.github/workflows/`).
- Use Copilot for boilerplate, repetitive code, and automation scripts (e.g., `.github/scripts/`).
- Always review Copilot suggestions for correctness and security before committing.
- For sensitive or security-critical code, double-check Copilot output and add manual tests.

---

## Copilot for Repository Automation

- Use Copilot to automate repetitive repository management tasks, such as labeling issues, triaging pull requests, or assigning reviewers.
- Leverage Copilot to generate scripts for automating dependency updates, branch cleanup, or release note generation.
- Employ Copilot to help create or update GitHub Actions for automating testing, deployment, and code quality checks.
- Use Copilot to draft custom bots or integrations that streamline repository workflows and notifications.
- Always review and test Copilot-generated automation scripts to ensure they are safe, efficient, and meet your repository’s requirements.
- Integrate Copilot suggestions with existing automation tools and workflows for seamless repository operations.
- Document any Copilot-assisted automation clearly for future maintainers and contributors.
- Use Copilot to generate or update GitHub Actions workflows for CI/CD, security, and automation.
- Let Copilot help you maintain configuration files such as `.github/CODEOWNERS`, `.github/dependabot.yml`, and PR templates.
- Use Copilot to draft or improve security policies (`SECURITY.md`) and CodeQL queries for code scanning.
- Copilot can assist in writing custom scripts for repository management in `.github/scripts/`.

---

## Copilot in Pull Requests

- Use Copilot to draft clear, detailed, and actionable pull request (PR) descriptions, outlining the purpose, changes, and impact of the PR.
- Let Copilot help you fill out all sections of PR templates, ensuring completeness and clarity.
- Use Copilot to suggest code review comments, highlight potential improvements, or flag areas needing further attention.
- Reference Copilot-generated code or suggestions explicitly in your PRs for transparency and traceability.
- For advanced PRs, leverage Copilot to:
    - Generate changelogs or summaries of significant changes.
    - Suggest test cases or validation steps relevant to the PR.
    - Propose documentation updates that should accompany the code changes.
    - Identify and list potential risks or breaking changes introduced by the PR.
- Always review and edit Copilot-generated PR content to ensure accuracy, professionalism, and alignment with repository standards.
- Encourage reviewers to use Copilot for suggesting improvements or identifying issues during the review process.
- Use Copilot to automate repetitive PR tasks, such as labeling, assigning reviewers, or updating status checks.
- Document any Copilot-assisted decisions or code changes in the PR discussion for future reference.

- Copilot can help draft PR descriptions and fill out PR templates.
- Use Copilot to suggest code review comments or improvements.
- Reference Copilot-generated code in your PRs for transparency.

---

## Security and Compliance

- Never accept Copilot suggestions that include secrets, credentials, or any sensitive information.
- Ensure all Copilot-generated code complies with your organization’s security policies and coding standards.
- Review Copilot output for potential vulnerabilities, insecure patterns, or license compliance issues.
- Use Copilot to help maintain up-to-date security documentation (e.g., `SECURITY.md`) and automate security checks in workflows.
- Validate that Copilot-generated scripts and workflows do not expose confidential data or introduce compliance risks.
- Regularly audit Copilot-assisted changes for adherence to privacy, regulatory, and security requirements.
- Document any security-related decisions or Copilot-assisted changes for future reference and audits.

### Automating GitHub Security Features

- Use Copilot to generate or update workflows that enable and configure the following security features via the GitHub API or CLI:
	- **Private vulnerability reporting** (for private repos): Add a workflow step using `gh api` to enable this feature.
	- **Dependency graph and automatic dependency submission**: Add a workflow step to enable these via `gh api`.
	- **Dependabot alerts and security updates**: Ensure `.github/dependabot.yml` is present and add a workflow step to enable alerts for private repos.
	- **Grouped security updates and version updates**: Configure these in `.github/dependabot.yml` using the `groups:` key and update schedules.

#### Example workflow steps to automate security features:

```yaml
- name: Enable Private Vulnerability Reporting
	if: github.repository_visibility == 'private'
	run: |
		gh api -X PATCH \
			-H "Accept: application/vnd.github+json" \
			"/repos/${{ github.repository }}" \
			-f private_vulnerability_reporting=true
- name: Enable Dependency Submission
	run: |
		gh api -X PATCH \
			-H "Accept: application/vnd.github+json" \
			"/repos/${{ github.repository }}" \
			-f dependency_graph_enabled=true \
			-f dependency_submission_enabled=true
- name: Enable Dependabot Alerts and Security Updates
	run: |
		gh api -X PATCH \
			-H "Accept: application/vnd.github+json" \
			"/repos/${{ github.repository }}" \
			-f vulnerability_alerts=true
```

- Always use a Personal Access Token (PAT) with admin rights for these API calls in workflows.
- Review and update `.github/dependabot.yml` to include all relevant ecosystems, update schedules, and group rules for grouped updates.

---

## Example Copilot Prompts for This Repository

- "Create a GitHub Actions workflow to run CodeQL analysis on every push."
- "Suggest a CODEOWNERS file for a project with frontend and backend directories."
- "Write a Dependabot configuration for npm and GitHub Actions updates."
- "Draft a PR template for bug reports."
- "Generate a Python script to validate PR template structure."

---

## Troubleshooting
- If Copilot suggestions are not relevant, try rephrasing your comment or providing more context.
- For complex logic, break down your request into smaller steps for better results.

---

## Changelog and Documentation Updates

- Use Copilot to generate or update a `CHANGELOG.md` file that summarizes notable changes, enhancements, and bug fixes for each release.
- **This code is intended to be developed as a reusable, generic tool.** Ensure all code, scripts, and configurations are designed for portability and can be easily integrated or adapted for use in any repository. Avoid hardcoding repository-specific values, and structure the codebase for maximum reusability and maintainability.
- When making changes, use Copilot to help update user-facing documentation (e.g., `README.md`, usage guides) so it accurately reflects the latest features, usage instructions, and configuration options.
- Always review Copilot-generated changelog entries and documentation updates for clarity, accuracy, and completeness before committing.
- Encourage contributors to update both the changelog and relevant documentation as part of their pull requests.


## Additional Resources
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot Labs](https://githubnext.com/projects/copilot-labs/)

---

For questions or improvements, open an issue or pull request.
