import pandas as pd
from unidecode import unidecode
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

df = pd.read_parquet('./raw_data/startup.parquet')

df['name'] = df['name'].str.lower().str.strip()

df['cidade_estado'] = df['cidade_estado'].str.lower().str.strip()
df['cidade_estado'] = [unidecode(one) for one in df['cidade_estado']]

df['mercado'] = df['mercado'].str.lower().str.strip()
df['mercado'] = [unidecode(mercado) for mercado in df['mercado']]

df['modelo'] = df['modelo'].str.lower().str.strip()
df['modelo'] = [unidecode(modelo) for modelo in df['modelo']]

df['momento'] = df['momento'].str.lower().str.strip()
df['momento'] = [unidecode(momento) for momento in df['momento']]

df['tamanho'] = df['tamanho'].str.lower().str.strip()
df['tamanho'] = [unidecode(tamanho) for tamanho in df['tamanho']]

df['modelo de receita'] = df['modelo de receita'].str.lower().str.strip()
df['modelo de receita'] = [unidecode(modelo_receita) for modelo_receita in df['modelo de receita']]

df['segmento'] = df['segmento'].str.lower().str.strip()
df['segmento'] = [unidecode(segmento) for segmento in df['segmento']]

df.loc[df['mercado'] == 's/n', 'mercado'] = None
df.loc[df['modelo'] == 's/n', 'modelo'] = None
df.loc[df['momento'] == 's/n', 'momento'] = None
df.loc[df['tamanho'] == 'n/d', 'tamanho'] = None
df.loc[df['modelo de receita'] == 's/n', 'modelo de receita'] = None
df.loc[df['segmento'] == 's/n', 'segmento'] = None
df.loc[df['tamanho'] == '(nao informado)', 'tamanho'] = None

df['momento'] = df['momento'].str.lower().str.strip()

df['estado'] = ['' for row in df['name']]
df['cidade'] = ['' for row in df['name']]

for i in range(len(df['name'])):
    ci_es = df['cidade_estado'][i]
    ci_es = str(ci_es).split(' - ')
    if len(ci_es) >= 2:
        df['estado'][i] = unidecode(ci_es[1])
        df['cidade'][i] = unidecode(ci_es[0])

df = df.drop(['cidade_estado', 'redes'], axis=1)

load_dotenv('login.env')
host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{database}')
df.to_sql("startupBase", engine, if_exists='replace', index=False)
