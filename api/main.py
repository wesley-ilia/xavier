from fastapi import FastAPI, Request
# from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from Log import Log
import pandas as pd

load_dotenv(dotenv_path='../login.env')
log = Log()
db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)

app = FastAPI()
templates = Jinja2Templates(directory="frontend/html")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.route("/")
def choose(request: Request):
    return templates.TemplateResponse('index.html',
                                      context={'request': request})

@app.get("/dropdown")
def dropdown():
    return "teste2<br>teste3"

@app.get("/search")
def get_info(market: str, stack: str, state: str, file_name: str='untitled', get_csv : bool = False):
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
    df = db.query(query)
    if get_csv:
        df.to_csv(file_name, sep=',', index=False)
        return FileResponse(file_name, filename=file_name)
    else:
        return len(df.index)
