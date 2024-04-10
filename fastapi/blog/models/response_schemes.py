from datetime import datetime

from pydantic import BaseModel

   
class PostResponse(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    updated_at: datetime
    created_at: datetime
    
    class Config():
        orm_mode = True