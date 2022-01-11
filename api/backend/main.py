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
from sqlalchemy import create_engine
from mysql import connector
import time


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
    s = [unidecode(i.strip().lower()) for i in ",".join(a).split(',') if i]
    ret = ", ".join(set(s))
    ret = ret.strip()

    return ret

def initialize():
    global df
    log = Log()
    global db
    db = pd.read_sql_query("SELECT * FROM empresa_merge_teste WHERE 1", log.con)
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
    dropdown_list = {"mercados": mercados, "stacks": stacks, "colunas": db.columns.tolist()}

initialize()


def update_db(adicionar):
    #stmt = f"UPDATE tb_usuario (`estado`, `cidade`, `mercado`, `stacks`) VALUES (%s, %s, %s, %s), WHERE nome={adc[0]}"
    frase = "INSERT INTO empresa_merge_teste (nome,estado,cidade,mercado,stacks) values(%s,%s,%s,%s,%s)"
    frase2 = "UPDATE empresa_merge_teste SET `stacks` = %s, mercado = %s  WHERE id = %s;"
    # frase2 = " UPDATE empresa_merge_teste (mercado, stacks) VALUES (%s, %s), WHERE nome=%s"
    t0 = time.time()
    """ update = []
    insert = []
    df = db.replace(np.nan, "")
    print(df['id'])
    adicionar = adicionar.replace(np.nan, "")
    for i, n in enumerate(adicionar['nome']):
        index = df.index[df['nome'] == n].tolist()
        if not index:
            insert.append(adicionar.iloc[i][['nome', 'estado', 'cidade', 'mercado', 'stacks']].tolist())
        else:
            for col in adicionar.columns:
                if col != 'nome' and col != 'estado' and col != 'cidade' and col != 'id':
                    adicionar[col][i] = ", ".join(set((adicionar[col][i] + ', ' + df[col][index[0]]).split(', ')))
            up = adicionar.iloc[i][['mercado', 'stacks']].tolist()
            up.append(df['id'][index[0]])
            update.append(up)
        if i == 20:
            break
    
    print(update[0],len(update))
    log = Log()
    log.cursor.executemany(frase, insert)
    teste = []
    for i in range (0,50):
        teste.append(['mercado','stacsksss',i])
    log.cursor.executemany(frase2, teste) """

    aggregation_db = {'estado': 'first', 'cidade': 'first', 'mercado': agg, 'stacks': agg}
    for col in db.columns:
        if col not in aggregation_db.keys():
            aggregation_db[col] = 'first'
    
    adicionar = pd.concat([db, adicionar], axis=0, ignore_index=True)
    adicionar = adicionar.groupby(['nome'], as_index=False).aggregate(aggregation_db)
    adicionar.reset_index(drop=True, inplace=True)

    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWD")

    sql = f'mysql+pymysql://{user}:{password}@{host}:3306/decasoft_xavier'
    engine = create_engine(sql, echo=False)


    adicionar['id'] = adicionar.index
    adicionar.to_sql("empresa_merge_teste", engine, if_exists='replace', index=False)
    with engine.connect() as con:
        con.execute('ALTER TABLE `empresa_merge_teste` ADD PRIMARY KEY (id);')
    t1 = time.time()
    total = t1-t0
    print("total time 2 = " + str(total))

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

    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWD")

    sql = f'mysql+pymysql://{user}:{password}@{host}:3306/decasoft_xavier'
    engine = create_engine(sql, echo=False)


    adicionar['id'] = adicionar.index
    adicionar.to_sql("tb_usuario3", engine, if_exists='replace', index=False)
    with engine.connect() as con:
        con.execute('ALTER TABLE `tb_usuario3` ADD PRIMARY KEY (id);')
    t1 = time.time()
    total = t1-t0
    print("total time 1 = " + str(total))

    update_db(adicionar)
    
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
