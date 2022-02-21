from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class StartupBase(webdriver.Chrome):
    def __init__(self, headless: bool = False) -> None:
        chrome_options = ChromiumOptions()
        capabilities = DesiredCapabilities().CHROME
        if headless is True:
            capabilities.update(pageLoadStrategy="eager")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--window-size=1920,1080')
        super(StartupBase, self).__init__(
            desired_capabilities=capabilities,
            options=chrome_options
        )
        self.implicitly_wait(5)

    def __exit__(self, tp, vl, tb):
        self.close()

    # Lands the startupbase page of the website buildwith.com
    def land_page(self) -> None:
        self.get('https://startupbase.com.br/home/startups')

    def scroll_down(self):
        while True:
            last_element = self.find_elements(By.CLASS_NAME, "org__body")[-1]
            self.execute_script("arguments[0].scrollIntoView();", last_element)
            try:
                WebDriverWait(self, 5).until(
                        method=lambda x: x.find_elements(
                            by=By.CLASS_NAME,
                            value="org__body"
                            )[-1] != last_element
                        )
            except BaseException:
                break

    def get_page_links(self):
        html_links = self.find_elements(
                By.CSS_SELECTOR, 'div[class="search-body__item"] > a')
        return [item.get_attribute('href') for item in html_links]
