from s3 import S3
from os import getenv
from time import sleep
from bs4 import BeautifulSoup
import concurrent.futures as cf
from slintel_bot import Slintel
from pandas import read_parquet, DataFrame
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


BASE_URL = "https://www.slintel.com/search?searchTerm="

stacks_box_needed = {
        "Programming Languages And Frameworks",
        "Devops And Development",
        "IT Security",
        "IT Management",
        "Platform And Storage",
        "Computer Networks",
        "Operations Software",
        "Testing And QA"
        }


def loading():
    with cf.ProcessPoolExecutor() as worker:
        data = worker.map(packaging, loading_info_from_parquet())
    dt = {name: stacks for name, stacks in data}
    return dt


def delivery(data):
    df = DataFrame(
            data={
                "name": data.keys(),
                "stacks": data.values()
                }
            )
    driver = S3()
    driver.send_to_s3(
            df=df,
            bucket_name=getenv("BUCKET_NAME"),
            destination=getenv("DESTINATION")
            )


def format_website(website):
    website = website.replace("https:", '').replace("http:", '')
    website = website.replace("www.", '').replace("//", '').replace('/', '')
    return website


def format_names(name):
    name = name.replace(".com", '').replace('[', '')
    name = name.replace('[', '').replace(':', '')
    return name


def select_itens_in_dropbox(bot: Slintel):
    """Select which itens of stacks_box_needed
    has in dropdown of company page"""
    try:
        dropdown = bot.find_element(by=By.CLASS_NAME, value="techstack_select")
    except NoSuchElementException:
        return ()
    return filter(
            lambda x: x.text in stacks_box_needed,
            dropdown.find_elements(
                by=By.TAG_NAME, value="option")
            )


def get_stacks_from_page(bot: Slintel, selector: str) -> set:
    """Parse stacks from html page"""
    stacks = bot.find_element(
            by=By.CSS_SELECTOR,
            value=selector
            )
    soup = BeautifulSoup(stacks.get_attribute('innerHTML'), 'html.parser')
    return {stack.text.strip(" \n") for stack in soup.select('a')}


def get_first_element_name_on_dropdown(bot: Slintel):
    try:
        first_element_in_dropdown = bot.find_element(
            by=By.CSS_SELECTOR,
            value='select.techstack_select > option'
            ).text
    except NoSuchElementException:
        return None
    return first_element_in_dropdown


def loading_info_from_parquet():
    with S3() as connection:
        name = 'scrappy.parquet'
        connection.download_from_s3(
            bucket_name=getenv('BUCKET_NAME'),
            obj_name=getenv("OBJ_NAME"),
            name=name
            )
        sleep(1)
        df_startup = read_parquet(name)
        df_startup["website"] = df_startup["website"].str.lower()
        return zip(
            map(format_website, df_startup['website']),
            map(format_names, df_startup['name'])
            )


def packaging(values: tuple) -> dict:
    name = values[1]
    stacks = set()
    with Slintel(headless=True) as bot:
        bot.land_in_page(BASE_URL + values[0])
        try:
            button = bot.find_element(
                    by=By.CSS_SELECTOR, value="div.media-body > h5 > a")
            button.click()
        except NoSuchElementException:
            return (name, stacks)
        itens_in_dropbox = select_itens_in_dropbox(bot)
        if get_first_element_name_on_dropdown(bot) in stacks_box_needed:
            stacks.update(get_stacks_from_page(
                bot,
                'div[class="row techstack_card show_techstack_init"]'
                ))
            next(itens_in_dropbox)
        for item in itens_in_dropbox:
            item.click()
            stacks.update(get_stacks_from_page(
                bot,
                'div[class="row techstack_card show_techstack_onchange"]'
                ))
    return (name, stacks)
