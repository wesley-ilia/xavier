import pandas as pd
from sqlalchemy import create_engine
from os import getenv


def narray_colunm_to_list(column) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


df = pd.read_parquet('./raw_data/slintel.parquet')
df.to_parquet("test.parquet", index=False)

df['name'] = df['name'].str.strip()
for index, lst in enumerate(df['stacks']):
    df['stacks'][index] = list(set([string.lower().strip() for string in lst]))

host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(
        url=f'postgresql://{user}:{passwd}@{host}:{port}/{database}'
        )
df.to_parquet("./clean_data/slintel.parquet", index=False)
