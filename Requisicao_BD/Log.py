import pymysql
import pandas
import os
import sys

class Log():
	def __init__(self):
		self.host = os.getenv("HOSTNAME_DB")
		self.user = os.getenv("USER_DB")
		self.password = os.getenv("PASSWD")
		self.connect_db()
		self.cursor = self.con.cursor()

	def connect_db(self):
		try:
			self.con = pymysql.connect(
					host=self.host,
					user=self.user,
					password=self.password,
					database="decasoft_xavier"
				)
		except BaseException:
			print("Informações de login erradas")
			sys.exit(os.EX_IOERR)

	def save_to_csv(self, query, con, file):
		try:
			results = pandas.read_sql_query(query, con)
			results.to_csv(file, index=False)
		except BaseException:
			print("Informações da query erradas")
			sys.exit(os.EX_IOERR)

	def insert_into_log(self, query:str, version:str, result_csv:str, obs:str):
		self.cursor.execute(f"INSERT INTO logs (query, version, result, obs) VALUES ('{query}', '{version}', '{result_csv}', '{obs}')")
		self.con.commit()

	def set_feedback(self, query="SELECT * FROM logs WHERE opinion IS NULL limit 1"):
		self.cursor.execute(query)
		myresult = self.cursor.fetchone()
		opinion = input("A pesquisa de " + str(myresult[6]) + " foi satisfatoria? ").lower()
		self.cursor.execute(f"UPDATE logs SET opinion='{opinion}' WHERE id='{myresult[0]}'")
		self.con.commit()
