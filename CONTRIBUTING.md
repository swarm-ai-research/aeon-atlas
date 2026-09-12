# Contributing to Australia Administration

Thank you for contributing to Australian governance transparency and administration!

## Contribution Types

### 1. Documentation Updates
- Clarifying existing procedures
- Fixing outdated information
- Adding missing documentation
- Improving clarity and accessibility

### 2. New Department Records
- Adding agency information
- Documenting responsibilities
- Updating contact information
- Recording organizational changes

### 3. Policy & Procedure Additions
- New legislative frameworks
- Administrative procedure updates
- Process standardization
- Governance improvements

### 4. Data Contributions
- Public datasets and statistics
- Historical records
- Performance metrics
- Decision logs and transparency reports

### 5. Quality & Accessibility
- Improving formatting
- Adding missing metadata
- Accessibility enhancements
- Localization

## Getting Started

1. **Fork the repository** (or branch if you have write access)
2. **Create a feature branch** with a descriptive name:
   ```bash
   git checkout -b docs/department-xyz-update
   git checkout -b policy/new-framework-name
   git checkout -b data/dataset-addition
   ```
3. **Make your changes** following the guidelines below
4. **Commit with clear messages**:
   ```
   Add: [Brief description]
   Ref: [Issue/department/section affected]
   
   [Detailed explanation if needed]
   ```
5. **Submit a pull request** with:
   - Clear title describing the change
   - Link to any related issues
   - Summary of what changed and why

## Documentation Standards

### File Naming
- Use kebab-case: `my-department-name.md`
- Be descriptive: `federal-tax-collection-procedures.md`
- Avoid abbreviations unless official

### Structure
Every document should include:
```markdown
# Department/Policy Name

**Established**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Responsible**: [Department/Agency Name]

## Overview
Brief description of purpose and scope.

## Key Responsibilities
- Item 1
- Item 2

## Procedures
Step-by-step processes.

## Contact
- Department: [name]
- Email: [contact]
- Phone: [number]

## Related Documents
- [[document-name]]
- [[another-document]]
```

### Formatting Rules
- Use `#` for main heading (H1 only once per document)
- Use `##` for sections, `###` for subsections
- Link to other documents: `[[document-name]]`
- Use tables for structured data
- Keep paragraphs concise (max 3 sentences)

### Metadata
Include at the top of documents:
```yaml
---
date: 2026-09-12
category: procedures
department: [Department Name]
status: active | draft | archived
version: 1.0
---
```

## Data Contribution Guidelines

### Datasets
- Include a `README.md` explaining the dataset
- Provide data dictionary with field definitions
- Use standard formats (CSV, JSON, Parquet)
- Include data source and collection date
- Add update frequency information

### Decision Logs
- Record significant decisions
- Include date, decision, rationale
- Link to supporting documents
- Note outcomes and impacts
- Update when new information emerges

### Transparency Reports
- Quarterly or annual summaries
- Performance metrics aligned to objectives
- Public accountability measures
- Comparison to prior periods
- Clear accessibility notes

## Review Process

1. **Automated checks** run on all PRs:
   - Link validation
   - Markdown linting
   - File naming conventions
   - Metadata completeness

2. **Human review** by maintainers:
   - Accuracy verification
   - Consistency with existing content
   - Completeness assessment
   - Accessibility check

3. **Approval & Merge**:
   - Requires at least one maintainer approval
   - All checks must pass
   - Conflicts resolved collaboratively

## Issue Labels

- `documentation` — Documentation updates
- `department-records` — Department information
- `policy` — Policy and legislation
- `data` — Datasets and records
- `accessibility` — Accessibility improvements
- `question` — Question or clarification needed
- `good-first-issue` — Good for new contributors

## Code of Conduct

All contributors must adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md). We expect:
- Respectful, professional communication
- Focus on improving transparency
- Acknowledgment of different perspectives
- Good faith participation

## Questions?

- **Issues**: Use GitHub Issues for questions and discussions
- **Security concerns**: See [SECURITY.md](./SECURITY.md)
- **Process questions**: Contact [maintainers](./MAINTAINERS.md)

---

Thank you for helping build a more transparent Australian administration!
