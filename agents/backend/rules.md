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
* **Minimal Refactoring Policy**: 기존 백엔드 설계가 제공될 경우, 기능 추가에 필수적이지 않은 리팩토링이나 명칭 변경(Renaming)을 엄격히 제한합니다. 작동하는 기존 설계를 최대한 보존하세요.

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
