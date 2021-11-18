import pymysql
import os
import sys


class MySQL():

    def __init__(self):
        self.host = os.getenv("HOSTNAME_DB")
        self.user = os.getenv("USER_DB")
        self.passwd = os.getenv("PASSWD")
        try:
            self.con = pymysql.connect(
                    user=self.user,
                    password=self.passwd,
                    host=self.host,
                    # port=3306,
                    database="decasoft_xavier"
                    )
            self.cursor = self.con.cursor()
        except Exception as e:
            print(f"ERROR_CONNECTION: {e}")
            sys.exit(os.EX_OSERR)

    def insert_in_db(self, query: str):
        """
        INSERT NAMES IN TABLE
        """
        self.cursor.execute(query)

    def select_from(self, query: str):
        """
        USE QUERY TO SELECT FROM A TABLE
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def remove_duplicate(self, table: str):
        """
        REMOVE DUPLICATE ITENS
        """
        self.cursor.execute(f"DELETE S1 FROM {table} AS S1\
            INNER JOIN stacks AS S2 \
            WHERE S1.id < S2.id AND S1.name = S2.name")

    def __del__(self):
        try:
            self.con.commit()
        except Exception as e:
            print(f"ERROR_COMMIT: {e}")
        """ self.cursor.close() """
        self.con.close()
