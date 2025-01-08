from pydantic import BaseModel
from datetime import datetime

class CodeBlockCreate(BaseModel):
    title: str
    description: str
    tags: str
    code: str

class CodeBlockResponse(BaseModel):  # Ensure this uses BaseModel
    id: int
    title: str
    description: str
    tags: str
    code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
