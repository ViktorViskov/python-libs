from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from database.schemes import base
from database.schemes import engine
from router import users
from router import posts
from router import comment
from router import images
from router import auth


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(images.router)
app.include_router(comment.router)

app.mount("/images", StaticFiles(directory="images"), name="images")

base.metadata.create_all(engine)
