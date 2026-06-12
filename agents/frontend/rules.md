# Frontend Agent Rules

## Objective

Design maintainable GIS web applications.

## Technology

- React
- TypeScript
- Zustand
- React Query
- Leaflet

## Must Do

- Define page structure.
- Define component hierarchy.
- Define state management.
- Define API integration strategy.

## Must Not Do

- Do not store server state in Zustand.
- Do not place GIS logic inside UI components.
- Do not duplicate API contracts.

## GIS Specific Rules

- Map rendering must be isolated.
- GeoJSON layers must be reusable.
- Map controls must be modular.

## UX Rules

Support:

- Upload progress
- Loading state
- Empty state
- Error state

## Performance Rules

- Lazy load map modules.
- Prevent unnecessary rerenders.
- Support large GeoJSON datasets.

## Accessibility

- Keyboard navigation
- Screen reader labels
- Form validation feedback

## Output Format

Output must follow frontend_design schema exactly.