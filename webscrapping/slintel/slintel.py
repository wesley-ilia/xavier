import pandas as pd
import signal
import os
from time import sleep
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import pymysql

load_dotenv(dotenv_path='../../login.env')

class SlintelScrap():
    def __init__(self, empresas_novas, rescrap : bool = False):
        self.rescrap = rescrap
        self.empresas_novas = empresas_novas

        self.list_empresas = []
        self.erradas = []

        self.links = []

        """ df = pd.read_csv("empresas_slintel.csv", sep=',')
        self.empresas_velhas = list(df['nome'].values)
        df = pd.read_csv("problemas_slintel.csv", sep=',')
        empresas_erradas = list(df['nome'].values)
        self.empresas_velhas.extend(empresas_erradas) """

        signal.signal(signal.SIGINT, lambda signal, frame: self._signal_handler())

        self.terminated = False

    def search_letter(self, letter : str):
        self.links = []
        self.list_empresas = []
        self.non_brazilian = pd.read_csv('non_brazilian.csv', sep=',').to_dict(orient='list')

        host = os.getenv("HOSTNAME_AWS")
        user = os.getenv("USER_AWS")
        password = os.getenv("PASSWD_AWS")
        database = os.getenv("database")
        con = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                        )

        self.empresas_velhas = pd.read_sql_query("SELECT nome, website FROM empresa2 WHERE 1", con=con).to_dict(orient='list')
        df = pd.read_csv('empresas_slintel.csv', sep=',', index_col=False)
        self.empresas_velhas['nome'].extend(list(df['nome'].values))
        self.empresas_velhas['website'].extend(list(df['website'].values))
        con.close()
        letter = letter.upper()
        result = requests.get(f'https://www.slintel.com/directory/company/{letter}/{letter}' + '1')
        soup = BeautifulSoup(result.content, features='lxml')
        size = len(soup.select_one(".alp_combination").select_one(".row").select(".col-3"))
        self.get_address_by_letter(letter, 1, size + 1)
        self.search_links()

    def get_address_by_letter(self, letter : str, start : int, stop : int):        
        for i in range(start, stop):
            if self.terminated:
                break
            result = requests.get(f'https://www.slintel.com/directory/company/{letter}/{letter}' + str(i))
            soup = BeautifulSoup(result.content, features="lxml")
            links = soup.select('div[class=company_name_text] > a')
            self.links.extend([link['href'] for link in links if link['href'] not in self.non_brazilian['link']])
            if i % 1 == 0:
                print(i)
                break
    
    def search_links(self):
        for i, link in enumerate(self.links):
            if self.terminated:
                break
            result = requests.get('https://www.slintel.com/' + link)
            soup = BeautifulSoup(result.content, features="lxml")
            
            info = soup.select('.sl-subHeader')
            country = info[0].getText().strip()
            nome = soup.select_one('.sl-title').getText().strip()
            if len(info) > 2:
                website = info[2].getText().strip()
            else:
                website = 'not_website'
            
            if ('Brazil' in country and nome not in self.empresas_velhas['nome'] and 
            website not in self.empresas_velhas['website']) or ('Brazil' in country 
            and self.rescrap):
                size = info[3].getText().strip()

                area = soup.select('.list-inline-item')
                area = ", ".join([a.getText().strip() for a in area])

                descricao = soup.select_one('.sl-subTitle').getText().strip()

                stacks = soup.select_one("#Programming_Languages_And_Frameworks").select('.techstack-media-title')
                stacks = ", ".join([stack.getText().strip() for stack in stacks])
                self.list_empresas.append([nome, country.replace('\n', ' '), size.replace('\n', ' '), website.replace('\n', ' '), area.replace('\n', ' '), stacks.replace('\n', ' '), descricao.replace('\n', ' '), 'https://www.slintel.com/' + link])
            
            elif 'Brazil' not in country and nome not in self.non_brazilian['nome']:
                self.non_brazilian['nome'].append(nome)
                self.non_brazilian['link'].append(link)
                
            print(i)
            if i % 10 == 9:
                print(i)
                break
        
        self.finish()

    def finish(self):
        print(len(self.list_empresas))
        df = pd.DataFrame(self.list_empresas)
        df.to_csv('empresas_slintel.csv', sep=',', mode='a', header=False, index=False)

        df = pd.DataFrame(self.erradas)
        df.to_csv('problemas_slintel.csv', sep=',', mode='a', header=False, index=False)

        df = pd.DataFrame(self.non_brazilian)
        df.to_csv('non_brazilian.csv', sep=',', mode='w', header=True, index=False)

    def run(self):
        df = pd.read_csv("stupbase_certas.csv", sep=',')
        self.empresas_velhas = list(df['nome'].values)
        df = pd.read_csv("stupbase_erradas.csv", sep=',')
        empresas_erradas = list(df['nome'].values)
        self.empresas_velhas.extend(empresas_erradas)

        count = 0
        count2 = 0
        self.founds = []
        self.not_founds = []
        for empresa in self.empresas_novas:
            if self.terminated == True:
                break
            if empresa[0] not in self.empresas_velhas:
                search = empresa[0]

                result = requests.get(f"https://www.slintel.com/directory/company?searchTerm={search}")
                soup = BeautifulSoup(result.content, features="lxml")
                links = soup.select('div[class=company_name_text] > a')
                links = ['https://www.slintel.com/' + link['href'] for link in links]
                if not links:
                    self.not_founds.append([empresa[0], 'não achou na pesquisa'])
                    continue
                if pd.isnull(empresa[1]):
                    links = [links[0]]
                for link in links:
                    result = requests.get(link)
                    soup = BeautifulSoup(result.content, features="lxml")

                    if soup.select('.sl-subHeader') is None or len(soup.select('.sl-subHeader')) <= 2:
                        continue
                    slintel_site = soup.select('.sl-subHeader')[2].getText()
                    if slintel_site in empresa[1] or pd.isnull(empresa[1]):
						#soup.select_one("#Programming_Languages_And_Frameworks")
                        if pd.isnull(empresa[1]):
                            descricao = 'sem site da stupbase'
                        else:
                            descricao = 'com site da stupbase'
                        if soup.select_one("#Programming_Languages_And_Frameworks") is None:
                            self.not_founds.append([empresa[0], "achou na pesquisa " + descricao])
                            break
                        stacks = soup.select_one("#Programming_Languages_And_Frameworks").select('.techstack-media-title')
                        stacks = ", ".join([stack.getText().strip() for stack in stacks])
                        self.founds.append([empresa[0], link, slintel_site, stacks, descricao])
                        break
                        """ self.not_founds.append([empresa[0], "achou na pesquisa " + descricao])
                        break """
                    elif link == links[-1]:
                        self.not_founds.append([empresa[0], "achou na pesquisa"])
                count += 1
                if count % 10 == 0:
                    print(count)
                    self.save_csv()
            else:
                count2 += 1
        self.finish_program()

    def save_csv(self):
        df = pd.DataFrame(self.founds)
        df.to_csv('stupbase_certas.csv', mode='a', header=False, index=False)
        self.founds = []

        df = pd.DataFrame(self.not_founds)
        df.to_csv('stupbase_erradas.csv', mode='a', header=False, index=False)
        self.not_founds = []

    def finish_program(self):
        print("founds")
        print(self.founds)
        print('not_founds')
        print(self.not_founds)
        df = pd.DataFrame(self.founds)
        df.to_csv('certas_slintel.csv', mode='a', header=False, index=False)

        df = pd.DataFrame(self.not_founds)
        df.to_csv('erradas_slintel.csv', mode='a', header=False, index=False)

    def _signal_handler(self):
        self.terminated = True
