from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Codesh(webdriver.Chrome):
    def __init__(
        self,
        teardown: bool = False,
        implicit_wait: int = 0,
        driver_path: str = './',
        headless: bool = False
            ) -> None:

        self.teardown = teardown
        environ['PATH'] += driver_path
        super(Codesh, self).__init__()
        self.implicitly_wait(implicit_wait)

    def land_in_page(self, page: str = None):
        self.get(page)

    def scroll_site(self, sleep_time: int) -> None:
        """Scroll a page until get the end"""
        last_height = self.execute_script(
                "return document.body.scrollHeight")
        while True:
            self.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
            sleep(sleep_time)
            new_height = self.execute_script(
                    "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_first_page_infos(self) -> list:
        container = self.find_element(
            By.CSS_SELECTOR, 'div[class="space-2 container"]')
        boxes = container.find_elements(
            By.CSS_SELECTOR, 'a[class="mb-5 card"]')
        companies = dict()
        for box in boxes:
            tag = box.find_element(By.TAG_NAME, 'a')
            name = tag.text
            stacks = box.find_element(
                By.CSS_SELECTOR,
                'div[class="mb-3 mb-md-0"] > span[class="align-middle"]')
            stacks = stacks.find_elements(By.TAG_NAME, 'span')
            if name not in companies.keys():
                name_href = tag.get_attribute('href')
                companies[name] = dict()
                companies[name]['perfil'] = name_href
                companies[name]['vagas'] = box.get_attribute('href')
                companies[name]['stacks'] = [stack.text for stack in stacks]
            else:
                companies[name]['stacks'] = \
                    list(
                        set(companies[name]['stacks'] +
                            [stack.text for stack in stacks])
                    )
        return companies
