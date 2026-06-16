from pydantic import BaseModel
from typing import Optional, Any

class AnalysisResult(BaseModel):
    """
    개별 지리 객체에 대한 분석 결과 스키마
    """
    feature_index: int
    area_sqm: float           # 제곱미터 단위 면적
    area_pyung: float         # 평 단위 면적
    properties: Optional[dict] = None
    geometry_type: str