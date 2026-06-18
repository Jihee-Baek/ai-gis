# Frontend Structure Rules

## Core Rule

Generate a complete frontend project structure.

The structure must be production-ready.

The structure must be scalable.

The structure must follow Feature-Based Architecture.

---

## Required Folders

The following folders must exist.

* src/pages
* src/components
* src/features
* src/hooks
* src/services
* src/stores
* src/types
* src/routes
* src/layouts
* src/utils

---

## State Management Rule

Use Zustand for client-side state.

Use React Query for server-state management.

Do not duplicate responsibilities.

---

## GIS Rule

The application handles GeoJSON visualization.

The structure must support:

* GeoJSON Upload
* Layer Management
* Feature Selection
* Feature Popup
* Area Analysis
* Attribute Table
* Map Visualization

---

## React Rule

Use React Functional Components.

Use TypeScript.

Use Custom Hooks.

Use Component Reusability.

---

## File Responsibility Rule

Every file must have a single responsibility.

Do not combine unrelated responsibilities.

---

## Naming Convention

Use PascalCase for React Components.

Examples:

* MapContainer.tsx
* LayerPanel.tsx
* FeaturePopup.tsx

Use camelCase for hooks.

Examples:

* useLayers.ts
* useUploadLayer.ts

Use camelCase for stores.

Examples:

* authStore.ts
* mapStore.ts

---

## Route Rule

Every page must have a route definition.

Route ownership must be explicitly defined.

---

## Component Rule

Each page must define:

* owned components
* shared components
* dependencies

---

## Minimal Refactoring Policy

* 기존 프론트엔드 구조(# Existing Frontend Structure)가 제공될 경우, 이를 원형 그대로 유지하는 것을 원칙으로 합니다.
* 이미 정의된 파일 경로, 컴포넌트 명칭, 훅의 사용처 등을 사용자의 명시적 요청 없이 수정하지 마세요.

---

## Output Rule

Output must follow frontend_structure.schema.json.

Output valid JSON only.

No markdown.

No explanations.
