-- PostGIS 확장 활성화
CREATE EXTENSION IF NOT EXISTS postgis;

-- GeoJSON 파일 메타데이터 테이블
CREATE TABLE IF NOT EXISTS geo_files (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    original_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    upload_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 개별 지리 피처 및 공간 데이터 테이블
CREATE TABLE IF NOT EXISTS geo_features (
    id SERIAL PRIMARY KEY,
    file_id INTEGER NOT NULL REFERENCES geo_files(id) ON DELETE CASCADE,
    geometry GEOMETRY(GEOMETRY, 4326) NOT NULL, -- WGS84 좌표계 사용
    properties JSONB NOT NULL, -- 피처의 상세 속성 키-값 데이터
    calculated_area FLOAT, -- 계산된 면적 값 (m²)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 공간 쿼리 성능 최적화를 위한 GIST 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_geo_features_geometry ON geo_features USING GIST (geometry);

-- 파일 ID 기반 조회를 위한 인덱스
CREATE INDEX IF NOT EXISTS idx_geo_features_file_id ON geo_features (file_id);

-- 속성 데이터 검색 최적화를 위한 JSONB GIN 인덱스
CREATE INDEX IF NOT EXISTS idx_geo_features_properties ON geo_features USING GIN (properties);
