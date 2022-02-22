import Levenshtein as lev
from sqlalchemy import create_engine
from thor_normalize import thor_normalize
from codesh_normalize import codesh_normalize
from slintel_normalize import slintel_normalize
from const import HOST, USER, PASSWD, PORT, DATABASE
from pandas import read_sql, read_parquet, DataFrame
from startupbase_normalize import startupbase_normalize


engine = create_engine(
        url=f'postgresql://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}',
        echo=False)


def convert_list(lst) -> list:
    if type(lst) == str:
        return convert_str_to_list(lst)
    if lst is None:
        return []
    return list(lst)


def convert_str_to_list(strin: str) -> list:
    strin = strin.replace('{', '')
    strin = strin.replace('}', '')
    strin = strin.replace('"', '')
    strin = [s.strip() for s in strin.split(sep=',')]
    return strin


def substitute_similar(df: DataFrame, compare):
    for i, line in enumerate(df):
        line = line.split(', ')
        line = new_list(line, compare)
        df[i] = ', '.join(line)


def difflibfunction(df: DataFrame):

    palavras_unicas = [
            'node.js', 'react.js', 'next.js', 'vue.js', '.net',
            'angular.js', 'vb.net', 'smart adserver',
            'styled-components', 'design patterns']
    for i, line in enumerate(df):
        if line is not None:
            line = line.split(', ')
            for stack in palavras_unicas:
                line = new_list(line, stack)
            df[i] = ', '.join(line)


def new_list(line, compare):
    original = []
    for i in range(len(line)):
        if lev.ratio(line[i], compare) > 0.9:
            original.append(line[i])
            line[i] = compare
            if (original != [] and (
                    compare not in original or len(original) > 1)):
                if compare in original:
                    original.remove(compare)
    return line


def startupbase_fill_data(data) -> dict:
    df_startup = read_parquet('./clean_data/startupbase.parquet')
    for i, nome in enumerate(df_startup['name']):
        data[nome] = {
                'mercado': [df_startup['mercado'][i],
                            df_startup['segmento'][i]],
                'modelo de receita': df_startup['modelo de receita'][i],
                'cidade': df_startup['cidade'][i],
                'estado': df_startup['estado'][i],
                'website': df_startup['website'][i],
                'tamanho': df_startup['tamanho'][i],
                'modelo': df_startup['modelo'][i],
                'momento': df_startup['momento'][i],
                'referencia': 'startupbase'
                }


def slintel_fill_data(data) -> dict:
    df_slintel = read_parquet('./clean_data/slintel.parquet')
    for i, nome in enumerate(df_slintel['name']):
        if nome in data.keys():
            data[nome]['stacks'] = list(df_slintel['stacks'][i])
            data[nome]['referencia'] += ', slintel'


def thor_fill_data(data) -> dict:
    df_thor = read_parquet('./clean_data/programathor.parquet')

    for i, nome in enumerate(df_thor['name']):
        if nome in data.keys() and 'stacks' in data.keys():
            data[nome]['stacks'] = list(set(
                data[nome]['stacks'] + convert_list(df_thor['stacks'][i])))
        else:
            data[nome] = dict()
            data[nome]['stacks'] = list(set(
                convert_list(df_thor['stacks'][i])))
            data[nome]['referencia'] = 'thor'


def codesh_fill_data(data) -> dict:
    df_codesh = read_parquet('./clean_data/codesh.parquet')
    for i, nome in enumerate(df_codesh['name']):
        if nome in data.keys():
            if 'mercado' not in data[nome].keys():
                data[nome]['mercado'] = list()

            data[nome]['mercado'] = list(set(
                data[nome]['mercado'] + convert_list(df_codesh['mercado'][i])))
            if 'stacks' in data[nome]:
                data[nome]['stacks'] = set(data[nome]['stacks'] + convert_list(
                    df_codesh['stacks'][i]))

            data[nome]['website'] = df_codesh['website'][i]
            data[nome]['cidade'] = df_codesh['cidade'][i]
            data[nome]['estado'] = df_codesh['estado'][i]
            data[nome]['tamanho'] = df_codesh['tamanho'][i]
        else:
            data[nome] = {
                'mercado':   convert_list(df_codesh['mercado'][i]),
                'stacks':   convert_list(df_codesh['stacks'][i]),
                'cidade':   df_codesh['cidade'][i],
                'estado':   df_codesh['estado'][i],
                'tamanho':   df_codesh['tamanho'][i],
                'website':   df_codesh['website'][i],
                'referencia': 'coodesh'
            }


def user_fill_data(data) -> dict:
    df_user = read_sql(sql='user', con=engine)

    for i, nome in enumerate(df_user['nome']):
        if nome in data.keys():
            if 'mercado' not in data[nome].keys():
                data[nome]['mercado'] = list()
            data[nome]['mercado'] = list(set(
                data[nome]['mercado'] + convert_str_to_list(
                    df_user['mercado'][i])))
            if 'stacks' in data[nome]:
                data[nome]['stacks'] = set(
                        data[nome]['stacks'] + convert_str_to_list(
                            df_user['stacks'][i]))
            data[nome]['cidade'] = df_user['cidade'][i]
            data[nome]['estado'] = df_user['estado'][i]
        else:
            data[nome] = {
                'mercado':  convert_str_to_list(df_user['mercado'][i]),
                'stacks':   convert_str_to_list(df_user['stacks'][i]),
                'cidade':   df_user['cidade'][i],
                'estado':   df_user['estado'][i],
                'referencia': 'usuario'
            }


def if_not_exists(data: dict, text: str):
    if text in data.keys():
        back = data[text]
        return back
    return None


def if_not_list_exists(data: dict, text: str):
    if text in data.keys():
        back = ", ".join([i for i in data[text] if i and i != '-'])
        return back
    return None


def make_list_to_send_to_sql(data):
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
        referencia = data[nome]['referencia']
        if nome == 'netfoods':
            print(estado)
        real.append([nome, stacks, cidade, estado,
                    tamanho, receita,  mercado, momento, website, referencia])
    return real


def delivery_to_sql(list_to_send_to_sql: list):
    df = DataFrame(
            list_to_send_to_sql,
            columns=[
                'nome', 'stacks',
                'cidade', 'estado', 'tamanho',
                'receita', 'mercado', 'momento', 'website', 'referencia'
                ])
    difflibfunction(df['stacks'])

    df.to_sql("main", engine, if_exists='replace', index=False)


if __name__ == "__main__":
    codesh_normalize()
    thor_normalize()
    startupbase_normalize()
    slintel_normalize()
    data = {}
    startupbase_fill_data(data)
    slintel_fill_data(data)
    thor_fill_data(data)
    codesh_fill_data(data)
    user_fill_data(data)
    list_to_send_to_sql = make_list_to_send_to_sql(data)
    delivery_to_sql(list_to_send_to_sql)
