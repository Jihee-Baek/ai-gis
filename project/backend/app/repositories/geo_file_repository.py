from sqlalchemy.orm import Session
from app.models.geo_file import GeoFile
from typing import Optional, List

class GeoFileRepository:
    """
    GeoFile 데이터 접근 로직을 담당하는 클래스
    """
    def __init__(self, db: Session):
        self.db = db

    def create(self, geo_file_data: dict) -> GeoFile:
        db_obj = GeoFile(**geo_file_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_by_id(self, file_id: int) -> Optional[GeoFile]:
        return self.db.query(GeoFile).filter(GeoFile.id == file_id).first()

    def list_all(self) -> List[GeoFile]:
        return self.db.query(GeoFile).order_by(GeoFile.upload_time.desc()).all()

    def delete(self, file_id: int) -> bool:
        db_obj = self.get_by_id(file_id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False
