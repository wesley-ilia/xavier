from thor_bot import get_all
import pandas as pd


data = get_all()
df = pd.DataFrame(
    data,
    columns=[
            'name', 'stacks'])

df.to_parquet('../data_files/thor.parquet')
