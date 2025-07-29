from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import tag as tag_crud
from app.schemas.tag import TagOut

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/", response_model=List[TagOut])
def list_tags(db: Session = Depends(get_db)):
    return tag_crud.get_all_tags(db)
