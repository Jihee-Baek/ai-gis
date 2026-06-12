# Rules
Technology
- React
- TypeScript
- Vite
- Zustand
- React Query

Architecture
- Feature Based Structure
- Reusable Components
- Separation of Concerns
- Avoid Business Logic in Components

Component Rules
- One responsibility per component
- Props must be strongly typed
- Avoid prop drilling
- Prefer composition over inheritance

State Management

Use local state when possible.
Use Zustand only for shared application state.
Use React Query for server state.
Do not duplicate backend data in Zustand.

API Integration

All API communication must be isolated.

Use custom hooks.
Example:
- useUploadGeoJson
- useMapData
- useAnalysisResult

GIS Rules

Leaflet is the default map engine.

Map rendering logic must be separated from UI components.

GeoJSON rendering must be reusable.

Support future migration to:

- MapLibre
- Cesium
- Three.js

Performance

Avoid unnecessary re-renders.
Use memoization only when needed.
Lazy load large GIS modules.
Support large GeoJSON datasets.

Accessibility

All buttons require labels.
All forms require validation.
Keyboard navigation must be supported.

Error Handling

API failures must show user-friendly messages.
Loading state is required.
Empty state is required.

Testing

Test:
- Components
- Hooks
- User interactions

Prefer React Testing Library.

Deliverables

Frontend Agent must provide:
- Folder Structure
- Component Structure
- State Design
- API Integration Design
- UI Flow