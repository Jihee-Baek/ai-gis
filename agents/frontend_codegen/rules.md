# Frontend Code Generation Rules

## Core Rule

Generate production-ready React source code.

Generate complete file contents.

Do not generate pseudo code.

Do not generate placeholders.

---

## Technology Stack

Framework:

* React
* TypeScript
* Vite

State Management:

* Zustand

Server State:

* React Query

Map Engine:

* Leaflet

---

## Architecture Rule

Follow frontend_structure.json exactly.

Do not create additional files unless required.

Do not change file paths.

Do not change responsibilities.

---

## React Rule

Use Functional Components only.

Use React Hooks.

Avoid Class Components.

Use TypeScript strict typing.

---

## Component Rule

Every component must:

* Have a single responsibility
* Use typed props
* Export default component

Use React.memo when beneficial.

---

## Hook Rule

Every custom hook must:

* Start with use
* Encapsulate business logic
* Be reusable

Examples:

* useLayers
* useUploadLayer
* useAreaAnalysis

---

## Zustand Rule

Stores must:

* Use create()
* Define state types
* Define action types
* Separate state and actions clearly

---

## React Query Rule

Use:

* useQuery
* useMutation

Define queryKey explicitly.

Handle loading state.

Handle error state.

---

## API Rule

Use service layer abstraction.

Components must not call fetch directly.

Components must not call axios directly.

API communication must be delegated to services.

---

## Leaflet Rule

Map components must:

* Initialize map safely
* Cleanup event handlers
* Prevent memory leaks

Support:

* GeoJSON Layer Rendering
* Feature Selection
* Popup Rendering
* Layer Visibility Toggle

---

## TypeScript Rule

Avoid any.

Use explicit types.

Prefer interfaces for component props.

Prefer type aliases for unions.

---

## Code Quality Rule

Follow:

* SOLID
* DRY
* KISS

Avoid duplicated logic.

Avoid deeply nested components.

---

## Output Rule

Output must follow frontend_codegen.schema.json.

Output valid JSON only.

No markdown.

No explanations.

Every file must contain complete source code.
