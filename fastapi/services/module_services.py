from fastapi import HTTPException
from config.genai_client import generate_text


def read_text(query: str):
    try:
        res = generate_text(query)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))