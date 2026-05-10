---
name: pci-compliance
description: |
  PCI DSS compliance guidance for payment data handling, storage, and transmission.
  Perfect for: compliance assessments, security architecture, audit preparation.
  Not ideal for: non-card payment methods, general application security.
---

# PCI DSS Compliance

## Core Philosophy
**"Protect cardholder data as if your business depends on it — because it does."**

## PCI DSS 4.0 Requirements Summary

### Requirement 1: Network Security Controls
- Install and maintain network security controls (firewalls, WAFs)
- Segment cardholder data environment (CDE) from other networks
- Restrict inbound/outbound traffic to only what's necessary

### Requirement 2: Secure Configurations
- Change all vendor-supplied defaults
- Remove unnecessary services, protocols, ports
- Document all security configurations

### Requirement 3: Protect Stored Account Data
- **Never store CVV/CVC after authorization**
- **Never store full track data after authorization**
- Encrypt stored PAN using AES-256 or stronger
- Mask PAN display (show only first 6 and last 4)
- Implement key management procedures

### Requirement 4: Encrypt Transmission
- TLS 1.2+ for all cardholder data transmission
- No SSL or early TLS
- Strong cipher suites only

### Requirement 5: Malware Protection
- Deploy anti-malware on all systems in CDE
- Keep definitions current
- Perform periodic scans

### Requirement 6: Secure Development
- Address common vulnerabilities (OWASP Top 10)
- Review custom code before release
- Protect web-facing applications (WAF or code review)

### Requirement 7: Restrict Access
- Limit access to cardholder data by business need-to-know
- Implement role-based access control
- Default deny for all access

### Requirement 8: Identify Users
- Unique ID for every person with computer access
- Multi-factor authentication for CDE access
- Strong password/passphrase policies

### Requirement 9: Physical Security
- Restrict physical access to CDE
- Secure media containing cardholder data
- Control access to sensitive areas

### Requirement 10: Logging & Monitoring
- Log all access to cardholder data
- Implement audit trails
- Review logs daily
- Retain logs for at least one year

### Requirement 11: Test Security
- Quarterly vulnerability scans (ASV)
- Annual penetration testing
- Intrusion detection/prevention
- File integrity monitoring

### Requirement 12: Security Policies
- Maintain information security policy
- Perform risk assessments annually
- Security awareness training
- Incident response plan

## SAQ (Self-Assessment Questionnaire) Types

| SAQ | Applies To | Scope |
|-----|-----------|-------|
| SAQ A | e-commerce, fully outsourced | Redirect or iframe — no cardholder data touches your servers |
| SAQ A-EP | e-commerce, partial outsource | Your page controls payment form but data goes to processor |
| SAQ B | Imprint/standalone terminal | No electronic cardholder data storage |
| SAQ C | Payment application internet | Connected terminal, no data storage |
| SAQ D | Everyone else | Full assessment (300+ controls) |

## Tokenization for Scope Reduction

Using tokenization reduces PCI scope:
- **Before**: Application servers, databases, logs, backups all in scope
- **After**: Only the token vault and checkout page in scope
- **Result**: SAQ D → SAQ A or SAQ A-EP

## Audit Readiness Checklist
1. Network diagrams current and showing CDE segmentation
2. Data flow diagrams showing cardholder data paths
3. Inventory of all systems touching cardholder data
4. Evidence of quarterly ASV scans (passing)
5. Evidence of annual penetration test
6. Log retention for 12 months (3 months immediately available)
7. Incident response plan tested within last year
8. All third-party service providers have current AOC/SAQ
