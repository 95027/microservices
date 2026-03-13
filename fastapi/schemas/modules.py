from pydantic import BaseModel

class Query(BaseModel):
    input: str