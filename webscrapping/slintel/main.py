import pandas as pd
import requests
from bs4 import BeautifulSoup
from slintel_bot import Slintel
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def get_links(soup: BeautifulSoup):
    box = soup.select_one('div[class="row show_intial_data_subcall"]')
    links = box.find_all('a')
    links = [link['href'] for link in links]
    return links

def match_web(links: list, website: str):
    for link in links:
        link = f'https://www.slintel.com/{link}'
        request = requests.get(link)
        if (request.status_code != 200):
            continue
        soup = BeautifulSoup(request.content, 'html.parser')
        website2 = soup.select_one('p[class="sl_subHeader hover_"]')
        if (website2.text.strip() == website):
            return link
    return ''

def get_stacks(soup: BeautifulSoup, website: str):
    links = get_links(soup)
    if links == []:
        return links
    match = match_web(links, website)
    if match == '':
        return []
    
    bot = Slintel(
    driver_path=':/home/luigi/selenium_drivers/',
    implicit_wait=10)
    bot.land_in_page(match)

    info = bot.find_element(By.CSS_SELECTOR, 'div[class="teck_stack_section st-48"]')
    drop = info.find_element(By.CSS_SELECTOR, 'select[class="techstack_select"]')

    ids = ['Programming_Languages_And_Frameworks', 'Devops_And_Development', 'IT_Security',
    'IT_Management', 'Platform_And_Storage', 'Computer_Networks', 'Operations_Software',
    'Testing_And_QA']
    stacks = []
    for i in ids:
        try:
            drop.find_element(By.CSS_SELECTOR, f'option[data-id="{i}"').click()
        except NoSuchElementException:
            continue
        soup = BeautifulSoup(info.get_attribute('innerHTML'), 'html.parser')
        s = soup.select('a[class="techstack-media-title"]')
        stacks.extend([x.text.strip() for x in s])
    return stacks
# selenium.common.exceptions.NoSuchElementException
# techstack-media-title
def format_website(website: str)-> str:
    website = website.strip()
    website = website.replace('www.', '')
    website = website.replace('https://', '')
    website = website.replace('http://', '')
    if website[-1] == '/':
        website = website[:-1]
    return website

df = pd.read_parquet('../data_files/startup.parquet')
df['name'] = df['name'].str.lower()

data = list()

for i in range(len(df['name'])):
    name = df['name'][i]
    website = format_website(df['website'][i])
    soup = requests.get(f'https://www.slintel.com/directory/company?searchTerm={name})').content
    soup = BeautifulSoup(soup, 'html.parser')
    stacks = get_stacks(soup, website)
    data.append([name, stacks])
    if i > 10:
        break

df = pd.DataFrame(
    data,
    columns=[
            'name', 'stacks'])

df.to_parquet('../data_files/slintel.parquet')

print(df)
