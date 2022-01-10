import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv


def convert_str_to_list(strin: str) -> list:
    strin = strin.replace('{', '')
    strin = strin.replace('}', '')
    strin = strin.replace('"', '')
    return strin.split(sep=',')


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


for i, company in enumerate(df_slintel['name']):
    data[company]['stacks'] = convert_str_to_list(df_slintel['stacks'][i])

df_thor = pd.read_sql(sql='programathor', con=engine)

for i, company in enumerate(df_thor['name']):
    if company in data.keys():
        data[company]['stacks'] = \
            list(set(data[company]['stacks'] +
                 convert_str_to_list(df_thor['stacks'][i])))
    else:
        data[company] = dict()
        data[company]['stacks'] = list(set(convert_str_to_list(
            df_thor['stacks'][i])))

df_codesh = pd.read_sql(sql='codesh', con=engine)

for i, company in enumerate(df_codesh['name']):
    if company in data.keys():
        if 'mercado' not in data[company].keys():
            data[company]['mercado'] = []
        data[company]['mercado'] = list(set(
            data[company]['mercado'] + [df_codesh['mercado'][i]]))
        data[company]['stacks'] = list(set(
            data[company]['stacks'] + convert_str_to_list(
                df_codesh['stacks'][i])))
        data[company]['website'] = df_codesh['website'][i]
        data[company]['cidade'] = df_codesh['cidade'][i]
        data[company]['estado'] = df_codesh['estado'][i]
        data[company]['tamanho'] = df_codesh['tamanho'][i]
    else:
        data[company] = {
            'mercado':   [df_codesh['mercado'][i]],
            'stacks':   convert_str_to_list(df_codesh['stacks'][i]),
            'cidade':   df_codesh['cidade'][i],
            'estado':   df_codesh['estado'][i],
            'tamanho':   df_codesh['tamanho'][i],
            'website':   df_codesh['website'][i]
        }


def if_not_exists(data: dict, text: str):
    if text in data.keys():
        back = data[text]
    else:
        back = None
    return back


real = list()

for i, company in enumerate(data):
    mercado = if_not_exists(data[company], 'mercado')
    stacks = if_not_exists(data[company], 'stacks')
    cidade = if_not_exists(data[company], 'cidade')
    estado = if_not_exists(data[company], 'estado')
    tamanho = if_not_exists(data[company], 'tamanho')
    receita = if_not_exists(data[company], 'modelo de receita')
    momento = if_not_exists(data[company], 'momento')
    website = if_not_exists(data[company], 'website')
    real.append([company, stacks, cidade, estado,
                tamanho, receita, momento, website])

df = pd.DataFrame(real, columns=['company', 'stacks',
                                 'cidade', 'estado', 'tamanho',
                                 'receita', 'momento', 'website'])

df.to_sql("main", engine, if_exists='replace', index=False)
