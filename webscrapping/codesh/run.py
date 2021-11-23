import os
import sys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from codesh_class import CodeshClass
from selenium.webdriver.common.by import By 
import pandas as pd
import time

# driver.add_cookie({"name": "key", "value": "value"})
""" cookie = {'name':'ajs_anonymous_id', 'value': '9ebd4adc-fc05-4120-8371-5f59f2df4cb4'} """
cookie = {'name':'euconsent-v2', 'value': 'CPQF278PQF278AKAkAPTB2CsAP_AAH_AAALIIXwHgAFgAdAGIANAAcwB8QELAKfAWaAtYBeYDJAGTANggdOB1UDrAOwgdkB2kDtwO4Ad3A70Dv4HggeRA8oD5IHzAfZA-4D74H5AfpA_cEEIIJAgnBBUEHYIPghRBCoELwQvgTgALABwAEsAcwCRQFPgLzAZIAyYBqoDrIHYAdiA7OB2oHbQO5A7oB3gDwAHjwPJA8qB6IHpAPVAe0A90B8UD5APlgfWB9sD8APxgfqB-4EAQICAQMAgfBBEEFAIMQQaBBsCDwEIYIUAhXBC4ELwAAAA.YAAAAAAAAAAA'}

if (__name__ == "__main__"):
    load_dotenv(dotenv_path='../../login.env')
    driver = CodeshClass(headless=False)
    driver.land_in_page()
    driver.add_cookie(cookie)
    """ driver.get_cookies() """
    #print(driver.get_cookie("euconsent-v2"))
    driver.implicitly_wait(5)
    """ link = driver.find_element(By.CSS_SELECTOR, 'button[class= css-ibf4ke]')
    link.click() """
    last_element = driver.find_elements(By.CLASS_NAME, 'mb-5')[-1]
    SCROLL_PAUSE_TIME = 2
    #last_element = driver.find_elements_by_class_name("search-body__item")[-1]
    i = 0
    while True:
        i += 1
        driver.execute_script("arguments[0].scrollIntoView();", last_element)
        time.sleep(SCROLL_PAUSE_TIME)
        new_element = driver.find_elements(By.CLASS_NAME, 'mb-5')[-1]
        if new_element == last_element:
            break
        last_element = new_element
    
    elements = driver.find_elements(By.CLASS_NAME, 'mb-5')
    info_list = []
    for element in elements:
        nome = element.find_element(By.CLASS_NAME, 'link-muted')
        stacks = element.find_elements(By.CSS_SELECTOR, "span[class='text-white badge badge-pill badge-primary']")
        stack = ', '.join([i.text for i in stacks])
        info_list.append([nome.text, stack])
    
    df = pd.DataFrame(info_list, columns=['nome', 'stack'])
    df.to_csv('outro_teste.csv', sep=',', header=True, index=False)


""" 
class="text-white badge badge-pill badge-primary"
"""
"""
euconsent-v2 = 
CPQF278PQF278AKAkAPTB2CsAP_AAH_AAALIIXwHgAFgAdAGIANAAcwB8QELAKfAWaAtYBeYDJAGTANggdOB1UDrAOwgdkB2kDtwO4Ad3A70Dv4HggeRA8oD5IHzAfZA-4D74H5AfpA_cEEIIJAgnBBUEHYIPghRBCoELwQvgTgALABwAEsAcwCRQFPgLzAZIAyYBqoDrIHYAdiA7OB2oHbQO5A7oB3gDwAHjwPJA8qB6IHpAPVAe0A90B8UD5APlgfWB9sD8APxgfqB-4EAQICAQMAgfBBEEFAIMQQaBBsCDwEIYIUAhXBC4ELwAAAA.YAAAAAAAAAAA
"""