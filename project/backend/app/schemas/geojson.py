from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Any
from app.schemas.analysis import AnalysisResult

class GeoFileUploadResponse(BaseModel):
    """
    파일 업로드 완료 후 반환되는 응답 스키마
    """
    id: int
    filename: str
    original_name: str
    upload_time: datetime
    analysis_results: List[AnalysisResult]

class GeoFileDetail(BaseModel):
    """
    저장된 GeoJSON 파일의 상세 정보를 위한 응답 스키마
    """
    id: int
    original_name: str
    file_size: int
    upload_time: datetime
    geojson_data: dict  # 원본 GeoJSON 데이터

    class Config:
        from_attributes = True