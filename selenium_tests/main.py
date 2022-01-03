from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.environ['PATH'] += r"C:/home/felipe/Desktop/scrapping/drivers"
drive = webdriver.Chrome()

# def test_change_preview_based_on_acre():
#     drive.get('http://localhost:3000')
#     drive.find_element(By.CLASS_NAME, 'css-319lph-ValueContainer').click()
#     options = drive.find_element(By.ID, 'react-select-3-listbox')
#     options.find_element(By.ID, 'react-select-3-option-0').click()
#     preview = drive.find_element(By.ID, 'preview')
#     assert preview.text != 'Preview: 0'

def test_box_for_specifics_cities():
    drive.get('http://localhost:3000')

    drive.find_element(By.CLASS_NAME, 'css-319lph-ValueContainer').click()
    options = drive.find_element(By.ID, 'react-select-3-listbox')
    options.find_element(By.ID, 'react-select-3-option-0').click()

    drive.find_element(By.CSS_SELECTOR, 'div.col:nth-child(3) > input:nth-child(1)').click()
    drive.find_element(By.CSS_SELECTOR, "div.css-b62m3t-container:nth-child(1) > div:nth-child(3) > div:nth-child(1)").click()
    # options = drive.find_element(By.CLASS_NAME, 'css-26l3qy-menu')
    # options.find_element(By.CLASS_NAME, 'react-select-11-option-0').click()
    testing = drive.find_element(By.NAME, 'teste')
    print(testing.get_attribute('innerHTML'))

test_box_for_specifics_cities()
