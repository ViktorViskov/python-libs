from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql.functions import current_timestamp

from database.db import base


class PostDb(base):
    __tablename__ = 'posts'
    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    image_url = Column("image_url", String(256))
    title = Column("title", String(256))
    content = Column("content", Text)
    creator = Column("creator", String(256))
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())