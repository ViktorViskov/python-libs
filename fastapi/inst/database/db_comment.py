from sqlalchemy.orm import Session

from .schemes import CommentDb
from models.comment import CommentCreate

def create(db: Session, comment: CommentCreate, owner_id: int) -> CommentDb:
    db_comment = CommentDb()
    db_comment.text = comment.text
    db_comment.post_id = comment.post_id
    db_comment.owner_id = owner_id

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get(db: Session, id: int) -> CommentDb | None:
    return db.query(CommentDb).where(CommentDb.id == id).first()

def get_by_post(db: Session, id: int) -> CommentDb | None:
    return db.query(CommentDb).where(CommentDb.post_id == id).all()

def delete(db: Session, id: int) -> None:
    db.query(CommentDb).where(CommentDb.id == id).delete()
    db.commit()