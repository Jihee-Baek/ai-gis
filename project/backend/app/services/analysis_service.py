from typing import List
from app.schemas.analysis import AnalysisResult
from app.utils.spatial_utils import calculate_polygon_area

class SpatialAnalysisService:
    """
    공간 연산 유스케이스를 처리하는 서비스
    """
    def calculate_areas(self, geojson_data: dict) -> List[AnalysisResult]:
        """
        GeoJSON 데이터 내 폴리곤의 면적을 계산한다.
        """
        results = []
        features = geojson_data.get("features", [])

        for idx, feature in enumerate(features):
            geometry = feature.get("geometry")
            if not geometry:
                continue

            area_sqm = calculate_polygon_area(geometry)
            # 평 단위 변환 (1평 = 3.305785 제곱미터)
            area_pyung = area_sqm / 3.305785

            results.append(AnalysisResult(
                feature_index=idx,
                area_sqm=round(area_sqm, 2),
                area_pyung=round(area_pyung, 2),
                properties=feature.get("properties"),
                geometry_type=geometry.get("type")
            ))

        return results