import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from unidecode import unidecode
import os


# 'name', 'cidade', 'contato', 'stacks', 'mercado', 'tamanho', 'redes', 'website'
df = pd.read_parquet('./raw_data/codesh.parquet')

df['name'] = df['name'].str.lower().str.strip()

# cidades = ['sao paulo', 'Sao Paulo', 'são Paulo', 'São Paulo']

for i, city in enumerate(df['cidade']):
    df['cidade'][i] = unidecode(city.lower().strip())

for i, city in enumerate(df['cidade']):
    df['cidade'][i] = unidecode(city.lower().strip())

# print(json.dumps(city_json, indent=2))
for i, lst in enumerate(df['stacks'].values):
    df['stacks'][i] = [unidecode(string.lower().strip()) for string in df['stacks'][i]]

df['mercado'] = [unidecode(string.lower().strip()) for string in df['mercado'].values]

estados_dict = {
        "acre": "ac",
        "alagoas": "al",
        "amapa": "ap",
        "amazonas": "am",
        "bahia": "ba",
        "ceara": "ce",
        "distrito federal": "df",
        "espirito santo": "es",
        "goias": "go",
        "maranhao": "ma",
        "mato grosso": "mt",
        "mato grosso do sul": "ms",
        "minas gerais": "mg",
        "para": "pa",
        "paraiba": "pb",
        "parana": "pr",
        "pernambuco": "pe",
        "piaui": "pi",
        "rio de janeiro": "rj",
        "rio grande do norte": "rn",
        "rio grande do sul": "rs",
        "rondonia": "ro",
        "roraima": "rr",
        "santa catarina": "sc",
        "sao paulo": "sp",
        "sergipe": "se",
        "tocantins": "to"
        }

df['estado'] = df['contato']
for i, contato in enumerate(df['contato']):
    contato = unidecode(contato.split(',')[-2].lower().strip())
    if unidecode(contato) in estados_dict.keys():
        df['estado'][i] = estados_dict[contato]
    else:
        df['estado'][i] = contato
# df = df.loc[df['name'] != name]
# df.to_csv('teste.csv', sep=',', index=False)

load_dotenv('../../login.env')
host = os.getenv('DBHOST')
user = os.getenv('DBUSER')
passwd = os.getenv('DBPASS')
port = os.getenv('DBPORT')
database = os.getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')

df.to_sql("codesh", engine, if_exists='replace', index=False)
