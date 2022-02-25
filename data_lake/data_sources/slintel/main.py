import concurrent.futures as cf
from utils_get_by_website import delivery, packaging, loading_info_from_parquet


def main():
    with cf.ProcessPoolExecutor(max_workers=10) as worker:
        data = worker.map(packaging, loading_info_from_parquet())
    dt = {name: stacks for name, stacks in data}
    delivery(dt)


if __name__ == "__main__":
    main()
