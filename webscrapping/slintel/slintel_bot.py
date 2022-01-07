from selenium import webdriver
from selenium.webdriver.common.by import By
from os import environ
from time import sleep

class Slintel(webdriver.Chrome):
    def __init__(
        self,
        teardown: bool = False,
        implicit_wait: int = 0,
        driver_path: str = './',
        headless: bool = False
            ) -> None:

        self.teardown = teardown
        environ['PATH'] += driver_path
        super(Slintel, self).__init__()
        self.implicitly_wait(implicit_wait)

    def land_in_page(self, page: str = None):
        self.get(page)
