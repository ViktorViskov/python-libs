from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse

from auth_controller import AuthController


class AuthMiddleware:
    AUTH_URLS: tuple
    app: FastAPI

    def __init__(self, server: FastAPI) -> None:
        self._set_variables(server)
        self._add_auth_middleware()

    def _set_variables(self, server: FastAPI) -> None:
        self.app = server
        self.AUTH_URLS =  (
            "/private",
        )

    def _add_auth_middleware(self):
        @self.app.middleware("http")
        async def middleware(req: Request, call_back):
            auth = AuthController()
            token = req.cookies.get("token")
            url = "/%s" % req.url.path.split("/", 2)[1].lower()

            if url in self.AUTH_URLS:
                if token and auth.check_token(token):
                    response = await call_back(req)
                else:
                    response = PlainTextResponse("Not authorized")
                    response.delete_cookie("token")
            else:
                response = await call_back(req)

            return response

