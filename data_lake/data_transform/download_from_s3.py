from s3 import S3
from const import OBJ_NAME, BUCKET_NAME


def download_file_from_s3(name: str):
    with S3() as s3_obj:
        s3_obj.download_from_s3(
                bucket_name=BUCKET_NAME,
                obj_name=OBJ_NAME + name,
                name='raw_data/' + name
                )


download_file_from_s3('thor.parquet')
download_file_from_s3('codesh.parquet')
download_file_from_s3('startupbase.parquet')
download_file_from_s3('slintel.parquet')
