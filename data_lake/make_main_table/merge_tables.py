import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv(dotenv_path='../login.env')
host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(
        url=f'postgresql://{user}:{passwd}@{host}:{port}/{database}')

data = dict()

df_startup = pd.read_sql(sql='startupbase', con=engine)

for i, company in enumerate(df_startup['name']):
    data[company] = {
            'mercado': [df_startup['mercado'][i], df_startup['segmento'][i]],
            'modelo de receita': df_startup['modelo de receita'][i],
            'cidade': df_startup['cidade'][i],
            'estado': df_startup['estado'][i],
            'website': df_startup['website'][i],
            'tamanho': df_startup['tamanho'][i],
            'modelo': df_startup['modelo'][i],
            'momento': df_startup['momento'][i]
            }

df_slintel = pd.read_sql(sql='slintel_test', con=engine)


# print(df_slintel)
def convert_str_to_list(strin: str) -> list:
    strin = strin.strip("{\}")
    return strin.split(sep=',')

for i, company in enumerate(df_slintel['name']):
    data[company]['stacks'] = convert_str_to_list(df_slintel['stacks'][i])
    print(data[company]['stacks'])

# print(json.dumps(data, indent=4))
# print(data['kapsula']['stacks'])

# df = pd.DataFrame(data=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
#                   columns=['nome',
#                            'estados',
#                            'cidades',
#                            'mercados',
#                            'stacks',
#                            'tamanho',
#                            'websites',
#                            'modelo de receita',
#                            'publico alvo',
#                            'modelo'
#                            ])
