import pymysql
import os
import sys

class MySQL():
    def __init__(self, user=os.getenv("USER_DB"), passwd=os.getenv("PASSWD_DB"),
            host=os.getenv("HOSTNAME")):
        try:
            self.con = pymysql.connect(
                    user=user,
                    password=passwd,
                    host=host,
                    # port=3306,
                    database="stackshare"
                    )
            self.cursor = self.con.cursor()
        except Exception as e:
            print(f"ERROR_CONNECTION: {e}")
            sys.exit(os.EX_OSERR)


    def insert_name_lst(self, list: zip, table: str):
        """
        INSERT NAMES IN TABLE
        """""
        for name, link in list:
            self.cursor.execute(f"""
INSERT INTO {table} (name, link) VALUES ('{name}', '{link}')
            """)


    def __del__(self):
        try:
            self.con.commit()
        except Exception as e:
            print(f"ERROR_COMMIT: {e}")
        self.cursor.close()
        self.con.close()
