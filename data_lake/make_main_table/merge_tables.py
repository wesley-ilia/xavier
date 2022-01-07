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
df_startup = pd.read_sql(sql='startupBase', con=engine)


data = dict()

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


print(json.dumps(data, indent=4))

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
