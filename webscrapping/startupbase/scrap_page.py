import time, os, sys, json
from datetime import datetime 
from bs4 import BeautifulSoup
from selenium import webdriver
from Log import Log
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from startupbase_class import StartupBase
import time

def get_info(info, posic):
    if (info and info[posic]):
        return info[posic].text
    else:
        return ""

def connect(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.page_load_strategy = 'normal'
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome(executable_path=r"/home/cpereira/42/labs/startupbase/chromedriver", options=options)
    driver.implicitly_wait(1) # seconds
    driver.get(url)
    time.sleep(2)
    return (driver)

def insert_db(titulos , infos):
    con = connect_db()
    mycursor = con.cursor()

    infos = infos.replace("/","")

    sql = "INSERT INTO empresa_completa3 ("+titulos+") VALUES ("+infos+")"
    mycursor.execute(sql)
    con.commit()
    con.close
    return 

def get_titulos():
    titulos = "mercado, publico_alvo, modelo_receita, momento, id_ref"
    titulos += ",sobre, endereco, complemento, bairro, cidade, estado"
    titulos += ",url_curta, segmento, fundacao, tamanho, atualizacao"
    titulos += ",facebook, relacionadas, fundadores, aceleradoras, nome, subtitulo, website"
    return titulos

def action (driver : object, id: int):
    dados = {
        'descricao' : "",
        'mercado' : "",
        'receita' : "",
        'momento' : "",
        'endereco' : "",
        'complemento' : "",
        'bairro' : "",
        'cidade' : "",
        'estado' : "",
        'url_curta' : "",
        'seg_secundario' : "",
        'fundacao' : "",
        'tamanho' : "",
        'atualizacao' : "",
        'sociais' : "",
        'nome_fund' : "",
        'nome_badges' : "",
        'relacoes' : "",
        'site' : "",
        "origem": "startupbase"
    }
    titulos = get_titulos()
    time.sleep(1)
    html_content = driver.find_element(by=By.XPATH, value="/html/body").get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, "html.parser")
    nome = soup.find(class_="publ-header__name").text
    descricao = soup.find(class_="publ-header__description").text
    if (descricao):
        descricao = descricao.replace("\"", "")
        descricao = descricao.replace("'", "")
    descricao_box = soup.find_all(class_="startup-timely__data")
    dados['mercado'] = descricao_box[0].text
    dados['publico'] = descricao_box[1].text
    dados['receita'] = descricao_box[2].text
    dados['momento'] = descricao_box[3].text
    infos = '"'+dados['mercado'] +'","' + dados['publico'] +'","' +dados['receita']+'","' +dados['momento']+'","' +id+'"'
    t_sobre = soup.find_all(class_="publ-title")
    cards = soup.find_all('app-card')
    for card in cards:
        t_sobre = card.find_all(class_="publ-title")
        if (t_sobre and t_sobre[0].text == 'Sobre'):
            sobre = card.find(class_="publ-text").text
            if (sobre):
                sobre = sobre.replace("\"","")
                sobre = sobre.replace("'","")
        if (t_sobre and t_sobre[0].text == 'Localização'):
            info = card.find_all(class_="publ-text")
            dados['endereco'] = get_info(info, 0)
            dados['complemento'] = get_info(info, 1)
            dados['bairro'] = get_info(info, 2)
            cidade_estado = get_info(info, 3).split('-')
            cidade = cidade_estado[0]
            if (cidade_estado[1]):
                dados['estado'] = cidade_estado[1]
            else:
                dados['estado'] = ""
    localizacao = soup.find_all(class_="publ-header__location")
    cidade_estado = get_info(localizacao, 0).split('-')
    if (cidade_estado):
        cidade = cidade_estado[0]
        if (len(cidade_estado) == 2):
            estado = cidade_estado[1]
        else:
            estado = ""
    else:
        cidade = ""
    nome = nome.replace("\"","")
    dados['endereco'] = dados['endereco'].replace("\"","")
    dados['complemento'] = dados['complemento'].replace("\"","")
    dados['bairro'] = dados['bairro'].replace("\"","")
    dados['cidade'] = dados['cidade'].replace("\"","")
    dados['estado'] = dados['estado'].replace("\"","")
    infos += ',"'+sobre+'","' + dados['endereco'] +'","' +dados['complemento']+'","' +dados['bairro']+ '","' +dados['cidade']+'","' +dados['estado']+'"'
    cards = soup.find_all(class_="publ-aside__info")
    url_curta = cards[0].find(class_="publ-text").text
    seg_secundario = cards[1].find(class_="publ-text").text
    fundacao = cards[2].find(class_="publ-text").text
    tamanho = cards[3].find(class_="publ-text").text
    atualizacao = cards[4].find(class_="publ-text").text
    infos += ',"'+url_curta +'","' + seg_secundario +'","' +fundacao+'","' +tamanho+ '","' +atualizacao+'"'
    relacao = soup.find(class_="publ-aside__tags")
    if (relacao):
        links = relacao.find_all('a')
        relacoes = ""
        for link in links:
            relacoes += link.text + " "
    socials = soup.find(class_="publ-social")
    if (socials):
        links = socials.find_all('a')
        sociais = ""
        for link in links:
            sociais += link['href'] + " "
    websites = soup.find(class_="publ-channel")
    if (websites):
        dados['site'] = websites['href']
    fundadores = soup.find_all(class_="member__name")
    if (fundadores):
        link_fundadores = soup.find_all(class_="member__link")
        dados['nome_fund'] = ""
        for fundador in fundadores:
            dados['nome_fund'] += fundador.text + " " 
    badges = soup.find_all(class_="badge__name")
    dados['nome_badges'] = ""
    for badge in badges:
        dados['nome_badges'] += badge.text + " "
    infos += ',"'+dados['sociais'] +'","' + dados['relacoes'] +'","' +dados['nome_fund']+'","' +dados['nome_badges']+'","' +nome+'","' +dados['descricao']+'","' +dados['site']+'"'
    print(dados)
    #insert_db(titulos , infos)
    #driver.quit()
    if (nome):
        nome = nome.replace("/", "")
    print(id + " " + nome + " - DONE")
    return (0)


def update_status(status, id, con):
    mycursor = con.cursor()
    mycursor.execute("UPDATE control_startbase SET status = '"+status+"' WHERE id = '"+id+"'")
    con.commit()


def scrap_pag(connection):
    connection.insert_in_db(query="SELECT * FROM control_startupbase WHERE status like '%NOVO%' ")
    return connection.cursor.fetchall()

def put_on_data_base(myresult: tuple, connection: object, startupbase: object):
    for x in myresult:
        startupbase.land_in_page(page=x[2])
        try:
            action(startupbase, str(x[0]))
            update_status('Done', str(x[0]), connection)
        except:
            update_status('ERROR', str(x[0]), connection)
            print("xx ERROR", str(x[2]))

if (__name__ == "__main__"):
    load_dotenv(dotenv_path='../../login.env')
    log = Log()
    startupbase = StartupBase(headless=True)
    put_on_data_base(
        myresult=scrap_pag(log),
        connection=log,
        startupbase=startupbase
)

