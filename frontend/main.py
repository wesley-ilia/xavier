from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
# from mySQL_db import MySQL
from Log import Log
from utils import insert_log_in_db, make_csv
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="html/")
load_dotenv(dotenv_path='../login.env')
# db = MySQL()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.route("/")
def choose(request: Request):
    return templates.TemplateResponse('index.html',
                                      context={'request': request})

@app.get("/search")
def get_info(market: str, stack: str, state: str, file_name: str='untitled'):
    query = "SELECT * FROM empresa_completa3 WHERE "
    if not file_name:
        file_name = 'untitled'
    file_name += '.csv'

    if state:
        state_query = "(`estado`=' " + state.replace(',', "' OR `estado`=' ") + "')"
        query += state_query
        if market:
            query += ' AND '
            market_query = "(`mercado`='" + market.replace(',', "' OR `mercado`='") + "')"
            query += market_query
        if stack:
            query += ' AND '
            stack_query = "(`stacks` like '%" + stack.replace(',', "%' OR `stacks` like '%") + "%')"
            query += stack_query
    elif market:
        market_query =  "(`mercado`='" + market.replace(',', "' OR `mercado`='") + "')"
        query += market_query
        if stack:
            query += ' AND '
            stack_query = "(`stacks` like '%" + stack.replace(',', "%' OR `stacks` like '%") + "%')"
            query += stack_query
    elif stack:
        stack_query = "(`stacks` like '%" + stack.replace(',', "%' OR `stacks` like '%") + "%')"
        query += stack_query
    else:
        return {"message": "error"}
    print(query)
    log = Log()
    log.save_to_csv(query, log.con, file_name)
    return FileResponse(file_name, filename=file_name)


    """
        SELECT * FROM `empresa_completa3` WHERE (estado='{state_query}') AND (mercado='{market_query}')
    """

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
