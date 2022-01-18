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
from sqlalchemy import create_engine, event
from mysql import connector
import time
from io import StringIO
from utils import save_pdf

todas_capitais = ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

origins = [
    "http://localhost:3000",
]

load_dotenv(dotenv_path='login.env')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log = Log()
db = pd.read_sql_query("SELECT * FROM empresa_completa3 WHERE 1", log.con)

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWD")
sql = f'mysql+pymysql://{user}:{password}@{host}:3306/decasoft_xavier'
engine = create_engine(sql, echo=False)

@event.listens_for(engine, 'before_cursor_execute')
def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
    if executemany:
        cursor.fast_executemany = True

def agg(a):
    a = a.replace(np.nan, "")
    # a.dropna(inplace=True)
    a.reset_index(drop=True, inplace=True)
    s = [unidecode(i.strip().lower()) for i in ",".join(a).split(',') if i]
    ret = ", ".join(set(s))
    ret = ret.strip()

    return ret

def initialize():
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
    dropdown_list = {"mercados": mercados, "stacks": stacks, "colunas": db.columns.tolist()}

initialize()
""" DELETE FROM `empresa_merge_teste` WHERE `nome` like '%Cleimes%' or `nome` like '%JR%INFORMATICA%' """
 
def update_db_2(adicionar):
    values = ""
    query = "INSERT INTO empresa_merge_teste ("
    for i, col in enumerate(db.columns):
        if col != 'id':
            query += col
            values += '%s'
            if i < len(db.columns) - 1 and db.columns[i + 1] != 'id':
                query += ','
                values += ','
    query += f') values ({values})'

    delete = "DELETE FROM `empresa_merge_teste` WHERE "

    query_insert = 'INSERT INTO empresa_merge_teste (nome, estado, cidade, mercado, stacks) VALUES ("%s", "%s", "%s", "%s", "%s")'
    update = []
    insert = []
    for i, el in enumerate(adicionar['nome']):
        index = db.index[db['nome'] == el].tolist()
        if index:
            index = index[0]
            if delete != "DELETE FROM `empresa_merge_teste` WHERE ":
                delete += " or "
            delete += f' `nome` like "%{el}%" '
            update.append(db.iloc[index].tolist()[:-1])
        else:
            insert.append(adicionar.iloc[i][['nome', 'estado', 'cidade', 'mercado', 'stacks']].tolist())

    print("iniciando")
    log = Log()
    if update:
        log.cursor.execute(delete)
        t2 = time.time()
        total = t2-t0
        print("delete = " + str(total))
        log.cursor.executemany(query,update)
        t3 = time.time()
        total = t3-t2
        print("update = " + str(total))
    if insert:
        log.cursor.executemany(query_insert,insert)
        t4 = time.time()
        total = t4-t3
        print("insert = " + str(total))
    if insert or update:
        log.con.commit()

def update_db(adicionar):
    t0 = time.time()

    aggregation_db = {'estado': 'first', 'cidade': 'first', 'mercado': agg, 'stacks': agg}
    for col in db.columns:
        if col not in aggregation_db.keys():
            aggregation_db[col] = 'first'
    
    adicionar = pd.concat([db, adicionar], axis=0, ignore_index=True)
    adicionar = adicionar.groupby(['nome'], as_index=False).aggregate(aggregation_db)
    adicionar.reset_index(drop=True, inplace=True)

    adicionar['id'] = adicionar.index
    cols = adicionar.columns.tolist()
    nome = cols.index('nome')
    cols = [cols[nome]] + cols[:nome] + cols[nome + 1:]
    adicionar = adicionar[cols]
    adicionar.to_sql("empresa_merge_teste", engine, if_exists='replace', index=False)
    with engine.connect() as con:
        con.execute('ALTER TABLE `empresa_merge_teste` ADD PRIMARY KEY (id);')
    t1 = time.time()
    total = t1-t0
    print("total time 2 = " + str(total))
    return adicionar

def importFile (NomeArquivo):
    arquivo = pd.read_csv(NomeArquivo)
    if 'nome' not in arquivo.columns:
        return False, ""
    
    arquivo.replace(r'^\s*$', np.NaN, regex=True, inplace=True)

    erradas = arquivo.loc[arquivo['nome'].isnull()]
    adicionar = arquivo.loc[arquivo['nome'].notnull()]


    columns = ['estado', 'cidade', 'mercado', 'stacks']
    for col in columns:
        if col not in adicionar.columns:
            adicionar[col] = np.full(len(adicionar.index), np.nan)

    adicionar['nome'] = adicionar['nome'].str.strip()
    aggregation_user = {'estado': 'first', 'cidade': 'first', 'mercado': agg, 'stacks': agg}
    
    t0 = time.time()
    log = Log()
    df = pd.read_sql_query("SELECT * FROM tb_usuario4 WHERE 1", log.con)
    adicionar = pd.concat([df, adicionar], axis=0, ignore_index=True)
    adicionar = adicionar.groupby(['nome'], as_index=False).aggregate(aggregation_user)

    adicionar.reset_index(drop=True, inplace=True)

    adicionar['id'] = adicionar.index
    cols = adicionar.columns.tolist()
    nome = cols.index('nome')
    cols = [cols[nome]] + cols[:nome] + cols[nome + 1:]
    adicionar = adicionar[cols]
    adicionar.to_sql("tb_usuario3", engine, if_exists='replace', index=False)
    with engine.connect() as con:
        con.execute('ALTER TABLE `tb_usuario3` ADD PRIMARY KEY (id);')
    t1 = time.time()
    total = t1-t0
    print("total time 1 = " + str(total))

    global db
    db = update_db(adicionar)
    
    os.remove(NomeArquivo)
    initialize()
    return True, erradas

@app.post("/api/uploadfile")
async def upload(file: UploadFile=File(...)):
    with open(f"{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    worked, erradas = importFile(file.filename)
    if worked:
        erradas = ", ".join([str(i) for i in (erradas.index + 1)])
        if erradas:
            print(erradas)
            return {"message" : "As linhas " + erradas + " são inválidas, as outras foram adicionadas com sucesso!!"}
        return {"message" : 'Cadastrados com sucesso'}
    else:
        return {"message" : "Coluna 'nome' está faltando"}

@app.get("/dropdown")
def dropdown():
    return dropdown_list

@app.get("/search")
def get_info(market: str, stack: str, state: str, capitais: str, colunas: str, 
             cidade: str = "", file_name: str='Untitled', extension: str = "csv"):
    
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
    if colunas:
        colunas = colunas.split(',')
        df = df[colunas]
    if extension == 'csv':
        df.to_csv(file_name, sep=',', index=False)
    elif extension == 'xlsx':
        df.to_excel(file_name, index=False)
    elif extension == 'pdf':
        save_pdf(df, file_name)
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
