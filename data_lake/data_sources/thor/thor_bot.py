import requests
from bs4 import BeautifulSoup


def get_name_and_stacks(page: int) -> list:
    response = requests.get(
        "https://programathor.com.br/jobs/page/" + str(page))
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select(".cell-list")
    the_list = list()
    for element in elements:
        infos = element.select("div[class=cell-list-content-icon] > span")
        if not infos:
            continue
        infos = [info.text for info in infos]
        stacks = element.select('.tag-list')
        the_list.append([infos[0], [stack.text for stack in stacks]])
    return the_list


def get_all() -> list:
    all_data = list()
    i = 0
    while True:
        data = get_name_and_stacks(i)
        if (data == []):
            break
        all_data.extend(data)
        i += 1
    return all_data
