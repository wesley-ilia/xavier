from os.path import exists
from pandas import read_parquet
import concurrent.futures as cf
from beautiful_bot import get_all_infos
from utils import get_links, get_bodys_pages, delivery

name_parquet = "links.parquet"


def loading() -> list:
    links = read_parquet(name_parquet)['links']
    with cf.ProcessPoolExecutor() as exec:
        bodys = exec.map(get_bodys_pages, (link for link in links))
    with cf.ProcessPoolExecutor() as worker:
        data = worker.map(get_all_infos, bodys)
    return list(data)


def mapping_routes():
    if exists(name_parquet) is False:
        get_links(name_parquet)


if __name__ == "__main__":
    mapping_routes()
    data = loading()
    delivery(data)
