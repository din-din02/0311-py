#Пока не нужно потом изменить название!!
#python -m uvicorn very_first:app --reload

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

white_urls = ["/", "/login", "/home", "/register", "/main"]

@app.get("/home", response_class=HTMLResponse) #перехват адреса 

def home_page(request: Request):
    return templates.TemplateResponse( request=request, name="home.html")

@app.get("/404", response_class=HTMLResponse) #перехват адреса 
def error_page(request: Request):
    return templates.TemplateResponse( request=request, name="404.html")

@app.get("/login", response_class=HTMLResponse) #перехват адреса 
def login_page(request: Request):
    return templates.TemplateResponse( request=request, name="login.html")

@app.get("/main", response_class=HTMLResponse) #перехват адреса 
def main_page(request: Request):
    return templates.TemplateResponse( request=request, name="main.html")

@app.get("/register", response_class=HTMLResponse) #перехват адреса 
def reg_page(request: Request):
    return templates.TemplateResponse( request=request, name="register.html")