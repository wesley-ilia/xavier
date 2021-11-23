import os
import sys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from selenium_class import ThorClass
from selenium.webdriver.common.by import By 
import pandas as pd

if (__name__ == "__main__"):
    
    load_dotenv(dotenv_path='../../login.env')
    thor = ThorClass(headless=True)

    for x in range (599, 600):
        thor.land_in_page("jobs", "page", str(x))
        elements = thor.find_elements(By.CLASS_NAME, "cell-list")
        infos_list = []
        print("x",x)
        i = 0
        for element in elements:
            try :
                info = element.find_elements(By.CSS_SELECTOR, "div[class=cell-list-content-icon] > span")
                stack = element.find_elements(By.CLASS_NAME, 'tag-list')
                stack = ', '.join([i.text for i in stack])
                infos_list.append([info[0].text, info[2].text, stack])
            except IndexError:
                pass
        
        df = pd.DataFrame(infos_list, columns=['nome', 'tamanho', 'stack'])
        df.to_csv('teste.csv', sep=',', mode='a', header=False, index=False)
    