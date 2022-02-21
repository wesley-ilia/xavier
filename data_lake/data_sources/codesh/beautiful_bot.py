import requests
from bs4 import BeautifulSoup


def get_body_html(perfil_url: str):
    response = requests.get(perfil_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_perfil_infos(companies: dict):
    for company in companies:
        # Will get that principal div where all the importants
        # information will be get it.
        soup = get_body_html(companies[company]['perfil'])
        big_box = soup.select('div[class="shadow-sm mb-5 card"]')[0]

        # will get from the principal div
        # a div where has most of the imformation
        mid_box = big_box.select('div[class="px-5"]')[0]

        infos = mid_box.find_all('div', class_='text-center')
        companies[company]['cidade'] = infos[0].find('span').text
        companies[company]['fundacao'] = infos[1].find('span').text
        companies[company]['tamanho'] = infos[2].find('span').text
        companies[company]['mercado'] = infos[3].find('span').text

        redes = mid_box.find_all('a')
        companies[company]['redes'] = [href['href'] for href in redes]

        # will get from the princilap div a div where has website inforamtion
        top_box = big_box.find('div', {"class": "border-bottom"})
        web_site = top_box.select('div[class="mb-4"] > a')[0]['href']
        companies[company]['website'] = web_site


def get_cidade_second_page(companies):
    for company in companies:
        soup = get_body_html(companies[company]['vagas'])
        contato = soup.find('address', {"class": "jsx-3539478241"})
        companies[company]['contato'] = contato.text
