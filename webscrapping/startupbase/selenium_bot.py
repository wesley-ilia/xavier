from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


class startupbase(webdriver.Chrome):
    def __init__(self) -> None:
        os.environ['PATH'] += ':/home/luigi/selenium_drivers'
        super(startupbase, self).__init__()
        self.implicitly_wait(5)

    def __exit__(
                self, exception_type,
                exception_value, exception_traceback) -> None:
        self.close()
        self.quit()

    # Lands the startupbase page of the website buildwith.com
    def land_page(self) -> None:
        self.get('https://startupbase.com.br/home/startups')

    def scroll_down(self) -> None:
        SCROLL_PAUSE_TIME = 0.1
        last_element = self.find_elements(By.CLASS_NAME, "org__body")[-1]
        i = 0
        while i < 10:
            self.execute_script("arguments[0].scrollIntoView();", last_element)
            sleep(SCROLL_PAUSE_TIME)
            new_element = self.find_elements(By.CLASS_NAME, "org__body")[-1]
            if new_element == last_element:
                i += 1
                print("time:", i)
                print(new_element)
                print(last_element)
            else:
                last_element = new_element
        return None

    def get_page_links(self) -> list:
        body_itens = self.find_elements(By.CLASS_NAME, 'search-body__item')
        links = list()
        for item in body_itens:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(link)
        return links

    def get_body_requests(self, links: list) -> list:
        bodys = list()
        for link in links:
            self.get(link)
            sleep(1)
            body = self.find_element(By.TAG_NAME, 'body')
            bodys.append(body.get_attribute('innerHTML'))
        return bodys
