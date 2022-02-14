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

def search_autocomplete(empresa: str):
	url = ("https://maps.googleapis.com/maps/api/place/autocomplete/json?" +
	f"input={empresa}&types=establishment&key={apiKey}")

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)
	return response.json()

def search_text(empresa: str):
	url = ("https://maps.googleapis.com/maps/api/place/textsearch/json?" +
	f'query="{empresa}"&key={apiKey}')

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)
	return response.json()

def get_city_state2(description: str):
	address_list = description.split(',')
	print(address_list)
	city_state = address_list[-2].strip().split('-')
	city = city_state[0].strip()
	state = city_state[1].replace('State of', '').strip()
	return city, state

def get_city_state(formatted_address: str):
	address_list = formatted_address.split(',')
	city_state = address_list[-3].strip().split('-')
	city = city_state[0].strip()
	state = city_state[1].strip()
	return city, state

# counter = 0
# for i, nome in enumerate(db['nome']):
# 	response = search_text(nome + ' in Brasil')
# 	city, state = 'nada', 'nada'
	
# 	if response['status'] == 'OK':
# 		city, state = get_city_state(response['results'][0]['formatted_address'])
# 	if not pd.isna(db['cidade'][i]):
# 		print('---------------------------')
# 		print('nome = ', db['nome'][i])
# 		print('cidade achada = ', city)
# 		print('cidade do banco = ', db['cidade'][i])
# 		if db['cidade'][i]== city.lower():
# 			counter += 1
# 	if i == 20:
# 		break
# print('acertos ', counter)


counter = 0
for i, nome in enumerate(db['nome']):
	if pd.isna(db['estado'][i]):
		print('i =', i)
		response = search_text(nome + ' in Brasil')
		
		if response['status'] == 'OK':
			city, state = get_city_state(response['results'][0]['formatted_address'])
			counter += 1
			db['estado'][i] = state
			db['cidade'][i] = city

		if counter == 20:
			break

db.to_sql("main", engine, if_exists='replace', index=False)