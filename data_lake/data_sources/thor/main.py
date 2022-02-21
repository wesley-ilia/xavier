from s3 import S3
import pandas as pd
from os import getenv
from thor_bot import get_all


def delivery(data):
    df = pd.DataFrame(
        data,
        columns=[
                'name', 'stacks'])
    send = S3()
    send.send_to_s3(
            df=df,
            bucket_name=getenv('BUCKET_NAME'),
            destination=getenv('DESTINATION')
            )


if __name__ == "__main__":
    data = get_all()
    delivery(data)
