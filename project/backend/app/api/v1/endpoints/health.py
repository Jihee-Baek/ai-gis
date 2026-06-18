from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def check_health():
    """
    시스템 가동 상태를 확인한다.
    """
    return {"status": "ok", "message": "GIS Insight Viewer Backend is running"}
