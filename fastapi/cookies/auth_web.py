from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import PlainTextResponse

from auth_controller import AuthController


app = FastAPI()
auth_controller = AuthController()

@app.get("/login")
def main():
    resp = PlainTextResponse("Login")
    token = auth_controller.login_user("carrergt", "pass")
    resp.set_cookie("token", token.token)
    return resp

@app.get("/logout")
def main(req: Request):
    resp = PlainTextResponse("Logout")
    auth_controller.logout_user(req.cookies.get("token"))
    resp.delete_cookie("token")
    return resp

