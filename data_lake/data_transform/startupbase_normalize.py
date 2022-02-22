from unidecode import unidecode
from pandas import DataFrame, read_parquet


def format_to_ascii_characters(column_name: str, df: DataFrame):
    df[column_name] = df[column_name].str.lower().str.strip()
    df[column_name] = [unidecode(one) for one in df[column_name]]


def remove_null_values(df: DataFrame):
    df.loc[df['mercado'] == 's/n', 'mercado'] = None
    df.loc[df['modelo'] == 's/n', 'modelo'] = None
    df.loc[df['momento'] == 's/n', 'momento'] = None
    df.loc[df['tamanho'] == 'n/d', 'tamanho'] = None
    df.loc[df['modelo de receita'] == 's/n', 'modelo de receita'] = None
    df.loc[df['segmento'] == 's/n', 'segmento'] = None
    df.loc[df['tamanho'] == '(nao informado)', 'tamanho'] = None


def make_columns_city_state(df: DataFrame):
    df['estado'] = ['' for row in df['name']]
    df['cidade'] = ['' for row in df['name']]

    for i in range(len(df['name'])):
        ci_es = df['cidade_estado'][i]
        ci_es = str(ci_es).split(' - ')
        if len(ci_es) >= 2:
            df['estado'][i] = unidecode(ci_es[1])
            df['cidade'][i] = unidecode(ci_es[0])


def startupbase_normalize():
    df = read_parquet('./raw_data/startupbase.parquet')
    df['name'] = df['name'].str.lower().str.strip()
    df['momento'] = df['momento'].str.lower().str.strip()
    for column in filter(lambda x: x not in {'name', 'redes'}, df.columns):
        format_to_ascii_characters(column, df)
    remove_null_values(df)
    make_columns_city_state(df)
    df = df.drop(['cidade_estado', 'redes'], axis=1)
    df.to_parquet("./clean_data/startupbase.parquet", index=False)
