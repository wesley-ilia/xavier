from time import sleep
from stackshare_class.stackshare import StackShare
from stackshare_class.mySQL_db import MySQL

with StackShare() as bot:
    bot.land_in_page("search", "q=Brazil#")
    sleep(2)
    bot.click_on("div[class=row] > div:nth-child(1) > div:nth-child(1) > a:nth-child(5)")
    lst_links = bot.get_info('div[class="results group-companies"] > a', 'href')
    lst_names = bot.get_info('div[class="results group-companies"] > a > div:nth-child(2) > span:nth-child(1)', 'innerHTML')
    values = zip(lst_names, lst_links)
db = MySQL()
db.insert_name_lst(values, 'name_companies')
