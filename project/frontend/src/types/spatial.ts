import type { Feature, Geometry } from 'geojson';

/**
 * 서버에서 반환하는 공간 분석 결과 데이터 구조
 */
export interface SpatialAnalysisResult {
  id: number;
  filename: string;
  original_name: string;
  upload_time: string;
  analysis_results: Array<{
    feature_index: number;
    area_sqm: number;
    area_pyung: number;
    properties: Record<string, any>;
    geometry_type: string;
  }>;
}

/**
 * 지도 레이어의 메타데이터 및 상태 정보
 */
export interface LayerInfo {
  id: string;
  name: string;
  visible: boolean;
  data: any; // GeoJSON 데이터
  analysis?: SpatialAnalysisResult;
}

/**
 * GeoJSON Feature 타입 확장
 */
export type GeoJSONFeature = Feature<Geometry, Record<string, any>>;
