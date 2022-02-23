from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Slintel(webdriver.Chrome):
    def __init__(
        self,
        headless: bool = False
            ) -> None:

        chrome_options = Options()
        capabilities = DesiredCapabilities().CHROME
        if headless is True:
            capabilities.update(pageLoadStrategy="eager")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--max-size=1920,1080')
            chrome_options.add_argument("--disable-dev-shm-usage")
        super(Slintel, self).__init__(
            desired_capabilities=capabilities,
            options=chrome_options
        )
        self.implicitly_wait(4)

    def __enter__(self):
        return self

    def __exit__(self, tp, vl, tb):
        self.close()

    def land_in_page(self, page: str = None):
        self.get(page)
