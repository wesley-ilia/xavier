from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options


class WebScrapping(webdriver.Chrome):
    def __init__(self, teardown: bool = False,
                 implicit_wait: int = 0, driver_path: str = './',
                 headless: bool = False) -> None:
        self.teardown = teardown
        environ['PATH'] += driver_path
        super(WebScrapping, self).__init__(
                options=self.__headless_add(Options(), headless))
        self.implicitly_wait(implicit_wait)

    def __headless_add(self, options, headless: bool = False):
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-dev-shm-usage")
            options.experimental_options['prefs'] = {
                    "download.default_directory": r"/home/gvitor-s/Downloads"}
        return options

    def land_in_page(self, url: str = None):
        """Acess URL"""
        self.get(url)

    def click_on(self, find_by: str = By.ID, value: str = None):
        """Click on button in selenium object on find_element"""
        self.find_element(by=find_by, value=value).click()

    def get_uniq_info(self, find_by: str = By.ID, value: str = None):
        """ Get selenium objects in Site"""
        return self.find_element(by=find_by, value=value)

    def get_informations(self, find_by: str = By.ID, value: str = None):
        """ Get selenium objects in Site"""
        return self.find_elements(by=find_by, value=value)

    def get_info_by_attribute(
            self,
            selenium_element,
            attribute: str = None) -> list:
        """ Get information by attribute in selenium object"""
        return [element.get_attribute(attribute)
                for element in selenium_element]

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
