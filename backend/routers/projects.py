from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def list_projects():
    return [{"id": 1, "title": "PAPI"}]