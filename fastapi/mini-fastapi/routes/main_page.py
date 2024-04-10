from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.responses import RedirectResponse


def main_page_route(app: FastAPI):
    @app.get("/")
    async def main_page() -> Response:
        return RedirectResponse("/index.html")