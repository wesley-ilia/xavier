from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
import pandas as pd

os.environ['PATH'] += r"C:/home/felipe/Desktop/scrapping/drivers"
drive = webdriver.Chrome()

def test_change_preview_based_on_acre():
    drive.get('http://localhost:3000')
    drive.find_element(By.CLASS_NAME, 'css-319lph-ValueContainer').click()
    options = drive.find_element(By.ID, 'react-select-3-listbox')
    options.find_element(By.ID, 'react-select-3-option-0').click()
    preview = drive.find_element(By.ID, 'preview')
    assert preview.text != 'Preview: 0'

def test_box_for_specifics_cities():
    drive.get('http://localhost:3000')

    drive.find_element(By.CLASS_NAME, 'css-319lph-ValueContainer').click()
    options = drive.find_element(By.ID, 'react-select-3-listbox')

    options.find_element(By.ID, 'react-select-3-option-1').click()

    drive.find_element(By.CSS_SELECTOR, 'div.col:nth-child(3) > input:nth-child(1)').click()
    drive.find_element(By.CSS_SELECTOR, "div.css-b62m3t-container:nth-child(1) > div:nth-child(3) > div:nth-child(1)").click()
    options = drive.find_element(By.CLASS_NAME, 'css-26l3qy-menu')
    options.find_element(By.ID, 'react-select-11-option-1').click()
    preview = drive.find_element(By.ID, 'preview')
    assert preview.text == 'Preview: 1'

  
def test_the_download_button():
    drive.get('http://localhost:3000')
    drive.find_element(By.CLASS_NAME, 'css-319lph-ValueContainer').click()
    options = drive.find_element(By.ID, 'react-select-3-listbox')

    options.find_element(By.ID, 'react-select-3-option-1').click()
    drive.find_element(By.CLASS_NAME, 'form-control').send_keys('test_download_button')
    drive.find_element(By.TAG_NAME, 'button').click()
    home = os.path.expanduser('~')
    sleep(2)
    assert os.path.exists(f'{home}/Downloads/test_download_button.csv') == True
 

def test_preview_with_mercados_filled():
    drive.get('http://localhost:3000')
    drive.find_element(By.CLASS_NAME, 'mercados__input-container').click()
    elements_mercados = drive.find_elements(By.CLASS_NAME,  'mercados__option')
    list_mercados = [mercado.text for mercado in elements_mercados]
    location = list_mercados.index('Finanças')
    elements_mercados[location].click()

    preview = drive.find_element(By.ID, 'preview')
    assert preview.text == 'Preview: 571'

def test_stacks_preview():
    drive.get('http://localhost:3000')
    drive.find_element(By.CLASS_NAME, 'stacks__input-container').click()
    elements_stacks = drive.find_elements(By.CLASS_NAME, 'stacks__option')
    list_stacks = [stacks.text for stacks in elements_stacks]
    elements_stacks[list_stacks.index('.NET')].click()
    preview = drive.find_element(By.ID, 'preview')
    sleep(1)
    assert preview.text == 'Preview: 2259'

def test_stacks_preview():
    drive.get('http://localhost:3000')
    drive.find_element(By.CLASS_NAME, 'estados__input-container').click()
    elements_stacks = drive.find_elements(By.CLASS_NAME, 'estados__option')
    list_stacks = [stacks.text for stacks in elements_stacks]
    elements_stacks[list_stacks.index('BA')].click()

    drive.find_element(By.CLASS_NAME, 'form-control').send_keys('test_BA')
    drive.find_element(By.TAG_NAME, 'button').click()
    home = os.path.expanduser('~')
    sleep(2)
    df = pd.read_csv(f'{home}/Downloads/test_BA.csv')
    total = len(df.index)
    df.query('cidade == "Salvador "', inplace=True)
    capital = len(df.index)
    assert total - capital == 54