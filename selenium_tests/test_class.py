from os import getenv, environ
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium(webdriver.Chrome):
    def __init__(self, teardown=False, headless=False):
        self.driver_path = getenv("DRIVER_PATH")
        self.teardown = teardown
        environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        if headless:
           options.add_argument('headless') 
        super(TestSelenium, self).__init__(options=options)
        self.implicitly_wait(10)

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
