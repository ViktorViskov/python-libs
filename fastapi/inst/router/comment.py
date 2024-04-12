from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session
from database.db import get_db
from database import db_comment
from database import db_post
from database.schemes import UserDb
from models.comment import CommentCreate
from models.comment import CommentGet
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)

@router.post('', response_model=CommentGet, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentCreate, db: Session = Depends(get_db), user: UserDb = Depends(get_current_user)):
    post = db_post.get(db, comment.post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    return db_comment.create(db, comment, user.id)

@router.get('/post/{id}', response_model=list[CommentGet])
async def get_comments(id: int = Path(gt=0), db: Session = Depends(get_db)):
    return db_comment.get_by_post(db, id)

@router.delete('/{comment_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(comment_id: int, db: Session = Depends(get_db), user: UserDb = Depends(get_current_user)):
    comment = db_comment.get(db, comment_id)
    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    if comment.owner_id!= user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not the owner of this comment")
    
    db_comment.delete(db, comment_id)