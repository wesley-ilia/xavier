import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import getenv

def convert_str_to_list(strin: str) -> list:
    strin = strin.replace('{', '')
    strin = strin.replace('}', '')
    strin = strin.replace('"', '')
    return strin.split(sep=',')


load_dotenv(dotenv_path='./login.env')
host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(
        url=f'postgresql://{user}:{passwd}@{host}:{port}/{database}', echo=False)

data = dict()

df_startup = pd.read_sql(sql='startupbase', con=engine)

for i, nome in enumerate(df_startup['name']):
    data[nome] = {
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


for i, nome in enumerate(df_slintel['name']):
    data[nome]['stacks'] = convert_str_to_list(df_slintel['stacks'][i])

df_thor = pd.read_sql(sql='programathor', con=engine)

for i, nome in enumerate(df_thor['name']):
    if nome in data.keys():
        data[nome]['stacks'] = \
            list(set(data[nome]['stacks'] +
                 convert_str_to_list(df_thor['stacks'][i])))
    else:
        data[nome] = dict()
        data[nome]['stacks'] = list(set(convert_str_to_list(
            df_thor['stacks'][i])))

df_codesh = pd.read_sql(sql='codesh', con=engine)

for i, nome in enumerate(df_codesh['name']):
    if nome in data.keys():
        if 'mercado' not in data[nome].keys():
            data[nome]['mercado'] = []

        data[nome]['mercado'] = list(set(
            data[nome]['mercado'] + convert_str_to_list(
                df_codesh['mercado'][i])))

        data[nome]['stacks'] = list(set(
            data[nome]['stacks'] + convert_str_to_list(
                df_codesh['stacks'][i])))
    
        data[nome]['website'] = df_codesh['website'][i]
        data[nome]['cidade'] = df_codesh['cidade'][i]
        data[nome]['estado'] = df_codesh['estado'][i]
        data[nome]['tamanho'] = df_codesh['tamanho'][i]
    else:
        data[nome] = {
            'mercado':   convert_str_to_list(df_codesh['mercado'][i]),
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

def if_not_list_exists(data: dict, text: str):
    if text in data.keys():
        back = ", ".join([i for i in data[text] if i])
    else:
        back = None
    return back

real = list()

for i, nome in enumerate(data):
    mercado = if_not_list_exists(data[nome], 'mercado')
    stacks = if_not_list_exists(data[nome], 'stacks')
    cidade = if_not_exists(data[nome], 'cidade')
    estado = if_not_exists(data[nome], 'estado')
    tamanho = if_not_exists(data[nome], 'tamanho')
    receita = if_not_exists(data[nome], 'modelo de receita')
    momento = if_not_exists(data[nome], 'momento')
    website = if_not_exists(data[nome], 'website')
    real.append([nome, stacks, cidade, estado,
                tamanho, receita,  mercado, momento, website])

df = pd.DataFrame(real, columns=['nome','stacks',
                                 'cidade', 'estado', 'tamanho',
                                 'receita', 'mercado', 'momento', 'website'])

print(df)
# with engine.connect() as connection:
#     result = connection.execute(text("DROP TABLE IF EXISTS main"))
print('antes')

df.to_sql("main2", engine, if_exists='replace', index=False)
print('depois')