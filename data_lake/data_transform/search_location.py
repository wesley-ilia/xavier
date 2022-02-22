import requests
from os import getenv
from sqlalchemy import create_engine
import pandas as pd
from unidecode import unidecode


def search_text(empresa: str, apiKey: str):
    url = ("https://maps.googleapis.com/maps/api/place/textsearch/json?" +
           f'query="{empresa}"&key={apiKey}')

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_city_state(formatted_address: str):
    address_list = formatted_address.split(',')
    city_state = address_list[-3].strip().split('-')
    try:
        city = city_state[0].strip()
        state = city_state[1].strip()
        return city, state
    except IndexError:
        print(formatted_address)
        return '', city_state[0].strip()


def search_location(limit: int = 10000):
    apiKey = getenv('APIKEY')

    host = getenv('DBHOST')
    user = getenv('DBUSER')
    passwd = getenv('DBPASS')
    port = getenv('DBPORT')
    database = getenv('DBNAME')

    engine = create_engine(f'postgresql://{user}:{passwd}\
    @{host}:{port}/{database}')

    db = pd.read_sql_table("main", engine)

    counter = 0
    for i, nome in enumerate(db['nome']):
        if pd.isna(db['estado'][i]):
            print(nome)
            response = search_text(nome + ' in Brasil', apiKey)
            if response['status'] == 'OK':
                city, state = get_city_state(
                        response['results'][0]['formatted_address'])
                counter += 1
                db['estado'][i] = state.lower().strip()
                db['cidade'][i] = unidecode(city.lower().strip())

            if counter == limit - 1:
                break

    db.to_sql("main", engine, if_exists='replace', index=False)
