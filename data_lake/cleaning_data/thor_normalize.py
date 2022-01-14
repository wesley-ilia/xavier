import pandas as pd
from sqlalchemy import create_engine
from collections import Counter
from dotenv import load_dotenv
import os


def narray_colunm_to_list(column: pd) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


def lower_and_strip_datas(df: pd) -> None:
    df['name'] = df['name'].str.lower().str.strip()
    for i, array in enumerate(df['stacks']):
        df['stacks'][i] = ','.join([stack.lower().strip() for stack in array])
    return None


def remove_duplicates(df: pd) -> None:
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df


def merge_duplicates(array: pd):
    new_list = list()
    for stacks in array['stacks']:
        new_list.extend(stacks)
    return new_list


load_dotenv('../../login.env')
host = os.getenv('DBHOST')
user = os.getenv('DBUSER')
passwd = os.getenv('DBPASS')
port = os.getenv('DBPORT')
database = os.getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')

df = pd.read_parquet('./raw_data/thor.parquet')

narray_colunm_to_list(df['stacks'])
lower_and_strip_datas(df)
df = remove_duplicates(df)

for i, stack in enumerate(df['stacks']):
    df['stacks'][i] = list(stack.split(','))

to_merge = df['name'].tolist()
to_merge = [item for item, count in Counter(to_merge).items() if count > 1]

for i, name in enumerate(to_merge):
    array = df.loc[df['name'] == name]
    array = merge_duplicates(array)
    df = df.loc[df['name'] != name]
    df2 = pd.DataFrame(
        [[name, array]], columns=['name', 'stacks'])
    df = df.append(df2)

df = df.reset_index(drop=True)

df.to_sql('programathor', engine, if_exists='replace', index=False)
