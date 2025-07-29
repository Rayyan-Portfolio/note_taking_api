from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from app.models.note import Note
from app.models.tag import Tag
from app.models.association import note_tags
from app.schemas.note import NoteCreate, NoteUpdate
from app.crud.tag import get_or_create_tag

def create_note(db: Session, note_data: NoteCreate) -> Note:
    note = Note(title=note_data.title, content=note_data.content)
    # Attach tags
    for tag_name in note_data.tags:
        tag = get_or_create_tag(db, tag_name)
        note.tags.append(tag)

    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_note(db: Session, note_id: int) -> Optional[Note]:
    return db.query(Note).filter(Note.id == note_id).first()

# def get_all_notes(db: Session) -> List[Note]:
#     return db.query(Note).all()
def get_all_notes(db: Session, search: str = None, tag: str = None):
    query = db.query(Note)

    if search:
        search_term = f"%{search.lower()}%"
        query = query.filter(
            or_(
                Note.title.ilike(search_term),
                Note.content.ilike(search_term)
            )
        )

    if tag:
        query = query.filter(Note.tags.any(name=tag))
        # query = query.filter(Note.tags == tag)

    return query.all()

def update_note(db: Session, note_id: int, note_data: NoteUpdate) -> Optional[Note]:
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return None

    if note_data.title:
        note.title = note_data.title
    if note_data.content:
        note.content = note_data.content
    if note_data.tags is not None:
        note.tags.clear()
        for tag_name in note_data.tags:
            tag = get_or_create_tag(db, tag_name)
            note.tags.append(tag)

    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int) -> bool:
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return False
    db.delete(note)
    db.commit()
    return True
