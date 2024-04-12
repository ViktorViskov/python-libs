from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from database.db import get_db
from database import db_user
from models.user import UserCreate
from models.user import UserGet


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('', response_model=UserGet)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return db_user.create(db, user)

@router.get('/all', response_model=list[UserGet])
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all(db)