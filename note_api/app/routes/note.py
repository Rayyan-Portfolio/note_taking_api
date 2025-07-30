from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.note import NoteCreate, NoteOut, NoteUpdate
from app.db.session import get_db
from app.crud import note as note_crud

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return note_crud.create_note(db, note)

@router.get("/", response_model=List[NoteOut])
def read_all_notes(
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None, description="Search keyword in title or content"),
    tag: Optional[str] = Query(None, description="Filter notes by tag")
):
    return note_crud.get_all_notes(db, search=search, tag=tag)

@router.get("/{note_id}", response_model=NoteOut)
def read_note(note_id: int, db: Session = Depends(get_db)):
    note = note_crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_data: NoteUpdate, db: Session = Depends(get_db)):
    note = note_crud.update_note(db, note_id, note_data)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    success = note_crud.delete_note(db, note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}
