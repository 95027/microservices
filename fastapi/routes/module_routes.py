from fastapi import APIRouter
from services import module_services
from schemas.modules import Query


router = APIRouter()

router = APIRouter(prefix="/v1", tags=["LLMS"])

@router.post("/text")
def read_text(query: Query):
    return module_services.read_text(query.input)

