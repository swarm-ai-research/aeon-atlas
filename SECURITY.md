# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in Australia Administration, please report it responsibly:

**Do not** open a public GitHub issue for security vulnerabilities.

Instead:

1. **Email** [security@australia-admin.gov.au] (placeholder)
   - Subject: `SECURITY: [Brief description]`
   - Include: vulnerability details, impact, reproduction steps (if applicable)

2. **What to expect**:
   - Acknowledgment within 24 hours
   - Initial assessment within 1 week
   - Regular updates on progress
   - Coordinated disclosure timeline

3. **Confidentiality**:
   - Your report is confidential
   - We will not disclose your identity without permission
   - We will work with you on timing of any public disclosure

## Supported Versions

| Version | Status | Support Until |
|---------|--------|----------------|
| 1.0+ | Active | Current + 12 months |
| 0.9 | Security fixes only | 2026-12-31 |
| < 0.9 | Unsupported | — |

Critical security patches are released immediately when available. Non-critical updates follow the monthly release cycle.

## Security Considerations

### For Contributors
- Don't commit sensitive data (API keys, credentials, PII)
- Use environment variables for secrets
- Review diffs before committing
- Check for secrets in files before pushing
- Report suspicious activity immediately

### For Maintainers
- All access requires authentication
- Changes to governance files require review
- Sensitive data is never stored in the repository
- Branch protection rules are enforced
- Access logs are maintained and audited

### For Users
- This repository is public; treat accordingly
- Don't rely on it for operational security
- Always verify information from official sources
- Report inaccuracies and potential exploitation vectors

## Data Protection

- **Public data only**: This repository contains only public domain information
- **No personal information**: PII is never included (e.g., personal email addresses, phone numbers of individuals)
- **Minimal metadata**: Only publish necessary administrative information
- **Right to erasure**: Submit removal requests for any personal information discovered

## Dependencies & Supply Chain

- **Dependency scanning**: Enabled on all commits
- **License compliance**: All code uses compatible licenses
- **Minimal dependencies**: We keep external dependencies to a minimum
- **Update policy**: Security patches applied within 48 hours

## Access Control

- **Public read**: Anyone can read all content
- **Authenticated write**: Pull requests reviewed before merge
- **Maintainer approval**: All merges require maintainer review
- **Branch protection**: Main branch is protected

## Incident Response

In case of a security incident:

1. **Immediately notify** maintainers
2. **Do not discuss publicly** until addressed
3. **Provide details**:
   - What happened
   - When discovered
   - Scope and impact
   - Proposed fixes

4. **Response timeline**:
   - Critical: Fix within 24 hours
   - High: Fix within 1 week
   - Medium: Fix within 1 month
   - Low: Fix in next release

## Third-Party Services

This repository is hosted on GitHub. Please refer to [GitHub's Security Policy](https://github.com/security) for platform-level security information.

## Questions?

For security-related questions (non-vulnerability):
- Email: [security@australia-admin.gov.au]
- Issue tracker: Use "question" label with `[SECURITY]` prefix

---

**Last Updated**: 2026-09-12
**Effective**: 2026-09-12

Thank you for helping keep Australia Administration secure.
