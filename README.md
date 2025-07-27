# assessment

## Automated CODEOWNERS Management

This repository includes a reusable GitHub Action to ensure a `.github/CODEOWNERS` file exists. The action can be used locally or in other repositories to automate CODEOWNERS file creation.

### How It Works

- The composite action is located at `.github/actions/ensure-codeowners/action.yml`.
- The workflow `.github/workflows/ensure-codeowners.yml` runs the action on every push to `main` or via manual dispatch.
- If `.github/CODEOWNERS` does not exist, it will be created with the specified owner.
- If the file exists, no changes are made.

### Usage in This Repository

1. Edit `.github/workflows/ensure-codeowners.yml` and set the `owner` input to your GitHub username or team (e.g., `@your-github-username` or `@org/team`).
2. Commit and push your changes.
3. The workflow will run automatically or can be triggered manually from the Actions tab.

### Usage in Other Repositories

1. Copy the `.github/actions/ensure-codeowners` directory to your target repository.
2. Add or update a workflow (e.g., `.github/workflows/ensure-codeowners.yml`) with the following content:

		```yaml
		name: Ensure CODEOWNERS
		on:
			workflow_dispatch:
			push:
				branches: [main]
		jobs:
			ensure-codeowners:
				runs-on: ubuntu-latest
				steps:
					- uses: actions/checkout@v4
					- uses: ./.github/actions/ensure-codeowners
						with:
							owner: '@your-github-username'
		```
3. Set the `owner` input as needed.
4. Commit and push. The workflow will ensure a CODEOWNERS file is present.

### Customization

- You can change the default owner by editing the workflow input.
- The action can be extended to support more advanced CODEOWNERS logic if needed.

---
For questions or improvements, open an issue or pull request.

---

## Automated dependabot.yml Management

This repository includes a reusable GitHub Action to ensure a `.github/dependabot.yml` file exists with all configuration options. The action can be used locally or in other repositories to automate dependabot configuration.

### How It Works

- The composite action is located at `.github/actions/ensure-dependabot/action.yml`.
- The workflow `.github/workflows/ensure-dependabot.yml` runs the action on every push to `main` or via manual dispatch.
- If `.github/dependabot.yml` does not exist, it will be created with the specified configuration options.
- If the file exists, no changes are made.

### Usage in This Repository

1. Edit `.github/workflows/ensure-dependabot.yml` and set the inputs as needed:
		- `package-ecosystem` (e.g., `npm`, `pip`, `maven`, etc.)
		- `directory` (e.g., `/`, `/src`, `/backend`)
		- `schedule-interval` (`daily`, `weekly`, `monthly`)
		- `open-pull-requests-limit` (default: `5`)
		- `rebase-strategy` (`auto`, `disabled`, `eager`)
		- `versioning-strategy` (`auto`, `widen`, `increase`, `lockfile-only`, `increase-if-necessary`)
		- `allow` (YAML array as string, optional)
		- `ignore` (YAML array as string, optional)
2. Commit and push your changes.
3. The workflow will run automatically or can be triggered manually from the Actions tab.

### Usage in Other Repositories

1. Copy the `.github/actions/ensure-dependabot` directory to your target repository.
2. Add or update a workflow (e.g., `.github/workflows/ensure-dependabot.yml`) with the following content:

		```yaml
		name: Ensure dependabot.yml
		on:
			workflow_dispatch:
			push:
				branches: [main]
		jobs:
			ensure-dependabot:
				runs-on: ubuntu-latest
				steps:
					- uses: actions/checkout@v4
					- uses: ./.github/actions/ensure-dependabot
						with:
							package-ecosystem: 'npm'
							directory: '/'
							schedule-interval: 'weekly'
							open-pull-requests-limit: '5'
							rebase-strategy: 'auto'
							versioning-strategy: 'auto'
							allow: ''
							ignore: ''
		```
3. Set the inputs as needed for your project.
4. Commit and push. The workflow will ensure a dependabot.yml file is present.

### Customization

- You can change the configuration options by editing the workflow inputs.
- The action can be extended to support more advanced dependabot logic if needed.

---
For questions or improvements, open an issue or pull request.

---

## Automated Pull Request Template Management

This repository includes a reusable GitHub Action to ensure a `.github/pull_request_template.md` file exists. The action can be used locally or in other repositories to automate PR template creation.

### How It Works

- The composite action is located at `.github/actions/ensure-pr-template/action.yml`.
- The workflow `.github/workflows/ensure-pr-template.yml` runs the action on every push to `main`, on a schedule, or via manual dispatch.
- If `.github/pull_request_template.md` does not exist, it will be created with the specified content.
- If the file exists, no changes are made.

### Usage in This Repository

1. Edit `.github/workflows/ensure-pr-template.yml` and set the `template-content` input to your desired PR template (Markdown).
2. Commit and push your changes.
3. The workflow will run automatically or can be triggered manually from the Actions tab.

### Usage in Other Repositories

1. Copy the `.github/actions/ensure-pr-template` directory to your target repository.
2. Add or update a workflow (e.g., `.github/workflows/ensure-pr-template.yml`) with the following content:

		```yaml
		name: Ensure PR Template
		on:
			workflow_dispatch:
			push:
				branches: [main]
			schedule:
				- cron: '0 3 * * 1'
		jobs:
			ensure-pr-template:
				runs-on: ubuntu-latest
				steps:
					- uses: actions/checkout@v4
					- uses: ./.github/actions/ensure-pr-template
						with:
							template-content: |
								# Pull Request
                
								## Description
								Please include a summary of the change and which issue is fixed. Also include relevant motivation and context.
                
								## Type of change
								- [ ] Bug fix
								- [ ] New feature
								- [ ] Breaking change
								- [ ] Documentation update
								- [ ] Other (describe below)
                
								## Checklist
								- [ ] My code follows the style guidelines of this project
								- [ ] I have performed a self-review of my code
								- [ ] I have commented my code, particularly in hard-to-understand areas
								- [ ] I have made corresponding changes to the documentation
								- [ ] My changes generate no new warnings
								- [ ] I have added tests that prove my fix is effective or that my feature works
								- [ ] New and existing unit tests pass locally with my changes
								- [ ] Any dependent changes have been merged and published in downstream modules
                
								## Related Issues
								Fixes # (issue)
                
								## Additional Notes
								Add any other context about the pull request here.
		```
3. Set the `template-content` input as needed.
4. Commit and push. The workflow will ensure a PR template file is present.

### Customization

- You can change the PR template content by editing the workflow input.
- The action can be extended to support more advanced PR template logic if needed.

---
For questions or improvements, open an issue or pull request.

---

## Advanced Pull Request Templates Automation

This repository includes a reusable GitHub Action to ensure multiple PR templates exist, with support for dynamic content, update logic, and validation.

### How It Works

- The composite action is located at `.github/actions/ensure-pr-templates-advanced/action.yml`.
- The workflow `.github/workflows/ensure-pr-templates-advanced.yml` runs the action on every push to `main`, on a schedule, or via manual dispatch.
- You can define multiple templates (e.g., `feature.md`, `bugfix.md`) with custom content.
- Dynamic fields like `{{DATE}}` and `{{AUTHOR}}` are replaced automatically.
- If a template exists, it will be updated if `overwrite` is set to `true`.
- The action validates that each template includes `Description` and `Checklist` sections.

### Usage in This Repository

1. Edit `.github/workflows/ensure-pr-templates-advanced.yml` and set the `templates` input as a YAML array of template objects:
		- `name`: The filename (e.g., `feature.md`)
		- `content`: The Markdown content (supports `{{DATE}}` and `{{AUTHOR}}`)
2. Set `overwrite`, `inject-date`, and `inject-author` as needed.
3. Commit and push your changes.
4. The workflow will run automatically or can be triggered manually from the Actions tab.

### Usage in Other Repositories

1. Copy the `.github/actions/ensure-pr-templates-advanced` directory to your target repository.
2. Add or update a workflow (e.g., `.github/workflows/ensure-pr-templates-advanced.yml`) with the following content:

		```yaml
		name: Ensure Advanced PR Templates
		on:
			workflow_dispatch:
			push:
				branches: [main]
			schedule:
				- cron: '0 3 * * 1'
		jobs:
			ensure-pr-templates-advanced:
				runs-on: ubuntu-latest
				steps:
					- uses: actions/checkout@v4
					- name: Set up Python
						uses: actions/setup-python@v5
						with:
							python-version: '3.x'
					- uses: ./.github/actions/ensure-pr-templates-advanced
						with:
							templates: |
								- name: feature.md
									content: |
										# Feature Pull Request
										...
								- name: bugfix.md
									content: |
										# Bugfix Pull Request
										...
							overwrite: 'true'
							inject-date: 'true'
							inject-author: 'true'
		```
3. Set the inputs as needed for your project.
4. Commit and push. The workflow will ensure all specified PR templates are present and up to date.

### Customization

- Add more templates by extending the `templates` input.
- Use `{{DATE}}` and `{{AUTHOR}}` in your template content for dynamic values.
- Set `overwrite` to `false` to skip updating existing templates.
- The action can be extended for more advanced validation or localization.

---
For questions or improvements, open an issue or pull request.
