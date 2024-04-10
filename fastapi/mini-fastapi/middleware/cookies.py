from fastapi import FastAPI
from fastapi import Request


def cookies_checker(server: FastAPI) -> None:
    @server.middleware("http")
    async def cookies_middleware(request: Request, call_next):
        return await call_next(request)