import pandas as pd
from sqlalchemy import create_engine
from unidecode import unidecode
import os


def narray_colunm_to_list(column: pd) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


# 'name', 'cidade', 'contato', 'stacks',
# 'mercado', 'tamanho', 'redes', 'website'
df = pd.read_parquet('./raw_data/codesh.parquet')

narray_colunm_to_list(df['stacks'])
narray_colunm_to_list(df['redes'])

df['name'] = df['name'].str.lower().str.strip()

for i, lst in enumerate(df['stacks']):
    df['stacks'][i] = \
        [unidecode(string.lower().strip()) for string in df['stacks'][i]]

df['cidade'] = \
    [unidecode(string.lower().strip()) for string in df['cidade'].values]
df['contato'] = \
    [unidecode(string.lower().strip()) for string in df['contato'].values]
df['mercado'] = \
    [unidecode(string.lower().strip()) for string in df['mercado'].values]

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
    if contato in estados_dict.keys():
        df['estado'][i] = estados_dict[contato]
    else:
        df['estado'][i] = contato

host = os.getenv('DBHOST')
user = os.getenv('DBUSER')
passwd = os.getenv('DBPASS')
port = os.getenv('DBPORT')
database = os.getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')
df.to_parquet("./clean_data/codesh.parquet", index=False)
