from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates


render = Jinja2Templates("views")

# service pages
def not_found_page(req: Request) -> Response:
    return render.TemplateResponse("service_pages/404.jinja", {"request": req})

def not_allowed_page(req: Request) -> Response:
    return render.TemplateResponse("service_pages/not_allowed.jinja", {"request": req})

def redirect_page(req: Request, redirect_url:str) -> Response:
    return render.TemplateResponse("service_pages/redirect.jinja", {"request": req, "redirect_url": redirect_url})

# auth pages
def login_page(req: Request, message: str = "") -> Response:
    return render.TemplateResponse("auth/login.jinja", {"request": req, "message": message})

def register_page(req: Request) -> Response:
    return render.TemplateResponse("auth/register.jinja", {"request": req})

# pages need auth
def dashboard_page(req: Request, data: dict = {}) -> Response:
    return render.TemplateResponse("pages/panel.jinja", {"request": req, "data": data})
