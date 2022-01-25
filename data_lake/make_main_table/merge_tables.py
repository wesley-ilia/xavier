import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv
import Levenshtein as lev

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
        back = ", ".join([i for i in data[text] if i and i != '-'])
    else:
        back = None
    return back

real = list()

for nome in data:
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

def new_list(line, compare):
    original = []
    for i in range(len(line)):
        if lev.ratio(line[i], compare) > 0.9:
            original.append(line[i])
            line[i] = compare
            if (original != [] and (compare not in original or len(original) > 1)):
                if compare in original:
                    original.remove(compare)
                print(original, compare)
    return line

def substitute_similar(df: pd.DataFrame, compare):
    for i, line in enumerate(df):
        line = line.split(', ')
        
        line = new_list(line, compare)

        df[i] = ', '.join(line)

def difflibfunction(df: pd.DataFrame):

    palavras_unicas = ['node.js', 'react.js', 'next.js', 'vue.js', '.net',
                'angular.js', 'vb.net', 'smart adserver',
                'styled-components', 'design patterns']
    for i, line in enumerate(df):
        line = line.split(', ')
        for stack in palavras_unicas:
            line = new_list(line, stack)
        df[i] = ', '.join(line)

    # for i, line in enumerate(df):
    #     line = line.split(', ')
    #     for word in line:
    #         if word not in palavras_unicas:
    #             palavras_unicas.append(word)
    #             substitute_similar(df, word)

print(lev.ratio('react.js', 'node.js'))

df = pd.DataFrame(real, columns=['nome','stacks',
                                 'cidade', 'estado', 'tamanho',
                                 'receita', 'mercado', 'momento', 'website'])

print("antes da diff")
difflibfunction(df['stacks'])
print('start')
df.to_sql("main4", engine, if_exists='replace', index=False)
print('end')