import pandas as pd
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv


def narray_colunm_to_list(column) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


df = pd.read_parquet('./raw_data/slintel.parquet')

df['name'] = df['name'].str.strip()
for index, lst in enumerate(df['stacks']):
    df['stacks'][index] = list(set([string.lower().strip() for string in lst]))

load_dotenv(dotenv_path='../login.env')
host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(
        url=f'postgresql://{user}:{passwd}@{host}:{port}/{database}'
        )

df.to_sql('slintel_test', engine, if_exists='replace', index=False)
