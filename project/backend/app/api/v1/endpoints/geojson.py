import json
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.ingestion_service import FileIngestionService
from app.services.analysis_service import SpatialAnalysisService
from app.schemas.geojson import GeoFileUploadResponse, GeoFileDetail

router = APIRouter()

@router.post("/upload", response_model=GeoFileUploadResponse)
async def upload_geojson(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    GeoJSON 파일 업로드 및 분석
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

@router.get("/{file_id}", response_model=GeoFileDetail)
async def get_geojson_detail(
    file_id: int,
    db: Session = Depends(get_db)
):
    """
    저장된 특정 GeoJSON 파일의 메타데이터 및 원본 데이터를 조회한다.
    """
    from app.repositories.geo_file_repository import GeoFileRepository
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