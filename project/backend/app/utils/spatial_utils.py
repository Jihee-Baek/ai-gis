import pyproj
from shapely.geometry import shape

def calculate_polygon_area(geometry: dict) -> float:
    """
    단일 폴리곤 객체의 지표면 면적을 계산한다 (제곱미터 단위).
    WGS84 타원체(Geod)를 사용하여 정확한 면적을 산출한다.
    """
    try:
        geom = shape(geometry)
        if geom.geom_type not in ['Polygon', 'MultiPolygon']:
            return 0.0
            
        # WGS84 타원체 기반 면적 계산
        geod = pyproj.Geod(ellps="WGS84")
        area, _ = geod.geometry_area_perimeter(geom)
        
        # 결과는 항상 양수
        return abs(area)
    except Exception:
        return 0.0
