## [v1.2.0] - 2026-06-18
### 변경 사항
- 구현된 API 목록
  - `GET /health`: 시스템 가동 상태 확인
  - `POST /api/v1/geojson/upload`: GeoJSON 파일 업로드, PostGIS 저장 및 공간 분석(면적 계산) 수행
  - `GET /api/v1/geojson/{file_id}`: 특정 GeoJSON 파일의 메타데이터 및 분석 결과가 포함된 데이터 조회

- DB 스키마 변경 사항
  - `geo_files`: 업로드된 GeoJSON 파일의 메타데이터(파일명, 경로, 크기 등) 저장
  - `geo_features`: PostGIS를 활용한 개별 지리 피처(Geometry), 속성(JSONB), 계산된 면적 정보 저장

- 프론트엔드 주요 변경 사항
  - `MapContainer`: Leaflet 기반의 대화형 지도 시각화 및 레이어 렌더링
  - `FileUploader`: GeoJSON 파일 드래그 앤 드롭 업로드 및 분석 상태 표시
  - `LayerSidebar`: 업로드된 레이어 목록 관리 및 독립적인 가시성(표시/숨김) 제어
  - `PropertyInspector`: 지도에서 선택된 피처의 상세 속성 및 분석 결과 표시
  - `AnalysisCard`: 폴리곤 면적(제곱미터 및 평 단위) 분석 결과 요약
  - `LoadingOverlay`: 파일 업로드 및 서버 분석 중 사용자 피드백 제공

- 기타 특이 사항
  - 설계(Architecture/PRD)에 정의된 핵심 기능 충실히 구현
  - PostGIS 활용 공간 데이터 저장 및 GIST 인덱스 최적화 적용
  - Zustand를 이용한 레이어별 독립적 상태 관리 및 TanStack Query 비동기 통신 구조 확립
  - 분석 서비스 내 ㎡와 평 단위 동시 계산 및 반환 로직 구체화
