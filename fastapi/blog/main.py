from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from models.db_schemes import base
from database.db import engine
from routers import post

base.metadata.create_all(engine)

app = FastAPI()

app.include_router(post.router)

app.mount("/images", StaticFiles(directory="images"), name="static")

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)