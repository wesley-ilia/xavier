import os
from time import sleep
from pandas import read_excel, read_csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

home = os.path.expanduser('~')
download_dir = f"{home}/Downloads"
host = os.getenv('FRONT_HOST')
BASE_URL = f'http://{host}:3000'


def enable_download(driver):
    driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
    params = {
            'cmd': 'Page.setDownloadBehavior',
            'params': {'behavior': 'allow', 'downloadPath': download_dir}
            }
    driver.execute("send_command", params)


options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')
drive = webdriver.Chrome(options=options)
enable_download(drive)


def download_file(filename: str, extension: str):
    drive.get(BASE_URL)

    mercados = drive.find_element(By.CLASS_NAME, 'mercados__input-container')
    mercados.click()
    elements_mercados = drive.find_elements(By.CLASS_NAME, 'mercados__option')
    list_mercados = [mercado.text for mercado in elements_mercados]
    location = list_mercados.index('financas')
    elements_mercados[location].click()

    drive.find_element(By.CLASS_NAME, 'form-control').send_keys(f'{filename}')
    ftype = drive.find_element(By.CLASS_NAME, 'fileType__control')
    ftype.click()

    elements_fileType = drive.find_elements(By.CLASS_NAME, 'fileType__option')
    list_fileType = [tp.text for tp in elements_fileType]
    index = list_fileType.index(extension)
    elements_fileType[index].click()

    download = drive.find_element(
            By.CSS_SELECTOR, 'button.btn-primary.btn')
    download.click()
    sleep(4)


def test_download_file_xlsx():
    filename = 'banana'
    extension = 'Excel'
    download_file(filename, extension)
    assert os.path.exists(f'{download_dir}/{filename}.xlsx') is True
    os.remove(f'{download_dir}/{filename}.xlsx')


def test_download_file_csv():
    filename = 'banana'
    extension = 'CSV'
    download_file(filename, extension)
    assert os.path.exists(
            f'{download_dir}/{filename}.{extension.lower()}') is True
    os.remove(f'{download_dir}/{filename}.{extension.lower()}')


def test_download_file_pdf():
    filename = 'banana'
    extension = 'PDF'
    download_file(filename, extension)
    assert os.path.exists(
            f'{download_dir}/{filename}.{extension.lower()}') is True
    os.remove(f'{download_dir}/{filename}.{extension.lower()}')


def test_get_csv_with_dot_net_stacks_expected_only_companies_with_dot_net():
    drive.get(BASE_URL)
    sleep(1)
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='div.stacks__input-container'
            ).click()
    dot_net = filter(
            lambda x: x.text == '.net',
            drive.find_elements(
                by=By.CSS_SELECTOR,
                value='div.stacks__option'
                )
            )
    next(dot_net).click()
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='input.form-control'
            ).send_keys("dot_net")
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='button.btn-primary.btn'
            ).click()
    sleep(1)
    df = read_excel(f'{download_dir}/dot_net.xlsx')
    elements = filter(
            lambda x: '.net' not in x,
            df['stacks'].tolist()
            )
    try:
        next(elements)
        assert False
    except StopIteration:
        assert True
    # drive.close()
    if (os.path.exists(f'{download_dir}/dot_net.xlsx')):
        os.remove(f'{download_dir}/dot_net.xlsx')

def test_get_xlsx_with_python_stack_expected_only_companies_with_python():
    drive.get(BASE_URL)
    sleep(1)
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='div.stacks__input-container'
            ).click()
    python = filter(
            lambda x: x.text == 'python',
            drive.find_elements(
                by=By.CSS_SELECTOR,
                value='div.stacks__option'
                )
            )
    next(python).click()
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='input.form-control'
            ).send_keys("python")
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='button.btn-primary.btn'
            ).click()
    sleep(1)
    df = read_excel(f'{download_dir}/python.xlsx')
    elements = filter(
            lambda x: 'python' not in x,
            df['stacks'].tolist()
            )
    try:
        next(elements)
        assert False
    except StopIteration:
        assert True
    if (os.path.exists(f'{download_dir}/python.xlsx')):
        os.remove(f'{download_dir}/python.xlsx')


def test_get_csv_with_sp_state_and_expected_only_sp_state():
    drive.get(BASE_URL)
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='div.estados__input-container'
            ).click()
    sp = filter(
            lambda x: x.text == 'SP',
            drive.find_elements(
                by=By.CSS_SELECTOR,
                value='div.estados__option'
                )
            )
    next(sp).click()
    drive.find_element(
            by=By.CSS_SELECTOR,
            value='input.form-control'
            ).send_keys("sp")
    drive.find_element(By.CLASS_NAME, 'fileType__control').click()
    csv = filter(
            lambda x: x.text == 'CSV',
            drive.find_elements(
                by=By.CLASS_NAME,
                value='fileType__option'
                )
            )
    next(csv).click()
    drive.find_element(
            By.CSS_SELECTOR,
            'button.btn-primary.btn').click()
    sleep(1)
    df = read_csv(f'{download_dir}/sp.csv')
    element = filter(
            lambda x: 'sp' not in x,
            df['estado'].tolist()
            )
    try:
        next(element)
        assert False
    except StopIteration:
        assert True
    if (os.path.exists(f'{download_dir}/sp.csv')):
        os.remove(f'{download_dir}/sp.csv')