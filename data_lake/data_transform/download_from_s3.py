import os
from s3 import S3


def download_file_from_s3(name: str):
    with S3() as s3_obj:
        s3_obj.download_from_s3(
                bucket_name=os.getenv('BUCKET_NAME'),
                obj_name=os.getenv('OBJ_NAME'),
                name=name
                )


if __name__ == "__main__":
    path = './raw_data'
    if os.path.exists(path) is False:
        os.makedirs(path)

    download_file_from_s3('thor')
    download_file_from_s3('codesh')
    download_file_from_s3('startupbase')
    download_file_from_s3('slintel')
