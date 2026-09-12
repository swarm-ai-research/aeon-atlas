# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in AUS-Monorepo, please report it responsibly:

**Do not** open a public GitHub issue for security vulnerabilities.

Instead:

1. **Email** security@aus-monorepo.dev (or submit via GitHub security advisory)
   - Subject: `SECURITY: [Brief description]`
   - Include: vulnerability details, impact, affected components, reproduction steps

2. **What to expect**:
   - Acknowledgment within 24 hours
   - Technical assessment within 1 week
   - Regular updates on progress
   - Coordinated disclosure timeline (typically 90 days)

3. **Confidentiality**:
   - Your report is handled confidentially
   - Your identity is protected unless you consent to disclosure
   - Credit for discovery will be offered if desired

## Supported Versions

| Version | Status | Support Until |
|---------|--------|----------------|
| 1.0+ | Active | Current + 12 months |
| 0.9 | Security fixes only | 2026-12-31 |
| < 0.9 | Unsupported | — |

Critical security patches are released immediately when available. Non-critical updates follow the monthly release cycle.

## Security Considerations

### For Contributors
- **No secrets in code**: Never commit API keys, private keys, or credentials
- **Use environment variables**: Store secrets in .env or local config, never in version control
- **Code review first**: Review your diffs for unintended data exposure before pushing
- **Cryptographic rigor**: Ensure cryptographic implementations follow specs precisely
- **Security assumptions**: Document threat models and security assumptions in designs
- **Report issues promptly**: If you discover a vulnerability, report via security channel

### For Stewards
- **Cryptographic review**: All crypto code undergoes formal security review
- **Dependency audit**: Security patches applied within 48 hours
- **Design review**: Major protocol changes require security analysis
- **Transparent disclosure**: Security issues are disclosed responsibly with timelines
- **Audit preparation**: Be ready for external security audits

### For Users & Implementers
- **This is research code**: Use caution before deploying to production without audit
- **Verify cryptographic properties**: Don't assume implementations are secure
- **Review threat model**: Understand assumptions made by each protocol
- **Report findings**: Share security research and findings with the community

## Cryptographic Standards

- **Formal specifications**: All protocols have detailed, auditable specifications
- **Reference implementations**: Include test vectors and reference code
- **Security proofs**: Where applicable, include formal security analysis
- **Peer review**: Major protocols undergo community security review
- **Responsible disclosure**: Vulnerabilities are handled confidentially before public disclosure

## Dependencies & Supply Chain

- **Dependency scanning**: Enabled on all commits
- **License compliance**: All code uses compatible licenses
- **Minimal dependencies**: We keep external dependencies to a minimum
- **Update policy**: Security patches applied within 48 hours

## Development Security

- **Public access**: Code and discussions are public
- **Pull request review**: All changes reviewed before merge
- **Steward approval**: Sensitive changes (cryptography, consensus) require steward review
- **Branch protection**: Main branch requires passing checks and reviews
- **Audit trail**: All changes are logged and attributable

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
- **Email**: security@aus-monorepo.dev
- **Discussions**: Use GitHub Discussions with `[SECURITY]` tag
- **Stewards**: Contact the cryptography steward in the maintainers list

---

**Last Updated**: 2026-09-12
**Effective**: 2026-09-12

Thank you for helping build secure, trustworthy decentralized systems.
