from pydantic import BaseModel
from datetime import datetime

from .user import UserGet
from .comment import CommentGet


class PostCreate(BaseModel):
    title: str
    content: str
    image_url: str

class PostGet(BaseModel):
    id: int
    title: str
    content: str
    image_url: str
    owner: UserGet
    comments: list[CommentGet]
    created_at: datetime
    updated_at: datetime