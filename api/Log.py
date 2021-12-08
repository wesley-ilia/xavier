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
        
        results = pandas.read_sql_query(query, con)
        results.to_csv(file, index=False)
        """  except BaseException:
            print("Informações da query erradas")
            sys.exit(os.EX_IOERR) """

    def insert_into_log(self, query: str, version: str,
                        result_csv: str, obs: str):
        self.cursor.execute(f"INSERT INTO logs (query, version, result, obs)\
                VALUES ('{query}', '{version}', '{result_csv}', '{obs}')")
        self.con.commit()

    def set_feedback(self, feedback: bool, comment: str, obs: str):
        self.cursor.execute(f"UPDATE logs SET feedback='{feedback}',\
                comments='{comment}' WHERE obs like '%{obs}%'")
        self.con.commit()

    def remove_duplicate(self, table: str):
        """
        REMOVE DUPLICATE ITENS
        """
        self.cursor.execute(f"DELETE S1 FROM {table} AS S1\
                INNER JOIN stacks AS S2 \
                WHERE S1.id < S2.id AND S1.name = S2.name")

    def __del__(self):
        self.con.close()
