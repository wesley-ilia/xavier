from os import path
from io import BytesIO
from pandas import DataFrame
from configparser import ConfigParser
from boto3 import setup_default_session, client


class S3:
    def __init__(self, df: DataFrame):
        self.credentials = self.__parsing_config()
        self.client = self.__create_session()
        self.df = df

    def __parsing_config(self) -> dict:
        config = ConfigParser()
        _path = path.join(path.expanduser('~'), '.aws/credentials')
        config.read(_path)
        credentials = {
                'aws_access_key_id': config.get(
                    'ilia-ecole42-xavier', 'aws_access_key_id'),
                'aws_secret_access_key': config.get(
                    'ilia-ecole42-xavier', 'aws_secret_access_key'),
                'aws_region': config.get('ilia-ecole42-xavier', 'aws_region')
                }
        return credentials

    def __create_session(self):
        setup_default_session(
                region_name=self.credentials['aws_region'],
                aws_access_key_id=self.credentials['aws_access_key_id'],
                aws_secret_access_key=self.credentials['aws_secret_access_key']
                )
        return client('s3')

    def send_to_s3(self, bucker_name: str, destination: str) -> int:
        with BytesIO() as buffer:
            self.df.to_parquet(buffer, index=False)
            response = self.client.put_object(
                    Bucket=bucker_name,
                    Key=destination,
                    Body=buffer.getvalue()
                    )

        return response.get("ResponseMetadata", {}).get("HTTPStatusCode")
