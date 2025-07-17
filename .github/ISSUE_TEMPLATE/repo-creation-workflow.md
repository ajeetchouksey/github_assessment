---
name: "Repo Creation Workflow"
about: "Tracks the main repo-creation task and its sub-issues"
title: "🔧 Repo Creation Workflow – [short description]"
labels:
  - automation
  - workflow
---

Use this template to break down the {{issue.title}} work into discrete sub-issues.

**Sub-issues:**
- [ ] Parent issue: #1 Automate repository creation via GitHub Actions
- [ ] #1.1 Define and validate workflow inputs (repo_name, description, visibility)
- [ ] #1.2 Implement the “create repo” logic (GitHub REST API or gh CLI)
- [ ] #1.3 Initialize default files (README, .gitignore, LICENSE)
- [ ] #1.4 Apply branch protection, labels, and topics via a settings action
- [ ] #1.5 Secure and scope the token (secret management, least-privilege scopes)
- [ ] #1.6 End-to-end testing and documentation
