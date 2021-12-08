from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


class TestSelenium(webdriver.Chrome):
    def __init__(self):
        super(TestSelenium, self).__init__()

    @staticmethod
    def download_with_headless_mode(self, )

    @staticmethod
    def tester(estados: list, mercados: list, stacks: list, name: str):
        with TestSelenium() as bot:
            bot.get("http://localhost:8000")
            estados_box = bot.find_element(By.ID, "txt_estados")
            stack_box = bot.find_element(By.ID, "txt_stacks")
            mercado_box = bot.find_element(By.ID, "txt_mercados")
            for estado in estados:
                estados_box.send_keys(estado)
                bot.find_element(By.ID, "add_estado").click()
            for mercado in mercados:
                mercado_box.send_keys(mercado)
                bot.find_element(By.ID, "add_mercado").click()
            for stack in stacks:
                stack_box.send_keys(stack)
                bot.find_element(By.ID, "add_stack").click()
