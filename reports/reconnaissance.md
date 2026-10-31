    
# Web Application Reconnaissance Report

## Target
OWASP Juice Shop (Local Docker Environment)

URL: http://localhost:3000

## Tools
- Burp Suite Community Edition
- Docker
- Web Browser

## Identified Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /rest/products/search?q= | Product search |
| GET | /rest/products/1/reviews | Retrieve product reviews |
| GET | /rest/user/whoami?fields=email | Retrieve user identity information |
| GET | /rest/languages | Retrieve available languages |

## Observations
- Product searches accept user-controlled query parameters.
- API responses contain structured JSON data.
- Product reviews are accessible through REST endpoints.
- HTTP responses include status codes such as 200 and 304.

## Potential Security Testing Areas
- SQL injection in search parameters
- Cross-site scripting (XSS)
- Authentication and authorization
- Input validation

## Status
Initial reconnaissance completed. No vulnerabilities confirmed yet.
