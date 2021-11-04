import pymysql
import pandas
import os

def connect_db():
	try:
		my_db = pymysql.connect(
			host="192.185.223.65",
			user="decasoft_42",
			password="42Labs@@",
			database="decasoft_xavier"
			)
		return my_db

	except:
		print("Informações erradas")

def save_to_csv(query, con, file):
	results = pandas.read_sql_query(query, con)
	results.to_csv(file, index=False)

if (__name__ == "__main__"):
	con = connect_db()

	out_csv = "out.csv"
	query = "SELECT nome FROM empresas WHERE 1"
	save_to_csv(query, con, out_csv)

	cursor = con.cursor()

	df = pandas.read_csv(out_csv)
	#df.to_sql("logs", con, if_exists='append', index=False)

	version="0.0.1"
	result_csv = str(df.to_csv(header=False, index=False)).replace('\'', '')
	cursor.execute(f"INSERT INTO logs (query, version, result) VALUES ('{query}', '{version}', '{result_csv}')")
	con.commit()

	con.close()