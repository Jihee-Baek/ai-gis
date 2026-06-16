# Backend Structure Rules

## Core Rule

Generate a complete backend project structure.

The structure must be production-ready.

The structure must be scalable.

The structure must follow Clean Architecture.

---

## Required Layers

The following layers must exist.

- api
- service
- repository
- domain
- schemas
- database
- core

---

## File Responsibility Rule

Every file must have a single responsibility.

Do not combine multiple responsibilities into one file.

---

## Naming Convention

Use snake_case for filenames.

Examples:

- layer_router.py
- layer_service.py
- layer_repository.py

---

## GIS Rule

The system handles GeoJSON data.

The structure must support:

- GeoJSON Upload
- Layer Management
- Feature Query
- Area Analysis
- Geometry Validation

---

## Output Rule

Output must follow backend_structure.schema.json.

Output valid JSON only.

No markdown.

No explanations.