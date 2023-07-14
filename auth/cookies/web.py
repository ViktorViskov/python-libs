from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.responses import PlainTextResponse

from auth_middleware import AuthMiddleware

from auth_web import app as auth_subpath

app = FastAPI()
auth_middleware = AuthMiddleware(app)

@app.get("/")
def main():
    return PlainTextResponse("Main")

@app.get("/private")
def main():
    return PlainTextResponse("Private")


app.mount("/auth", auth_subpath)
