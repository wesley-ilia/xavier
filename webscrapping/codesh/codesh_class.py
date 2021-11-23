from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class CodeshClass(webdriver.Chrome):
    def __init__(self, headless=False):
        self.driver_path = os.getenv("DRIVER_PATH")
        os.environ['PATH'] += self.driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        super(CodeshClass, self).__init__(options=options)
        self.implicitly_wait(10)

    def land_in_page(self):
        self.get('https://coodesh.com/vagas')