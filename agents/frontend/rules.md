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
- **Minimal Refactoring Policy**: 기존 프론트엔드 설계가 제공될 경우, 새로운 기능 추가를 위해 불가피한 경우를 제외하고는 컴포넌트 구조나 상태 관리 방식을 변경하지 마세요.

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