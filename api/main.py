from fastapi import FastAPI
# from fastapi.params import Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from Log import Log
import pandas as pd
import numpy as np

todas_capitais = ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

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
def get_info(market: str, stack: str, state: str, capitais: str, cidade: str = "", file_name: str='Untitled',
             extension: str = "csv"):
    if capitais == "sim":
        cidade = ""
    elif capitais == "nao":
        capitais_juntas = " ' and cidade!='".join(todas_capitais)
        cidade = "(cidade!='" + capitais_juntas + " ')"
    
    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")

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
            if capitais == 'nao':
                query += cidade
            else:
                cidade_query = "(cidade=='" + cidade.replace(',', "' or cidade=='") + "')"
                print(cidade_query)
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
    else:
        return '0'

    df = db.query(query)

    print(query)
    if extension == 'csv':
        df.to_csv(file_name, sep=',', index=False)
    elif extension == 'xlsx':
        df.to_excel(file_name, index=False)
    return FileResponse(file_name, filename=file_name)

@app.get("/cidades")
def get_cidades(state: str):
    state_query = "(estado==' " + state.replace(',', "' or estado==' ") + "')"

    df = db.query(state_query)
    cididades = list(set(df['cidade'].to_list()))
    cididades.sort()
    return (cididades)

@app.get("/preview")
def get_preview(state: str, cidade: str, market:str, stack: str, capitais: str):
    if capitais == "sim":
        cidade = ""
    elif capitais == "nao":
        capitais_juntas = " ' and cidade!='".join(todas_capitais)
        cidade = "(cidade!='" + capitais_juntas + " ')"

    query = ""

    stack = stack.replace("Cpp","C\+\+")
    stack = stack.replace("Csharp","C#")

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
            if capitais == 'nao':
                query += cidade
            else:
                cidade_query = "(cidade=='" + cidade.replace(',', "' or cidade=='") + "')"
                print(cidade_query)
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
    else:
        return '0'
    
    df = db.query(query)
    return len(df.index)