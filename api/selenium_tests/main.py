from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.chrome.options import Options

home = os.path.expanduser('~')
download_dir = f"{home}/Downloads"
host = os.getenv('FRONT_HOST')


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
    drive.get('http://localhost:3000')

    drive.find_element(By.CLASS_NAME, 'mercados__input-container').click()
    elements_mercados = drive.find_elements(By.CLASS_NAME,  'mercados__option')
    list_mercados = [mercado.text for mercado in elements_mercados]
    print(list_mercados)
    location = list_mercados.index('financas')
    elements_mercados[location].click()

    drive.find_element(By.CLASS_NAME, 'form-control').send_keys(f'{filename}')
    ftype = drive.find_element(By.CLASS_NAME, 'fileType__single-value')
    drive.execute_script("arguments[0].scrollIntoView();", ftype)
    sleep(1)
    ftype.click()

    sleep(1)
    elements_fileType = drive.find_elements(By.CLASS_NAME,  'fileType__option')
    list_fileType = [tp.text for tp in elements_fileType]
    # print(list_fileType)
    index = list_fileType.index(extension)
    # print(index)
    elements_fileType[index].click()

    download = drive.find_element(
            By.CSS_SELECTOR, 'button.btn-primary:nth-child(4)')
    download.click()
    sleep(10)


def test_download_file_xlsx():
    filename = 'banana'
    extension = 'Excel'
    download_file(filename, extension)
    home = os.path.expanduser('~')
    assert os.path.exists(f'{home}/Downloads/{filename}.xlsx') is True
    os.remove(f'{home}/Downloads/{filename}.xlsx')


def test_download_file_csv():
    filename = 'banana'
    extension = 'CSV'
    download_file(filename, extension)
    home = os.path.expanduser('~')
    assert os.path.exists(
            f'{home}/Downloads/{filename}.{extension.lower()}') is True
    os.remove(f'{home}/Downloads/{filename}.{extension.lower()}')


def test_download_file_pdf():
    filename = 'banana'
    extension = 'PDF'
    download_file(filename, extension)
    home = os.path.expanduser('~')
    assert os.path.exists(
            f'{home}/Downloads/{filename}.{extension.lower()}') is True
    os.remove(f'{home}/Downloads/{filename}.{extension.lower()}')
