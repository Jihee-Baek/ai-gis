from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.database.session import Base

class GeoFile(Base):
    """
    GeoJSON 파일 정보를 저장하는 데이터베이스 모델
    """
    __tablename__ = "geo_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)  # 서버 저장 파일명
    original_name = Column(String, nullable=False)                    # 원본 파일명
    file_size = Column(Integer)                                       # 파일 크기 (bytes)
    upload_time = Column(DateTime(timezone=True), server_default=func.now())
    file_path = Column(String, nullable=False)                        # 물리적 파일 경로