from s3 import S3
import pandas as pd
from os import getenv
from selenium_bot import Codesh
from beautiful_bot import get_perfil_infos, get_cidade_second_page

BASE_URL = "https://coodesh.com/vagas"


def convert_to_list(companies: dict):
    data = list()
    for company in companies:
        data.append(
            [company,
                companies[company]['cidade'],
                companies[company]['contato'],
                companies[company]['stacks'],
                companies[company]['mercado'],
                companies[company]['tamanho'],
                companies[company]['redes'],
                companies[company]['website']])
    return data


bot = Codesh(
        headless=True,
        implicit_wait=10,
        )
bot.land_in_page(BASE_URL)
bot.scroll_site()
companies = bot.get_first_page_infos()

get_perfil_infos(companies)
get_cidade_second_page(companies)

data = convert_to_list(companies)

df = pd.DataFrame(
    data,
    columns=[
            'name', 'cidade',
            'contato', 'stacks',
            'mercado', 'tamanho',
            'redes', 'website'])

send = S3()
send.send_to_s3(df=df,
        bucket_name=getenv('BUCKET_NAME'),
        destination=getenv('DESTINATION')
        )
