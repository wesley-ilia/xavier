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


    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.teardown:
            self.quit()


    def land_in_page(self, *args):
        self.get("/".join([BASE_URL, *args]))


    def click_on(self, css_selector: str):
        link = self.find_element_by_css_selector(css_selector)
        link.click()


    def get_info(self, css_selector: str, attribute: str):
        elements = self.find_elements_by_css_selector(css_selector)
        return [i.get_attribute(attribute) for i in elements]
