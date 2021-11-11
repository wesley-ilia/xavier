from fastapi import FastAPI
import pymysql
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from dotenv import load_dotenv
from mySQL_db import MySQL
from time import sleep

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
load_dotenv(dotenv_path='../login.env')
db = MySQL()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.route("/")
def choose(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.route("/startupbase")
def startupbase(request: Request):
    return templates.TemplateResponse('startupbase.html', context={'request': request})

@app.route("/stackshare")
def stackshare(request: Request):
    return templates.TemplateResponse('stackshare.html', context={'request': request})

@app.get("/get_by_language/{language}")
def get_by_language(language: str = None):
    result_search = db.select_from(
     f"SELECT name FROM stacks WHERE\
     `Application and Data` like '%{language}%'")
    return result_search





