from pydantic import BaseModel
from datetime import datetime

from .user import UserGet


class CommentCreate(BaseModel):
    text: str
    post_id: int

class CommentGet(BaseModel):
    id: int
    text: str
    owner: UserGet
    created_at: datetime