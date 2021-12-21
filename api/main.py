from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from Log import Log
import pandas as pd
import numpy as np

origins = [
    "http://localhost:3000",
]

load_dotenv(dotenv_path='../login.env')
log = Log()
db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

dropdown_list = {"mercados": mercados, "stacks": stacks}

@app.get("/dropdown")
def dropdown():
    return dropdown_list

@app.get("/search")
def get_info(market: str, stack: str, state: str, cidade: str = "", file_name: str='untitled',
             get_csv : bool = False, extension: str = "csv", get_cidades: bool = False):
    
    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")

    print("cidade = " + cidade)

    print(get_csv)
    query = ""
    if not file_name:
        file_name = 'Untitled'
    file_name += '.' + extension

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
        if cidade:
            query += ' and '
            cidade_query = "(cidade=='" + cidade.replace(',', " ' or cidade=='") + " ')"
            query += cidade_query
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
    elif not get_cidades:
        return '0'
    else:
        return ""

    print(query)
    df = db.query(query)
    if get_cidades:
        return (list(set(df['cidade'].to_list())))
    if get_csv:
        print(query)
        if extension == 'csv':
            df.to_csv(file_name, sep=',', index=False)
        elif extension == 'xlsx':
            df.to_excel(file_name, index=False)
        return FileResponse(file_name, filename=file_name)
    else:
        return len(df.index)
