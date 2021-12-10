import pymysql
import pandas
import os
import sys

class Log():
    def __init__(self):
        self.host = os.getenv("HOSTNAME_DB")
        self.user = os.getenv("USER_DB")
        self.password = os.getenv("PASSWD")
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
        self.cursor = self.con.cursor()

    def insert_in_db(self, query: str):
        return self.cursor.execute(query)

    def select_from(self, query: str, all: bool = True):
        self.cursor.execute(query)
        if all:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()
    
    def __del__(self):
        self.cursor.close()
        self.con.close()