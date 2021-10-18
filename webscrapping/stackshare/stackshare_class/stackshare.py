from selenium import webdriver
import os

BASE_URL = "https://stackshare.io"

class StackShare(webdriver.Chrome):
    def __init__(self, drive_path="~/Documents/xavier/webscrapping/drive_chrome",
            teardown=False):
        self.drive_path = drive_path
        self.teardown = teardown
        os.environ['PATH'] += drive_path
        super(StackShare, self).__init__()
        self.implicitly_wait(10)


    def __exit__(self):
        if self.teardown:
            self.quit()


    def get_page(self, language=""):
        self.get("/".join([BASE_URL, language.lower()]))


    def get_companies(self):
        elements = self.find_elements_by_css_selector(
                'div[class=css-1t7lufe] > div:nth-child(3) > ul > a'
                )
        return [i.get_attribute('title') for i in elements]
        # print(elements)

