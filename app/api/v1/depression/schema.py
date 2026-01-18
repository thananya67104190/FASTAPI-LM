from pydantic import BaseModel

class DepressionRequest(BaseModel):
    query: str
    type: str
    top_k: int