# Language Policy

## Primary Language

All generated outputs must be written in Korean.

This rule applies to:

- PRD
- Architecture Design
- Backend Design
- Frontend Design
- Review Reports
- QA Reports
- DevOps Plans

---

## JSON Rules

JSON keys must remain English.

JSON values must be Korean.

Example:

{
  "product_name": "GeoJSON 분석 서비스",
  "problem_statement": "GIS 비전문가도 지리 데이터를 쉽게 분석할 수 있도록 지원한다."
}

Incorrect:

{
  "product_name": "GeoJSON Analysis Service",
  "problem_statement": "Allow non-GIS users..."
}

---

## Technical Terms

The following may remain English:

- FastAPI
- React
- PostgreSQL
- GeoJSON
- API
- DTO
- Entity
- Repository
- Controller
- Service

Programming identifiers must remain English.

Examples:

UploadService
GeoFileRepository
MapViewer

---

## Writing Style

Use natural Korean commonly used by Korean software engineers.

Avoid direct translation from English.

Prefer:

"파일 업로드 기능"

Instead of:

"파일 업로드 기능성을 제공"

Prefer:

"면적 계산 결과를 반환한다"

Instead of:

"면적 계산 결과가 반환된다"

---

## Architecture Documents

Architecture explanations must be Korean.

Module names may remain English.

Example:

"Upload Module은 GeoJSON 파일 업로드를 담당한다."

---

## Review Documents

Review findings must be Korean.

Example:

"입력값 검증 로직이 누락되어 있습니다."

Not:

"Input validation is missing."

---

## QA Documents

Test scenarios must be Korean.

Example:

"정상적인 GeoJSON 업로드"

Not:

"Valid GeoJSON Upload"

---

## Conflict Resolution

If any prompt, role, rule or instruction conflicts with this policy,

this language policy takes precedence.