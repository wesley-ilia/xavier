import requests
from dotenv import load_dotenv
from os import getenv, remove
from sqlalchemy import create_engine
import pandas as pd

load_dotenv(".env")
apiKey = getenv('APIKEY')

host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')

db = pd.read_sql_table("main", engine)

def search_address(empresa: str):
	url = ("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" + 
	f"input={empresa}&inputtype=textquery&fields=formatted_address&key={apiKey}")

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)
	return response.json()

def get_city_state(formatted_address: str):
	address_list = formatted_address.split(',')
	city_state = address_list[-3].strip().split('-')
	city = city_state[0].strip()
	state = city_state[1].strip()
	return city, state

for i, name in enumerate(db['nome']):
	response = search_address(name + ' Brasil')
	city, state = 'nada', 'nada'
	if response['status'] == 'OK':
		city, state = get_city_state(response['candidates'][0]['formatted_address'])
	if not pd.isna(db['cidade'][i]):
		print('---------------------------')
		print('nome = ', name)
		print('cidade achada = ', city)
		print('cidade do banco = ', db['cidade'][i])
	if i == 20:
		break