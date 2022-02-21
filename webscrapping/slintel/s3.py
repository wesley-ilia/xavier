from os import getenv
from io import BytesIO
from pandas import DataFrame
from boto3 import setup_default_session, client, resource


class S3:
    def __init__(self):
        self.__create_session()
        self.client = client('s3')
        self.resource = resource('s3')

    def __enter__(self):
        return self

    def __exit__(self, tp, vl, tb):
        del self

    def __create_session(self):
        setup_default_session(
                region_name=getenv('AWS_REGION'),
                aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
                )

    def send_to_s3(self, bucket_name: str, destination: str, df: DataFrame):
        with BytesIO() as buffer:
            df.to_parquet(buffer, index=False)
            responses = self.client.put_object(
                    Bucket=bucket_name,
                    Key=destination,
                    Body=buffer.getvalue()
                    )
        return responses.get("ResponseMetadata", {}).get("HTTPStatusCode")

    def download_from_s3(self, bucket_name: str, obj_name: str, name: str):
        self.client.download_file(
            bucket_name,
            obj_name,
            name
            )
