from thor_bot import get_all
import pandas as pd
from s3 import S3


data = get_all()
df = pd.DataFrame(
    data,
    columns=[
            'name', 'stacks'])
print(df)
send = S3(df=df)
send.send_to_s3(
        bucker_name='ilia-ecole42-xavier',
        destination='raw_data/thor.parquet'
        )
