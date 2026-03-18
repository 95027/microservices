from fastapi import HTTPException
from config.genai_client import generate_text, generate_audio_text


def read_text(query: str):
    try:
        res = generate_text(query)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def read_audio(audio_bytes: bytes, prompt: str = None, mime_type: str = "audio/wav",):
    try:
        res = generate_audio_text(audio_bytes, prompt, mime_type)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))