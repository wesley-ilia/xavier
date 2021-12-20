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
    "http://ec2-18-118-198-27.us-east-2.compute.amazonaws.com:3000",
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
def get_info(market: str, stack: str, state: str, file_name: str='untitled', get_csv : bool = False):
    print("mercado = " + market)
    print("estado = " + state)
    print("stack = " + stack)
    
    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")

    print(get_csv)
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
        return '0'

    print("teste" + str(get_csv))
    df = db.query(query)
    if get_csv:
        print(query)
        df.to_csv(file_name, sep=',', index=False)
        return FileResponse(file_name, filename=file_name)
    else:
        return len(df.index)
