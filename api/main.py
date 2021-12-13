from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import pandas as pd
from Log import Log
import json

app = FastAPI()
templates = Jinja2Templates(directory="frontend/html")
load_dotenv(dotenv_path='../login.env')

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.route("/")
def choose(request: Request):
    log = Log()
    df = pd.read_sql_query("SELECT mercado, stacks FROM empresa_completa3 WHERE 1")
    mercados = list(set(df['mercado'].to_list()))
    total_stacks = df['mercado'].to_list()
    stacks = []
    for stack in total_stacks:
        stacks.extend(stack.split(','))
    stacks = list(set(stacks))
    with open("out.json", 'w') as f:
        json.dump({'mercados': mercados, 'stacks': stacks}, f, indent=4)
    return templates.TemplateResponse('index.html',
                                      context={'request': request})

@app.get("/search")
def get_info(market: str, stack: str, state: str, file_name: str='untitled'):
    query = "SELECT * FROM empresa_completa3 WHERE "
    query2 = "SELECT * FROM empresa_completa3 WHERE "
    if not file_name:
        file_name = 'Untitled'
    file_name += '.csv'

    if state and state != 'TODOS':
        print("teste")
        state_list = state.split(',')
        for st in state_list:
            if st != 'OR' and st != 'AND' and st != 'NOT':
                query2 += "`estado`=' " + st + "' "
            else:
                query2 += st + " "
        """ state_novo = state.replace(",", "")
        state_novo = state.replace('OR', "' OR `estado`=' ").replace('AND', "' AND `estado`=' ")
        state_query = "(`estado`=' " +  + "')"
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
        return {"message": "error"}"""
    print(query2)
    # print(query)
    log = Log()
    log.save_to_csv(query2, log.con, file_name)
    return FileResponse(file_name, filename=file_name)
