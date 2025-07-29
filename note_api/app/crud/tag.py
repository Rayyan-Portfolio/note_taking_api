from sqlalchemy.orm import Session
from app.models.tag import Tag

def get_or_create_tag(db: Session, tag_name: str) -> Tag:
    tag = db.query(Tag).filter(Tag.name == tag_name).first()
    if tag:
        return tag
    tag = Tag(name=tag_name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_all_tags(db: Session):
    return db.query(Tag).all()
