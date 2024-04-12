from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Request
from sqlalchemy.orm import Session

from database.db import get_db
from database import db_user
from database import hash
from auth import oauth2


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db_user.get_by_username(db, form.username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not hash.verify_password(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    token_data = {
        "sub": user.id
    }

    token = oauth2.create_access_token(token_data)
    return {
        "access_token": token,
        "token_type": "bearer",
    }
