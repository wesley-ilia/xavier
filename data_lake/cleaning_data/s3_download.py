import boto3
import os
import configparser


def download_file_from_s3(name: str) -> None:
    s3.download_file(
        'ilia-ecole42-xavier',
        f'raw_data/{name}.parquet',
        f'raw_data/{name}.parquet')
    return None


config = configparser.ConfigParser()
path = os.path.join(os.path.expanduser('~'), '.aws/credentials')
config.read(path)

# pegando as chaves e a regiào para o projeto xavier
aws_access_key_id = config.get('ilia-ecole42-xavier', 'aws_access_key_id')
aws_secret_access_key = config.get(
    'ilia-ecole42-xavier', 'aws_secret_access_key')
aws_region = config.get('ilia-ecole42-xavier', 'aws_region')

# inicializando o cliente boto3
boto3.setup_default_session(
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )

# definindo o recurso da aws que será usado
s3 = boto3.client('s3')

# pegando todos os objetos do bucket da pasta users
response = s3.list_objects(
    Bucket='ilia-ecole42-xavier',
    Prefix='users',
    )

path = './raw_data'
if os.path.exists(path) is False:
    os.makedirs(path)

download_file_from_s3('thor')
download_file_from_s3('codesh')
download_file_from_s3('startup')
