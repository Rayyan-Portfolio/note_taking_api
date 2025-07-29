from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.session import Base

note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)
