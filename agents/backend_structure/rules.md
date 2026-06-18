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

## Minimal Refactoring Policy

* 기존 프로젝트 구조(# Existing Backend Structure)가 제공될 경우, 이를 최우선으로 존중하세요.
* 이미 구현된 파일 경로나 클래스/함수 명칭은 절대 변경하지 마세요.
* 오직 새로운 기능에 필요한 파일 추가나, 기존 파일 내에서의 함수 추가만 허용합니다.

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