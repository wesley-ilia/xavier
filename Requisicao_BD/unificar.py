from mySQL_db import MySQL
import pandas as pd
import pymysql
from dotenv import load_dotenv

"""
stmt = "INSERT INTO all_stacks (nome, stack) VALUES (%s, %s)"
	data = []
	ret = []
	for nome, stack in zip(thor_df['nome'],thor_df['stack']):
		stacks = stack.split(",")
		for z in stacks:
			val = z.strip()
			json = (nome, val)
			data.append(json)

    mycursor.executemany(stmt, data)
	con.commit()
"""
load_dotenv(dotenv_path='login.env')

db = MySQL()

query_stacks = "SELECT nome, GROUP_CONCAT(stack SEPARATOR ', ') FROM all_stacks GROUP BY nome"

"""SELECT stack, nome, GROUP_CONCAT(stack SEPARATOR ', ') FROM all_stacks GROUP BY nome"""

stacks = pd.read_sql_query(query_stacks, db.con)
print(stacks)

count = 0
for i, stack in enumerate(stacks.values):
	query_update = "UPDATE `empresa_completa3` SET stacks='{}' WHERE nome='{}'".format(stack[1], stack[0].replace("'", ""))
	if db.insert_in_db(query_update) == 0:
		count += 1
		query_add = "INSERT INTO `empresa_completa3` (nome, stacks) values ('{}', '{}')".format(stack[0].replace("'", ""), stack[1])
		db.insert_in_db(query_add)

	if i % 10 == 0:
		print(i)
print(count)