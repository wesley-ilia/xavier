import os
import sys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from startupbase_class import StartupBase

if (__name__ == "__main__"):
    load_dotenv(dotenv_path='../../login.env')
    startup = StartupBase()
    startup.land_in_page(BASE_URL)
