from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session
from database.db import get_db
from database import db_user
from database import db_post
from database.schemes import UserDb
from models.post import PostCreate
from models.post import PostGet
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post('', response_model=PostGet)
async def create_post(post: PostCreate, db: Session = Depends(get_db), user: UserDb = Depends(get_current_user)):
    return db_post.create(db, post, user.id)

@router.get('/all', response_model=list[PostGet])
async def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db), user: UserDb = Depends(get_current_user)):
    post = db_post.get(db, post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if post.owner_id!= user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not the owner of this post")
    
    db_post.delete(db, post_id)