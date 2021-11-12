from fastapi import FastAPI, Request
from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from mySQL_db import MySQL
from Log import Log
from utils import *

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
load_dotenv(dotenv_path='../login.env')
db = MySQL()
log = Log()
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

@app.route('/log')
def show_log(request: Request):
    return templates.TemplateResponse('log.html', context={'request': request})

@app.get("/get_by_language")
def get_by_language(*, search: str, obs: str, output_name: str):
    output_csv = output_name + ".csv"
    query = f"SELECT * FROM stacks WHERE \
    `DevOps` LIKE '%{search}%' or \
    `Application and Data` LIKE '%{search}%' or \
    `Utilities` LIKE '%{search}%' or \
    `Business Tools` like '%{search}%'"
    error = make_csv(query, output_csv, log.con)
    insert_log_in_db(log, query, output_csv, obs)

    if error:
        return {"error": "search not found"}
    return FileResponse(output_csv, filename=output_csv)


@app.get("/start_up_base")
def get_in_startup_base(state_name: str, output_name: str, obs: str, mercado: str):
    print(mercado)
    query = "SELECT * FROM empresa_completa WHERE"
    if mercado:
        mercado = mercado.replace(",", "%' OR `mercado` LIKE '%")
        query += f" `mercado` like ('%{mercado}%')"
    if state_name:
        if mercado:
            query += " AND"
        state_name = state_name.upper()
        state_name = state_name.replace(" OR ", "%' OR `estado` LIKE '%").replace(" AND ", "%' AND `estado` LIKE '%")
        query += f" `estado` like ('%{state_name}%')"
    if not mercado and not state_name:
        return {"error": "search something"}
    """   else:
    state_name = state_name.upper()
    state_name = state_name.replace(" OR ", "%' OR `estado` LIKE '%").replace(" AND ", "%' AND `estado` LIKE '%")
    query = f"SELECT * FROM empresa_completa WHERE `estado` like '%{state_name}%' AND `mercado` like '%{mercado}%'" """
    print(query)
    if not output_name:
        output_name = "untitled"
    output_csv = output_name + ".csv"
    error = make_csv(query, output_csv, log.con)
    insert_log_in_db(log, query, output_csv, obs)

    if error:
        return {"error": "search not found"}
    return FileResponse(output_csv, filename=output_csv)

@app.get('/insert_into_log')
def fill_log(comment: str, feedback: bool, obs: str):
    log.set_feedback(feedback=feedback,
                     comment=comment,
                     obs=obs)
    return {"message": "sucesso"}



""" tabela logs
id
query
result
version
date_time
feedback
obs
comments
"""

