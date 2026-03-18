from fastapi import APIRouter, File, UploadFile,  Form
from services import module_services
from schemas.modules import Query

router = APIRouter(prefix="/v1", tags=["LLMS"])

@router.post("/text")
def read_text(query: Query):
    return module_services.read_text(query.input)

@router.post("/audio")
async def read_audio(file: UploadFile = File(...), prompt: str = Form(None)):
    audio_bytes  = await file.read()
    return module_services.read_audio(audio_bytes, prompt)

