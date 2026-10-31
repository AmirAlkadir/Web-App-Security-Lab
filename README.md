
# Web Application Penetration Testing & Security Automation Lab

## Overview

A hands-on cybersecurity portfolio project focused on identifying, validating, and documenting vulnerabilities in OWASP Juice Shop, an intentionally vulnerable web application deployed locally using Docker.

The project combines manual penetration testing with Python security automation, vulnerability reporting, and secure coding demonstrations.

## Technologies Used

- OWASP Juice Shop
- Burp Suite Community Edition
- Docker
- Python 3.13
- Requests
- SQLite / SQL
- JavaScript and HTML
- Git and GitHub

## Security Findings

| ID | Vulnerability | Severity | Result |
|---|---|---|---|
| 001 | SQL Injection | High (provisional) | Confirmed |
| 002 | Cross-Site Scripting (XSS) | Medium (provisional) | Tested; see report for validation |
| 003 | Broken Access Control (IDOR) | High (provisional) | Confirmed |

Testing was performed against a locally hosted, intentionally vulnerable application.

## Python Security Automation

Developed Python scripts to:

- Send HTTP requests to Juice Shop API endpoints.
- Automate product searches and input validation tests.
- Identify unusual HTTP responses and server errors.
- Export security test results to CSV.

Scripts are located in the `scripts/` directory.

## Vulnerability Remediation

Developed separate secure coding demonstrations:

- **SQL Injection:** Parameterized queries prevent SQL statement manipulation.
- **XSS:** `textContent` safely renders untrusted text instead of executing it as HTML.
- **IDOR:** Server-side ownership checks prevent unauthorized basket access.

These are independent remediation demonstrations. The original Juice Shop application was not patched.

## Regression Testing

Created Python unittest checks to validate expected results from the SQL injection and IDOR remediation demonstrations.

Run tests:

```powershell
python -m unittest discover -s tests -v
```

Result: 2 tests passed.

## Repository Structure

- `scripts/` — Python security automation
- `remediation/` — Secure coding demonstrations
- `reports/` — Vulnerability reports and CSV results
- `screenshots/` — Redacted testing evidence
- `tests/` — Automated regression tests

## Key Learning Outcomes

- HTTP request interception and manipulation
- API reconnaissance
- SQL injection testing and prevention
- Cross-site scripting and safe DOM manipulation
- Authentication and authorization testing
- Python HTTP automation
- Security regression testing
- Technical vulnerability reporting

## Ethical Testing Disclaimer

All penetration testing was performed against a locally hosted OWASP Juice Shop environment and personally controlled test accounts.

No unauthorized third-party systems were targeted.
