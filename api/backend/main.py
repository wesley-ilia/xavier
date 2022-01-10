from fastapi import FastAPI, UploadFile, File
import shutil
# from fastapi.params import Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from Log import Log
import pandas as pd
import numpy as np
import os
from unidecode import unidecode

todas_capitais = ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

origins = [
    "http://localhost:3000",
]

load_dotenv(dotenv_path='login.env')

with open("../frontend/src/modelo.csv", 'w') as f:
    f.write("nome,estado,cidade,mercado,stacks")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def agg(a):
    a = a.replace(np.nan, "")
    # a.dropna(inplace=True)
    a.reset_index(drop=True, inplace=True)
    ret = ", ".join(set(", ".join(a).split(', ')))
    print('ret = ' + ret)
    return ret

def initialize():
    global df
    log = Log()
    global db
    db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)
    df = db

    db['mercado'].replace(np.nan, "", inplace=True)
    total_mercados = db['mercado'].to_list()
    mercados = []
    for mercado in total_mercados:
        if mercado:
            mercados.extend([s.strip() for s in mercado.split(',')])
    mercados = [x for x in list(set(mercados)) if x]
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
    print("mercado = " + db['mercado'][6498])

initialize()

def importFile (NomeArquivo):
    arquivo = pd.read_csv(NomeArquivo)
    if 'nome' not in arquivo.columns:
        print("veio errado")
    
    arquivo.replace(r'^\s*$', np.NaN, regex=True, inplace=True)

    erradas = arquivo.loc[arquivo['nome'].isnull()]
    adicionar = arquivo.loc[arquivo['nome'].notnull()]

    print(adicionar.columns)

    columns = ['estado', 'cidade', 'mercado', 'stacks']
    for col in columns:
        if col not in adicionar.columns:
            adicionar[col] = np.full(len(adicionar.index), np.nan)

    adicionar['nome'] = adicionar['nome'].str.strip()
    aggregation_functions = {'estado': 'first', 'cidade': 'first', 'mercado': agg, 'stacks': agg}
    adicionar = adicionar.groupby(['nome'], as_index=False).aggregate(aggregation_functions)
    print(adicionar)
    
    log = Log()
    df = pd.read_sql_query("SELECT * FROM tb_usuario WHERE 1", log.con)
    adicionar = pd.concat([df, adicionar], axis=0, ignore_index=True)
    adicionar = adicionar.groupby(['nome'], as_index=False).aggregate(aggregation_functions)

    adicionar.reset_index(drop=True, inplace=True)
    print(adicionar['mercado'])

    """ df = pd.concat([db, adicionar], axis=0, ignore_index=True)
    aggregation_functions = {'estado': 'first', 'cidade': 'first', 'mercado': agg}
    df = df.groupby(['nome'], as_index=False).aggregate(aggregation_functions)
    df.reset_index(drop=True, inplace=True) """
    
    adicionar.replace(np.nan, "", inplace=True)

    adicionar_list = adicionar[['nome', 'estado', 'cidade', 'mercado', 'stacks']].values.tolist()

    print(adicionar_list)

    log = Log()
    df = pd.read_sql_query("SELECT * FROM tb_usuario WHERE 1", log.con)
    for adc in adicionar_list:
        if adc[0] in df['nome']:
            stmt = f"UPDATE tb_usuario (`estado`, `cidade`, `mercado`, `stacks`) VALUES (%s, %s, %s, %s), WHERE nome={adc[0]}"
            log.cursor.execute(stmt, adicionar_list)
    stmt = "INSERT INTO tb_usuario (`nome`, `estado`, `cidade`, `mercado`, `stacks`) VALUES (%s, %s, %s, %s, %s)"
    log.cursor.executemany(stmt, adicionar_list)
    log.con.commit()

    print(adicionar)
    os.remove(NomeArquivo)
    initialize()


@app.post("/api/uploadfile")
async def upload(file: UploadFile=File(...)):
    with open(f"{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    importFile(file.filename)
    return{"File_name" : file.filename}

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
            markets = market.split(',')
            print(markets)
            for i in range(len(markets)):
                query += f'mercado.str.contains("{markets[i]}", na=False).values'
                if i < len(markets) - 1:
                    query += ' or '
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
        markets = market.split(',')
        for i in range(len(markets)):
            query += f'mercado.str.contains("{markets[i]}", na=False).values'
            if i < len(markets) - 1:
                query += ' or '

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
            markets = market.split(',')
            print(markets)
            for i in range(len(markets)):
                query += f'mercado.str.contains("{markets[i]}", na=False).values'
                if i < len(markets) - 1:
                    query += ' or '

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
        markets = market.split(',')
        for i in range(len(markets)):
            query += f'mercado.str.contains("{markets[i]}", na=False).values'
            if i < len(markets) - 1:
                query += ' or '

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
