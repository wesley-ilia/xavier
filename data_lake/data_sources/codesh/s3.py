from io import BytesIO
from os import getenv
from pandas import DataFrame
from boto3 import setup_default_session, client


class S3:
    def __init__(self, df: DataFrame):
        self.client = self.__create_session()
        self.df = df

    def __create_session(self):
        setup_default_session(
                region_name=getenv('AWS_REGION'),
                aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
                )
        return client('s3')

    def send_to_s3(self, bucket_name: str, destination: str) -> int:
        with BytesIO() as buffer:
            self.df.to_parquet(buffer, index=False)
            response = self.client.put_object(
                    Bucket=bucket_name,
                    Key=destination,
                    Body=buffer.getvalue()
                    )
        return response.get("ResponseMetadata", {}).get("HTTPStatusCode")
