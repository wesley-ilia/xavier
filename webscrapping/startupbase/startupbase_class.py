from os import getenv
from webscrapping_cl import WebScrapping
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class StartupBase(WebScrapping):
    def __init__(self, teardown: bool = False, headless: bool = False):
        super(StartupBase, self).__init__(
            driver_path=getenv('DRIVER_PATH'),
            teardown=teardown,
            headless=headless)

    def scroll_all_page(self, url):
        SCROLL_PAUSE_TIME = 0.01
        self.land_in_page(url)
        last_element = self.get_informations(find_by=By.CLASS_NAME, value="org__body")[-1]
        i = 0
        z = 0
        while True:
            try :
                print("i= ",i,"z=",z)
                i += 1
                self.execute_script("arguments[0].scrollIntoView();", last_element)
                time.sleep(SCROLL_PAUSE_TIME)
                new_element = self.get_informations(find_by=By.CLASS_NAME, value="org__body")[-1]
                if new_element == last_element:
                    z += 1
                    if (z == 10):
                        break
                else:
                    z = 0
                    last_element = new_element
            except BaseException:
               break
