from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from .db import base

from .db import base
from .db import engine


class UserDb(base):
    __tablename__ = 'users'
    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    username = Column("username", String(128))
    email = Column("email", String(128))
    password = Column("password", String(128))
    posts = relationship("PostDb", back_populates="owner")
    comments = relationship("CommentDb", back_populates="owner")
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())

class PostDb(base):
    __tablename__ = 'posts'
    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    title = Column("title", String(128))
    content = Column("content", String(1024))
    image_url = Column("image_url", String(128))
    owner_id = Column("owner_id", Integer, ForeignKey("users.id"))
    owner = relationship("UserDb", back_populates="posts")
    comments = relationship("CommentDb", back_populates="post")
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())

class CommentDb(base):
    __tablename__ = 'comments'
    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    text = Column("title", String(512))
    owner_id = Column("owner_id", Integer, ForeignKey("users.id"))
    owner = relationship("UserDb", back_populates="comments")
    post_id = Column("post_id", Integer, ForeignKey("posts.id"))
    post = relationship("PostDb", back_populates="comments")
    created_at = Column("created_at", DateTime(), default=current_timestamp())