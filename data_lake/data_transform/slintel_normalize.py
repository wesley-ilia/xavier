import pandas as pd


def slintel_normalize():
    df = pd.read_parquet('./raw_data/slintel.parquet')

    df['name'] = df['name'].str.lower().str.strip()
    for index, lst in enumerate(df['stacks']):
        df['stacks'][index] = list(
                set([string.lower().strip() for string in lst]))

    df.to_parquet("./clean_data/slintel.parquet", index=False)
