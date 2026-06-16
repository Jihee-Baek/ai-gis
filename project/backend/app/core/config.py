from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """
    BaseSettings를 상속받아 환경 변수 및 앱 설정을 정의한다.
    """
    PROJECT_NAME: str = "GIS Insight Viewer"
    API_V1_STR: str = "/api/v1"
    
    # 데이터베이스 설정
    DATABASE_URL: str = "postgresql://postgres:1234@127.0.0.1:5432/postgres?client_encoding=utf8"
    
    # 파일 저장 경로
    STORAGE_DIR: str = "storage/geojson"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# 저장소 디렉토리 생성
os.makedirs(settings.STORAGE_DIR, exist_ok=True)