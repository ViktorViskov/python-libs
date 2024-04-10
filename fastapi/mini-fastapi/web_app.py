import uvicorn 
from fastapi import Request
from fastapi import Response
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.main_page import main_page_route
from middleware.cookies import cookies_checker


class WebApp:
    server: FastAPI
    host_addr: str
    port: int
    workers: int

    def __init__(self, *, host_addr: str, port: int) -> None:
        self.server = FastAPI()
        self.host_addr = host_addr
        self.port = port
        self.workers = 4

        self._init_middleware()
        self._init_routes()
        self._init_static()
    
    def _init_middleware(self) -> None:
        cookies_checker(self.server)

    def _init_routes(self) -> None:
        main_page_route(self.server)
    
    def _init_static(self) -> None:
        self.server.mount("/src", StaticFiles(directory="src"), name="src")

    def start(self, app_str: str,* , development: bool = False) -> None:
        if development:
            uvicorn.run(app=app_str, host=self.host_addr, port=self.port, reload=True)
        else:
            uvicorn.run(app=app_str, host=self.host_addr, port=self.port, workers=self.workers)