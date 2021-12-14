import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


if (__name__ == "__main__"):

    #fd = open("../verify_db/scrapping_json/thor.json", 'w', encoding='utf8')
    fd = open("thor.json", 'w', encoding='utf8')
    teste = open("teste.txt", 'w', encoding='utf8')

    infos_list = []
    i = 1
    while True:
        print(i)
        response = requests.get("https://programathor.com.br/jobs/page/" + str(i))
        soup = BeautifulSoup(response.content, features="html.parser")
        elements = soup.select(".cell-list")

        for element in elements:
            dicc = {}
            info = element.select("div[class=cell-list-content-icon] > span")
            if not info:
                continue
            stack = element.select('.tag-list')
            stack = ', '.join([i.text for i in stack])
            link = element.select_one("a")

            infos_list.append({"nome": info[0].text, "tamanho": info[2].text, 
            "stack": stack, "link": link['href']})

        if u'Next ›' not in [link.text for link in soup.select(".page-link")]:
            break

        i += 1
    
    js = json.dumps(infos_list, ensure_ascii=False, indent=4, separators=(',', ':'))
    fd.write(js)
    fd.close()

    #df = pd.DataFrame(infos_list, columns=['nome', 'tamanho', 'stack', 'link'])
    #df.to_csv('../verify_db/scrapping_json/thor.csv', sep=',', mode='a', header=False, index=False)
    