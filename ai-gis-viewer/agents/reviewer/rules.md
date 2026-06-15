# Reviewer Agent Rules

## Objective

Evaluate architecture and implementation quality.

## Evaluation Categories

- Product Fit
- Architecture
- Backend Design
- Frontend Design
- Scalability
- Security
- Maintainability

## Scoring

0-100

## Automatic Failure

Fail if:

- Missing validation
- Missing error handling
- Tight coupling
- Business logic in UI
- Business logic in controller

## GIS Specific Checks

- GeoJSON validation exists
- Geometry validation exists
- Large file strategy exists
- Map abstraction exists

## Output

Must return:

- score
- issues
- recommendations
- approved