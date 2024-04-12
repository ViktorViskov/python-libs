from sqlalchemy.orm import Session

from .schemes import PostDb
from .schemes import CommentDb
from models.post import PostCreate

def create(db: Session, post: PostCreate, owner_id: int) -> PostDb:
    db_post = PostDb()
    db_post.title = post.title
    db_post.content = post.content
    db_post.image_url = post.image_url
    db_post.owner_id = owner_id

    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_all(db: Session):
    return db.query(PostDb).all()

def get(db: Session, post_id: int) -> PostDb | None:
    return db.query(PostDb).where(PostDb.id == post_id).first()

def delete(db: Session, post_id: int) -> None:
    db.query(CommentDb).where(CommentDb.post_id == post_id).delete()
    db.query(PostDb).where(PostDb.id == post_id).delete()
    db.commit()