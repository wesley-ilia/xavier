from selenium import webdriver
from selenium.webdriver.common.by import By
import os

BASE_URL = "https://stackshare.io"

class StackShare(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.driver_path = os.getenv("DRIVER_PATH")
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
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
    
    def get_stacks_by_companies(self, company='nubank', address=r'https://stackshare.io/nubank/nubank'):
        self.get("{}".format(address))
        self.implicitly_wait(8)

        stacks = self.find_elements(By.CLASS_NAME, "css-180cglb")

        info_company = [company]
        area_dict = {}
        for function in stacks:
            area = function.find_element(By.CLASS_NAME, "css-xze7jl").find_element(By.TAG_NAME, 'h3').text
            techs = [i.text for i in function.find_elements(By.CLASS_NAME, "css-12fxiad")]
            area_dict[area] = techs
        
        info_company.append(area_dict)
        print(info_company)
