import pandas as pd
from unidecode import unidecode

df = pd.read_parquet('./raw_data/startupbase.parquet')


def normalize(column_name: str, df: pd.DataFrame):
    df[column_name] = df[column_name].str.lower().str.strip()
    df[column_name] = [unidecode(one) for one in df[column_name]]


df['name'] = df['name'].str.lower().str.strip()
df['momento'] = df['momento'].str.lower().str.strip()

normalize('cidade_estado', df)
normalize('segmento', df)
normalize('mercado', df)
normalize('modelo', df)
normalize('momento', df)
normalize('tamanho', df)
normalize('modelo de receita', df)

df.loc[df['mercado'] == 's/n', 'mercado'] = None
df.loc[df['modelo'] == 's/n', 'modelo'] = None
df.loc[df['momento'] == 's/n', 'momento'] = None
df.loc[df['tamanho'] == 'n/d', 'tamanho'] = None
df.loc[df['modelo de receita'] == 's/n', 'modelo de receita'] = None
df.loc[df['segmento'] == 's/n', 'segmento'] = None
df.loc[df['tamanho'] == '(nao informado)', 'tamanho'] = None

df['estado'] = ['' for row in df['name']]
df['cidade'] = ['' for row in df['name']]

for i in range(len(df['name'])):
    ci_es = df['cidade_estado'][i]
    ci_es = str(ci_es).split(' - ')
    if len(ci_es) >= 2:
        df['estado'][i] = unidecode(ci_es[1])
        df['cidade'][i] = unidecode(ci_es[0])

df = df.drop(['cidade_estado', 'redes'], axis=1)

df.to_parquet("./clean_data/startupbase.parquet", index=False)
