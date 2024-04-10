from pydantic import BaseModel


class PostRequest(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str