from s3 import S3
import numpy as np
from os import getenv
from time import sleep
from pandas import DataFrame
import concurrent.futures as cf
from selenium_bot import StartupBase
from selenium.webdriver.common.by import By


def delivery(data: list):
    df = DataFrame(
        np.array(data, dtype=object),
        columns=[
                'name', 'cidade_estado', 'mercado',
                'modelo', 'modelo de receita',
                'momento', 'tamanho', 'segmento', 'redes', 'website'
                ])
    s3 = S3(df=df)
    s3.send_to_s3(
            bucker_name=getenv("BUCKET_NAME"),
            destination=getenv("DEST_PARQUET")
            )


def get_bodys_pages(link: str):
    with StartupBase(headless=True) as bot:
        bot.get(link)
        sleep(2)
        html = bot.page_source
    return html


def select_state(bot: StartupBase, num):
    bot.find_element(
            by=By.CSS_SELECTOR,
            value='app-panel[name="Estado"] > div > p'
            ).click()
    sleep(1)
    bot.find_element(
            by=By.CSS_SELECTOR,
            value='button.ais-RefinementList-showMore'
            ).click()
    sleep(1)
    bot.find_elements(
            by=By.CSS_SELECTOR,
            value='li[class="ais-RefinementList-item"]'
            )[num].click()
    sleep(1)


def to_do_process(num) -> list:
    with StartupBase(headless=True) as bot:
        bot.land_page()
        select_state(bot, num)
        bot.scroll_down()
        links = bot.get_page_links()
    return links


def make_parquet(data: list, name_parquet: str):
    df = DataFrame(
            data=np.array(data, dtype=object),
            columns=['links']
            )
    df.to_parquet(name_parquet, index=False)


def get_links(name_parquet: str):
    dt = set()
    with cf.ProcessPoolExecutor() as exec:
        data = exec.map(to_do_process, (state for state in range(27)))
    dt.update(*data)
    make_parquet(list(dt), name_parquet)
