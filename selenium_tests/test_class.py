from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestSelenium(webdriver.Chrome):
    def __init__(self, teardown: bool = False,
                 implicit_wait: int = 0, driver_path: str = './',
                 headless: bool = False) -> None:
        self.teardown = teardown
        environ['PATH'] += driver_path
        super(TestSelenium, self).__init__(
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

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
