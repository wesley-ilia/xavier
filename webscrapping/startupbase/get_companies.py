from dotenv import load_dotenv
from bs4 import BeautifulSoup
import json
from startupbase_class import StartupBase
from selenium.webdriver.common.by import By

BASE_URL = "https://startupbase.com.br/home/startups?" + \
"q=&states=all&cities=all&segments=all&targets=all&" + \
"phases=all&models=all&badges=all"


def write_json(driver, file):
    qtt = 0
    element = driver.find_element(by=By.XPATH,
    value="//div[@class='ais-InfiniteHits']")
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.find_all(class_="search-body__item")
    fd = open(file, 'w', encoding='utf8')
    lista = []
    for i in body:
        dicc = {}
        names = i.find_all(class_="org__title")
        el = i.find(href=True)
        link = el['href'].replace("/c/", "https://startupbase.com.br/c/")
        dicc['name'] = names[0].text.strip()
        dicc['link'] = link
        lista.append(dicc)
        print(names[0].text.strip(), "-", qtt)
        qtt = qtt + 1
    js = json.dumps(lista, ensure_ascii=False, indent=4, separators=(',', ':'))
    fd.write(js)
    fd.close()
    return ()


if (__name__ == "__main__"):
    file_name = "../verify_db/scrapping_json/startupbase.json"
    load_dotenv(dotenv_path='../../login.env')
    startup = StartupBase(headless=True)
    startup.scroll_all_page(BASE_URL)
    write_json(startup, file_name)
