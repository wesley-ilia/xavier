import pandas as pd
import os

def narray_colunm_to_list(column) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


df = pd.read_parquet('./raw_data/slintel.parquet')

df['name'] = df['name'].str.lower().str.strip()
for index, lst in enumerate(df['stacks']):
    df['stacks'][index] = list(set([string.lower().strip() for string in lst]))

path = './clean_data'
if os.path.exists(path) is False:
    os.makedirs(path)

df.to_parquet("./clean_data/slintel.parquet", index=False)
