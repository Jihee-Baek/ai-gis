import json
import os
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.ingestion_service import FileIngestionService
from app.services.analysis_service import SpatialAnalysisService
from app.repositories.geo_file_repository import GeoFileRepository
from app.schemas.geojson import GeoFileUploadResponse, GeoFileDetail, GeoFileListItem, MessageResponse

router = APIRouter()

@router.post("/upload", response_model=GeoFileUploadResponse)
async def upload_geojson(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    GeoJSON 파일 업로드 및 분석
    새로운 레이어를 추가하기 위해 GeoJSON 파일을 업로드하고 분석 결과를 반환합니다.
    """
    ingestion_service = FileIngestionService(db)
    analysis_service = SpatialAnalysisService()

    # 파일 저장
    geo_file, geojson_data = await ingestion_service.handle_upload(file)

    # 공간 분석 수행
    analysis_results = analysis_service.calculate_areas(geojson_data)

    return GeoFileUploadResponse(
        id=geo_file.id,
        filename=geo_file.filename,
        original_name=geo_file.original_name,
        upload_time=geo_file.upload_time,
        analysis_results=analysis_results
    )

@router.get("/", response_model=List[GeoFileListItem])
async def list_geojson_files(
    db: Session = Depends(get_db)
):
    """
    레이어 목록 조회
    사이드바에 표시될 모든 업로드된 레이어 목록을 조회합니다.
    고유한 id를 반환하여 프론트엔드에서 레이어의 독립적인 가시성을 제어할 수 있게 합니다.
    """
    repository = GeoFileRepository(db)
    geo_files = repository.list_all()
    
    return [
        GeoFileListItem(
            id=gf.id,
            original_name=gf.original_name,
            file_size=gf.file_size,
            upload_time=gf.upload_time
        ) for gf in geo_files
    ]

@router.get("/{file_id}", response_model=GeoFileDetail)
async def get_geojson_detail(
    file_id: int,
    db: Session = Depends(get_db)
):
    """
    저장된 특정 GeoJSON 파일의 메타데이터 및 원본 데이터를 조회합니다.
    """
    repository = GeoFileRepository(db)
    
    geo_file = repository.get_by_id(file_id)
    if not geo_file:
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")

    # 물리 파일 읽기
    try:
        with open(geo_file.file_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)
    except Exception:
        raise HTTPException(status_code=500, detail="파일을 읽는 중 오류가 발생했습니다.")

    return GeoFileDetail(
        id=geo_file.id,
        original_name=geo_file.original_name,
        file_size=geo_file.file_size,
        upload_time=geo_file.upload_time,
        geojson_data=geojson_data
    )

@router.delete("/{file_id}", response_model=MessageResponse)
async def delete_geojson_file(
    file_id: int,
    db: Session = Depends(get_db)
):
    """
    레이어 삭제
    특정 레이어를 시스템에서 완전히 삭제합니다.
    """
    repository = GeoFileRepository(db)
    geo_file = repository.get_by_id(file_id)
    
    if not geo_file:
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")
        
    # 물리 파일 삭제
    if os.path.exists(geo_file.file_path):
        try:
            os.remove(geo_file.file_path)
        except Exception:
            pass
            
    success = repository.delete(file_id)
    if not success:
        raise HTTPException(status_code=500, detail="데이터베이스에서 삭제하는 데 실패했습니다.")
        
    return MessageResponse(message="레이어가 성공적으로 삭제되었습니다.")
