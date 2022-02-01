import pandas as pd
from os import getenv
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv(dotenv_path='login.env')

host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')

conn = engine.connect()
data = [['', '', '', '', '']]
columns = ['nome', 'estatdo', 'cidade', 'mercado', 'stacks']

df = pd.DataFrame(data, columns=columns)
print(df)
df.to_sql('user', engine, if_exists='replace', index=False)