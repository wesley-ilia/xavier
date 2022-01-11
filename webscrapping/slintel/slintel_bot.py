from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ

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
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        super(Slintel, self).__init__(
            options=chrome_options
        )
        self.implicitly_wait(implicit_wait)

    def land_in_page(self, page: str = None):
        self.get(page)
