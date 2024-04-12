import datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from sqlalchemy.orm import Session
import jwt

from database.db import get_db
from database import db_user
from database.schemes import UserDb


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "SomeRandomSalt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserDb:
    error_response = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = token_data["sub"]
    except jwt.PyJWTError as e:
        print(e)
        raise error_response
    
    user = db_user.get(db, user_id)
    if user is None:
        raise error_response
    
    return user
    
