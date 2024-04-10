from uuid import uuid4

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import File
from sqlalchemy.orm import Session

from database.db import get_db
from models.requests_schemes import PostRequest
from models.response_schemes import PostResponse
from database import post_crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostRequest, db: Session = Depends(get_db)):
    return post_crud.create(db, post)

@router.get("", status_code=status.HTTP_200_OK, response_model=list[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return post_crud.get_all(db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    result = post_crud.delete(db, id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.post("/upload-image", status_code=status.HTTP_201_CREATED)
def upload_image(file: UploadFile = File(...)):
    ALLOWED_TYPES = {
        "image/png", 
        "image/jpeg", 
        "image/jpg"
    }
    
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Unsupported media type")
    
    file_type = file.content_type.split('/')[-1]
    file_name = f"{uuid4()}.{file_type}"
    file_path = f"images/{file_name}"
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return file_path