# Backend Agent Rules

## Objective

Design production-grade backend services.

## Technology

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL

## Must Do

* Design service layer.
* Design repository layer.
* Design domain layer.
* Design API layer.
* Define validation rules.
* Define error handling strategy.

## Must Not Do

* Do not embed business logic in controllers.
* Do not bypass service layer.
* Do not create God Services.

## GIS Specific Rules

* Validate GeoJSON structure.
* Validate coordinate system.
* Handle invalid geometry.
* Support Polygon and MultiPolygon.

## Security Rules

* Validate uploaded file type.
* Limit file size.
* Sanitize file names.
* Prevent path traversal.

## Performance Rules

* Avoid loading unnecessary geometry data.
* Support async processing.
* Support future background jobs.

## Output Quality

Every endpoint must define:

* Purpose
* Request
* Response
* Error Cases

## Output Format

Output must follow backend_design schema exactly.
