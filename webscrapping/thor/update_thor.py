from Log import Log
from dotenv import load_dotenv
import json

def status_thor(name):
    f = open(name,'r')
    log = Log()
    data = json.load(f)
    for count, i in enumerate(data):
        nome = i['nome'].replace("'","")
        ret = log.select_from("Select * from final where nome like '%"+nome+"%'", all=False)
        if ret:
            if ret[3] is not None:
                stacks = ", ".join(set(ret[3].split(", ") + i['stack'].split(", ")))
            else:
                stacks = i['stack']
            log.insert_in_db(f"update final set stacks='{stacks}' where nome like '%"+nome+"%'")
        else:
            log.insert_in_db(f"Insert into final (nome, tamanho, stacks, fonte, link )\
VALUES ('{nome}', '{i['tamanho']}', '{i['stack']}', 'thor', '{i['link']}')")
        log.con.commit()
        print(count,nome)
    f.close()

if (__name__ == "__main__"):
    load_dotenv(dotenv_path='../../login.env')
    """ thor = ThorClass(headless=True) """
    status_thor("../verify_db/scrapping_json/thor.json")
