from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from Log import Log
import pandas as pd
import numpy as np

load_dotenv(dotenv_path='../login.env')
log = Log()
db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)

app = FastAPI()
templates = Jinja2Templates(directory="frontend/html")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.route("/")
def choose(request: Request):
    db['mercado'].replace(np.nan, "", inplace=True)
    mercados = [x for x in list(set(db['mercado'].to_list())) if x]
    mercados.sort()
    db['stacks'].replace(np.nan, "", inplace=True)
    total_stacks = db['stacks'].to_list()
    stacks = []
    for stack in total_stacks:
        if stack:
            stacks.extend([s.strip() for s in stack.split(',')])
    stacks = [x for x in list(set(stacks)) if x]
    stacks.sort()
    global dropdown_list
    dropdown_list = {"mercados": mercados, "stacks": stacks}
    return templates.TemplateResponse('index.html',    
                                  context={'request': request})
@app.route("/mercados_list")
def get_mercados(request: Request):
    return templates.TemplateResponse('list.html',
                                      context={'request': request, 
                                      "lists": dropdown_list['mercados'], "name": "Mercados"})

@app.route("/estados_list")
def get_mercados(request: Request):
    estados_ori = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'TODOS'];
    
    return templates.TemplateResponse('list.html',
                                      context={'request': request, 
                                      "lists": estados_ori, "name": "Estados"})

@app.route("/stacks_list")
def get_mercados(request: Request):
    return templates.TemplateResponse('list.html',
                                      context={'request': request, 
                                      "lists": dropdown_list['stacks'], "name":"Stacks"})


@app.get("/dropdown")
def dropdown():
    return dropdown_list

@app.get("/search")
def get_info(market: str, stack: str, state: str, file_name: str='untitled', get_csv : bool = False):
    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")
    print(stack)

    query = ""
    if not file_name:
        file_name = 'Untitled'
    file_name += '.csv'

    if state and state != 'TODOS':
        state_query = "(estado==' " + state.replace(',', "' or estado==' ") + "')"
        query += state_query
        if market:
            query += ' and '
            market_query = "(mercado=='" + market.replace(',', "' or mercado=='") + "')"
            query += market_query
        if stack:
            query += ' and '
            stacks = stack.split(',')
            for i in range(len(stacks)):
                query += f'stacks.str.contains("{stacks[i]}", na=False).values'
                if i < len(stacks) - 1:
                    query += ' or '
    elif market:
        market_query = "(mercado=='" + market.replace(',', "' or mercado=='") + "')"
        query += market_query
        if stack:
            query += ' and '
            stacks = stack.split(',')
            for i in range(len(stacks)):
                query += f'stacks.str.contains("{stacks[i]}", na=False).values'
                if i < len(stacks) - 1:
                    query += ' or '
    elif stack:
        stacks = stack.split(',')
        for i in range(len(stacks)):
            query += f'stacks.str.contains("{stacks[i]}", na=False).values'
            if i < len(stacks) - 1:
                query += ' or '
    else:
        return 0
    print(query)
    df = db.query(query)
    if get_csv:
        df.to_csv(file_name, sep=',', index=False)
        return FileResponse(file_name, filename=file_name)
    else:
        return len(df.index)
