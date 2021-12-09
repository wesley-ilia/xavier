import pymysql
import pandas
import os
import sys


class Log():
    def __init__(self):
        self.host = os.getenv("HOSTNAME_AWS")
        self.user = os.getenv("USER_AWS")
        self.password = os.getenv("PASSWD_AWS")
        try:
            self.con = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database="ecole42_xavier"
                )
        except BaseException:
            print("Informações de login erradas")
            sys.exit(os.EX_IOERR)
        self.cursor = self.con.cursor()

    def insert_in_db(self, query: str):
        return self.cursor.execute(query)
    
    def __del__(self):
        self.cursor.close()
        self.con.close()
