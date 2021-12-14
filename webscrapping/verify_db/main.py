from dotenv import load_dotenv
from Log import Log
import json

def status_startupbase(name):
	f = open(name,'r')
	log = Log()
	data = json.load(f)
	for i in data:
		if not log.insert_in_db("Select * from control_startupbase where name like '%"+i['name']+"%'"):
			log.insert_in_db(f"Insert into control_startupbase (name, link, status)\
VALUES ('{i['name']}','{i['link']}','NOVO')")
			log.con.commit()
			print(i['name'])
	f.close()

if __name__ == '__main__':
	load_dotenv(dotenv_path='../../login.env')
	status_startupbase("scrapping_json/startupbase2.json")
