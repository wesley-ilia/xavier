from dotenv import load_dotenv
from time import sleep
from stackshare_class.stackshare import StackShare
from stackshare_class.mySQL_db import MySQL

load_dotenv(dotenv_path='login.env')
with StackShare() as bot:
    db = MySQL()
    tuple_links = db.select_from("SELECT * FROM name_stacks WHERE 1")
    result_lst = []
    for link in tuple_links:
        result = (bot.get_stacks_by_company(company=link[1], address=link[2], id_ref=link[0]))
        values = ", ".join([f"\"{value}\"" for value in result.values()]).lower()
        keys = ", ".join([f"`{key}`" for key in result.keys()])
        db.insert_in_db(f"INSERT INTO stacks ({keys}) VALUES ({values})")


"""
SELECT * FROM `stacks` WHERE `DevOps` LIKE '%slack%' or `Application and Data` LIKE '%slack%' or `Utilities` LIKE '%slack%' or `Business Tools` LIKE '%slack%'
""" 