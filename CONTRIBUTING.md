# Contributing to AUS-Monorepo

Thank you for contributing to decentralized, sovereign infrastructure!

## Contribution Types

### 1. Protocol Design & Implementation
- New consensus algorithms or communication protocols
- Cryptographic primitives and proofs
- P2P networking improvements
- Message passing and sync algorithms

### 2. Agent Frameworks & Implementations
- Multi-agent coordination systems
- Autonomous system behaviors
- Agent decision-making frameworks
- Interaction protocols

### 3. Governance & Decision-Making
- DAO mechanisms and voting systems
- Distributed consensus approaches
- Resource allocation models
- Dispute resolution protocols

### 4. Infrastructure & Network
- Distributed storage solutions
- Compute network architectures
- Mesh network implementations
- Resilience & fault tolerance

### 5. Cryptography & Security
- Zero-knowledge proof systems
- Key management and signing schemes
- Privacy primitives
- Formal security verification

## Getting Started

1. **Fork the repository** (or branch if you have write access)
2. **Create a feature branch** with a descriptive name:
   ```bash
   git checkout -b protocol/algorithm-name
   git checkout -b agent/system-implementation
   git checkout -b governance/mechanism-name
   ```
3. **Make your changes** following the guidelines below
4. **Commit with clear messages**:
   ```
   Add: [Brief description]
   Ref: [Domain/issue/protocol affected]
   
   [Detailed explanation if needed]
   ```
5. **Submit a pull request** with:
   - Clear title describing the change
   - Link to any related issues
   - Summary of what changed and why

## Documentation Standards

### File Naming
- Use kebab-case: `protocol-name.md`
- Be descriptive: `byzantine-fault-tolerant-consensus.md`
- Avoid abbreviations unless widely established

### Structure
Every document should include:
```markdown
# Protocol/System Name

**Status**: Proposed | In Development | Stable | Deprecated
**Authors**: [Name(s)]
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

## Overview
Brief description of purpose, scope, and motivation.

## Problem Statement
What problem does this solve?

## Design Approach
Core design principles and architecture.

## Specification
Detailed technical specification or algorithm.

## Security Considerations
Known limitations, threat model, security properties.

## Implementation
Reference implementation or guidance.

## Related Protocols
- [[protocol-name]]
- [[another-protocol]]
```

### Formatting Rules
- Use `#` for main heading (H1 only once per document)
- Use `##` for sections, `###` for subsections
- Link to other documents: `[[document-name]]`
- Use code blocks for formal specifications
- Include diagrams for complex systems (ASCII art or SVG)
- Keep descriptions concise and technical

### Metadata
Include at the top of documents:
```yaml
---
type: protocol | agent-framework | governance-mechanism | infrastructure | cryptography
domain: core | agents | governance | infrastructure | protocols | cryptography | contracts
status: proposed | development | stable | deprecated
version: 1.0
---
```

## Implementation & Research Guidelines

### Protocol Development
- Include formal specification (pseudocode or detailed description)
- Provide security analysis (threat model, assumptions)
- Reference relevant literature and prior work
- Include test vectors or example executions
- Document known limitations

### Agent Framework Design
- Specify agent capabilities and decision model
- Define interaction protocols with other agents
- Include examples of agent behavior
- Document learning or adaptation mechanisms
- Provide simulation/testing framework

### Governance Mechanism Design
- Describe decision-making process
- Include participation and voting rules
- Analyze equilibrium properties
- Document failure modes and recovery
- Provide parameter tuning guidance

### Research & Analysis
- Include methodology and assumptions
- Provide reproducible results (seeds, configurations)
- Document data sources and collection methods
- Share analysis notebooks or scripts
- Interpret findings with appropriate caveats

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

- `protocol` — Protocol design or improvement
- `agent-framework` — Agent system or behavior
- `governance` — Governance mechanism or voting
- `infrastructure` — Network, storage, or compute
- `cryptography` — Security, proofs, or primitives
- `documentation` — Docs and specifications
- `research` — Research questions or analysis
- `question` — Question or discussion
- `good-first-issue` — Good for new contributors
- `breaking-change` — API or protocol breaking change

## Code of Conduct

All contributors must adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md). We expect:
- Respectful, professional technical discussion
- Focus on improving system resilience and decentralization
- Openness to alternative designs and approaches
- Honest reporting of limitations and failures

## Questions?

- **Technical Questions**: Use GitHub Discussions or Issues
- **Design Review**: Open an issue and tag [@maintainers](./MAINTAINERS.md)
- **Security Concerns**: See [SECURITY.md](./SECURITY.md)
- **Governance**: Participate in community governance processes

---

Thank you for helping build resilient, decentralized infrastructure!
