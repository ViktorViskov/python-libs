from sqlalchemy.orm import Session

from models.db_schemes import PostDb
from models.requests_schemes import PostRequest

def create(db: Session, post: PostRequest) -> PostDb:
    new_post = PostDb()
    new_post.image_url = post.image_url
    new_post.title = post.title
    new_post.content = post.content
    new_post.creator = post.creator
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

def get_all(db: Session) -> list[PostDb]:
    return db.query(PostDb).all()

def delete(db: Session, id: int) -> bool:
    result = db.query(PostDb).where(PostDb.id == id).delete()   
    db.commit()
    return bool(result)