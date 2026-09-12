# Standards & Guidelines

This directory contains technical and organizational standards for consistency across government administration.

## Standards Categories

- **Documentation Standards** — Format, structure, metadata
- **Data Standards** — Formats, schemas, quality
- **Accessibility Standards** — WCAG 2.1, inclusive design
- **Security Standards** — Information security practices
- **Interoperability Standards** — System integration, APIs
- **Terminology Standards** — Consistent terminology across agencies

## Core Standards

### 1. Documentation Standards
See: `documentation-standard.md`

**Key Points:**
- Use Markdown for text
- Include metadata (date, author, status)
- Follow wiki-link conventions
- Maintain change logs
- Ensure plain language readiness

### 2. Data Standards
See: `data-standard.md`

**Key Points:**
- CSV for tabular data
- JSON for structured data
- Include data dictionaries
- Use ISO 8601 for dates
- Document encoding (UTF-8)

### 3. Accessibility Standards
See: `accessibility-standard.md`

**Key Points:**
- WCAG 2.1 Level AA compliance
- Alt text for images
- Semantic HTML structure
- Color contrast ratios
- Keyboard navigation support

### 4. Naming Conventions
See: `naming-conventions.md`

**Key Points:**
- Files: kebab-case (my-document-name)
- Folders: kebab-case (my-folder-name)
- Variables: snake_case (my_variable)
- Classes: PascalCase (MyClass)
- Constants: UPPER_SNAKE_CASE (MY_CONSTANT)

## Standard Template

```markdown
# Standard Title

**Category**: [Category]
**Effective Date**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Applies To**: [Scope]
**Compliance Level**: Mandatory | Recommended | Optional

## Purpose
Why this standard exists.

## Scope
What and who it applies to.

## Requirements
Detailed requirements, organized by section.

### Requirement 1
Description with examples.

### Requirement 2
Description with examples.

## Compliance
How compliance is verified.

## Exceptions
When the standard doesn't apply.

## Related Standards
- [[Standard Name]]
- [[Standard Name]]

## Change History
| Date | Version | Change |
|------|---------|--------|
| YYYY-MM-DD | 1.0 | Initial version |
```

## Creating New Standards

1. **Identify need**: Gap in current standards
2. **Draft**: Create draft using template
3. **Consult**: Get feedback from affected teams
4. **Review**: Maintainers assess against existing standards
5. **Publish**: Merge and announce
6. **Monitor**: Review effectiveness after 6 months

## Compliance Checking

Standards are verified through:
- **Automated checks**: Linting, schema validation
- **Manual review**: Code/document review
- **Audits**: Periodic compliance audits
- **Feedback**: Issue reporting and escalation

## Support & Questions

For questions about standards:
- Check documentation in each standard file
- Open an issue with [STANDARD] label
- Contact standards maintainer

---

**Last Updated**: 2026-09-12
**Standards Version**: 1.0
