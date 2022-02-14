import pandas as pd


def narray_colunm_to_list(column) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


df = pd.read_parquet('./raw_data/slintel.parquet')

df['name'] = df['name'].str.strip()
for index, lst in enumerate(df['stacks']):
    df['stacks'][index] = list(set([string.lower().strip() for string in lst]))

df.to_parquet("./clean_data/slintel.parquet", index=False)
