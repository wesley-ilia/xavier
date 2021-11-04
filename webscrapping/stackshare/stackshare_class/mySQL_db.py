import mariadb
import os
import sys

class MySQL():
    def __init__(self, user=os.getenv("USER_DB"), passwd=os.getenv("PASSWD_DB"),
            host=os.getenv("HOSTNAME")):
        try:
            self.connection = mariadb.connect(
                    user=user,
                    password=passwd,
                    host=host,
                    # port=3306,
                    database="stackshare"
                    )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"ERROR_CONNECTION: {e}")
            sys.exit(os.EX_OSERR)


    def insert_name_lst(self, list: zip, table: str):
        """
        INSERT NAMES IN TABLE
        """""
        for name, link in list:
            print(name)
            if (name == "5 Business Reasons Why Laravel and PHP could be a Good Choice for Your Web app"):
                continue
            self.cursor.execute(f"""
INSERT INTO {table} (name, link) VALUES ('{name}', '{link}')
            """)


    def __del__(self):
        try:
            self.connection.commit()
        except Exception as e:
            print(f"ERROR_COMMIT: {e}")
        self.cursor.close()
        self.connection.close()
