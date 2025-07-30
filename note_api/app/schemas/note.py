from typing import List, Optional
from pydantic import BaseModel
from app.schemas.tag import TagOut

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    tags: List[str] 

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None

class NoteOut(NoteBase):
    id: int
    tags: List[TagOut]

    model_config = {
        "from_attributes": True
    }