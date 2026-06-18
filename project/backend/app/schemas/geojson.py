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

class GeoFileListItem(BaseModel):
    """
    레이어 목록 조회를 위한 간략한 파일 정보 스키마
    프론트엔드에서 각 레이어를 고유하게 구분하고 독립적으로 가시성을 관리하기 위한 식별자(id) 제공.
    """
    id: int
    original_name: str
    file_size: int
    upload_time: datetime
    
    class Config:
        from_attributes = True

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

class MessageResponse(BaseModel):
    """
    일반적인 결과 메시지를 위한 응답 스키마
    """
    message: str
