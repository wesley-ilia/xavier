import pandas
import os
from dotenv import load_dotenv
from Log import Log

if (__name__ == "__main__"):
	load_dotenv(dotenv_path='login.env')
	log = Log()
	query = input("Query: ")
	out_csv = input("Endereço de saida: ")
	log.save_to_csv(query, log.con, out_csv)

	version = "0.0.1"
	df = pandas.read_csv(out_csv)
	result_csv = str(df.to_csv(header=False, index=False)).replace('\'', '')

	query = query.replace('\'', '')
	obs = input("obs: ")
	log.insert_into_log(query, version, result_csv, obs)
	log.con.close()
