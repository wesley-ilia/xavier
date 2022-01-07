# importando as bibliotecas
import boto3
import os
import configparser

def upload_file_to_s3(name: str) -> None:
    s3.upload_file(
            f'data_files/{name}.parquet',
            'ilia-ecole42-xavier',
            f'raw_data/{name}.parquet')
    return None

# analisando o arquivo credentials que está na pasta .aws abaixo do home dir
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
upload_file_to_s3('thor')
upload_file_to_s3('startup')
upload_file_to_s3('slintel')
