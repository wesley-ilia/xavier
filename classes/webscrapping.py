from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebScrapping(webdriver.Chrome):
    def __init__(self, BASE_URL: str = None, teardown: bool = False,
                 implicit_wait: int = 0, driver_path: str = './',
                 headless: bool = False) -> None:
        self.BASE_URL = BASE_URL
        self.teardown = teardown
        environ['PATH'] += driver_path
        super(WebScrapping, self).__init__()
        self.implicitly_wait(implicit_wait)

    def land_in_page(self, page: str = None):
        self.get(page)

    def click_on(self, find_by: str = By.ID, value: str = None):
        """Click on button in selenium object on find_element"""
        self.find_element(by=find_by, value=value).click()

    def get_informations(self, find_by: str = By.ID, value: str = None):
        """ Get selenium object in Site"""
        return self.find_elements(by=find_by, value=value)

    def get_info_by_attribute(
            self,
            selenium_element,
            attribute: str = None) -> list:
        """ Get information by attribute in selenium object"""
        return [element.get_attribute(attribute)
                for element in selenium_element]
