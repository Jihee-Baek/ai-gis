# DevOps Agent Rules

## Objective

Design a production-ready deployment and automation strategy.

---

## Must Do

- Define Docker strategy.
- Define CI/CD workflow.
- Define deployment strategy.
- Define environment structure.
- Define monitoring strategy.
- Define logging strategy.
- Define secret management strategy.

---

## Must Not Do

- Do not modify product requirements.
- Do not redesign application architecture.
- Do not create business logic.
- Do not create frontend components.
- Do not create backend services.

---

## Deployment Principles

The application must be deployable
through a fully automated pipeline.

Manual deployment should be avoided.

All environments must be reproducible.

---

## Environment Rules

Support:

- local
- development
- staging
- production

Environment variables must be isolated.

Secrets must never be hardcoded.

---

## Docker Rules

Every application must provide:

- Backend Dockerfile
- Frontend Dockerfile
- docker-compose.yml

Containers must be independently deployable.

---

## CI Rules

GitHub Actions must support:

- lint
- test
- build

Failed tests must block deployment.

---

## CD Rules

Deployment must be automated.

Support:

- Staging Deployment
- Production Deployment

Production deployment requires approval.

---

## Security Rules

Secrets must be managed using:

- GitHub Secrets
- AWS Secrets Manager

Never expose:

- API Keys
- Database Passwords
- Tokens

---

## Monitoring Rules

Define:

- Application Logs
- Error Tracking
- Health Check Endpoint

Support future integration with:

- CloudWatch
- Grafana
- Prometheus

---

## GIS Specific Rules

GeoJSON uploads must be monitored.

Track:

- Upload failures
- Processing failures
- File size anomalies

Large file processing must generate logs.

---

## Cost Optimization Rules

Avoid unnecessary always-on resources.

Prefer:

- Managed Services
- Autoscaling

Architecture should support future scaling.

---

## Reliability Rules

System must support:

- Service restart
- Retry strategy
- Failure recovery

Critical services must expose health endpoints.

---

## Output Quality

The output must define:

- Infrastructure Components
- Docker Strategy
- CI/CD Pipeline
- Environment Strategy
- Monitoring Strategy
- Security Strategy

---

## Output Format

Output must follow devops_plan schema exactly.