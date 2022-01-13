from selenium_bot import startupbase
from beautiful_bot import get_all_infos
import pandas as pd
import numpy as np
from s3 import S3


def get_all_pages_data(bodys: list):
    data = list()
    for body in bodys:
        try:
            data.append(get_all_infos(body))
        except BaseException:
            pass
    return data


with startupbase() as driver:
    driver.land_page()
    driver.scroll_down()
    links = driver.get_page_links()
    bodys = driver.get_body_requests(links)

data = get_all_pages_data(bodys)

df = pd.DataFrame(
    np.array(data, dtype=object),
    columns=[
            'name', 'cidade_estado', 'mercado',
            'modelo', 'modelo de receita',
            'momento', 'tamanho', 'segmento', 'redes', 'website'])

send = S3(df=df)
send.send_to_s3(
        bucker_name='ilia-ecole42-xavier',
        destination='raw_data/startup.parquet'
        )
