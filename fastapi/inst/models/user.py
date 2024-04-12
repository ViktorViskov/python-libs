from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserGet(BaseModel):
    id: int
    username: str
    email: str
    updated_at: datetime
    created_at: datetime