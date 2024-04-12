from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import status
from fastapi import File
from uuid import uuid4


router = APIRouter(
    prefix="/images",
    tags=["Images"]
)

ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/jpg']

@router.post('')
def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Allowed only jpeg and png")
    
    file_type = file.content_type.split('/').pop()
    filename = f"{str(uuid4())}.{file_type}"

    with open(f"images/{filename}", 'wb+') as buffer:
        buffer.write(file.file.read())

    return f"images/{filename}"