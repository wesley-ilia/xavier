from dotenv import load_dotenv
# from time import sleep
from stackshare_class.stackshare import StackShare
from stackshare_class.mySQL_db import MySQL


def get_stack_from_companies():
    with StackShare() as bot:
        db = MySQL()
        tuple_links = db.select_from("SELECT * FROM name_companies WHERE 1")
        for link in tuple_links:
            bot.get(link[2])
            bot.click_on('div[class=css-yb2pww] > a')
            result = bot.get_stacks_by_company(company=link[1], id_ref=link[0])
            values = ", ".join([f"\"{value}\"" for value in result.values()]).lower()
            keys = ", ".join([f"`{key}`" for key in result.keys()])
            db.insert_in_db(f"INSERT INTO stacks ({keys}) VALUES ({values})")
            bot.delete_all_cookies()


def get_stack_from_stacks():
    with StackShare() as bot:
        db = MySQL()
        tuple_links = db.select_from("SELECT * FROM name_stacks WHERE 1")
        for link in tuple_links:
            bot.get(link[2])
            result = bot.get_stacks_by_company(company=link[1], id_ref=link[0])
            values = ", ".join([f"\"{value}\"" for value in result.values()]).lower()
            keys = ", ".join([f"`{key}`" for key in result.keys()])
            db.insert_in_db(f"INSERT INTO stacks ({keys}) VALUES ({values})")
            bot.delete_all_cookies()


load_dotenv(dotenv_path='login.env')
db = MySQL()
db.remove_duplicate('stacks')

"""
SELECT * FROM `stacks` WHERE `DevOps` LIKE '%slack%'
or `Application and Data` LIKE '%slack%'
or `Utilities` LIKE '%slack%' or `Business Tools` LIKE '%slack%'
"""
