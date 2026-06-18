import os
import uuid
import json
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.repositories.geo_file_repository import GeoFileRepository
from app.core.config import settings
from app.models.geo_file import GeoFile

class FileIngestionService:
    """
    파일 유효성 검사 및 저장을 담당하는 서비스
    각 업로드된 파일을 고유한 식별자와 함께 독립된 레이어로 분리하여 저장한다.
    """
    def __init__(self, db: Session):
        self.repository = GeoFileRepository(db)

    async def handle_upload(self, file: UploadFile) -> tuple[GeoFile, dict]:
        """
        파일을 수신하여 검증하고 저장소에 기록한다.
        """
        if not file.filename.endswith(('.geojson', '.json')):
            raise HTTPException(status_code=400, detail="GeoJSON 파일만 업로드 가능합니다.")

        content = await file.read()
        try:
            geojson_data = json.loads(content)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="유효하지 않은 JSON 형식입니다.")

        # 물리 파일 저장
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(settings.STORAGE_DIR, unique_filename)
        
        with open(file_path, "wb") as f:
            f.write(content)

        # DB 메타데이터 저장
        geo_file = self.repository.create({
            "filename": unique_filename,
            "original_name": file.filename,
            "file_size": len(content),
            "file_path": file_path
        })

        return geo_file, geojson_data
