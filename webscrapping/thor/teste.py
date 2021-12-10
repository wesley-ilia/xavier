from __future__ import print_function
import json
import urllib
import urllib.parse
import urllib.request
import requests
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def launchBrowser():
	chrome_options = Options()
	chrome_options.binary_location="/home/ferrari/SeleniumDrivers/chromedriver"
	chrome_options.add_argument("start-maximized");
	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get("http://www.google.com/")
	return driver

driver = launchBrowser()

# driver = webdriver.Chrome("/home/ferrari/SeleniumDrivers/chromedriver")
# driver.get("https://www.google.com/")
""" fd = open("testee", 'w', encoding='utf8')
teste = open("teste.txt", 'w', encoding='utf8')

 
 """
""" result = requests.get("https://www.crunchbase.com/textsearch?q=afilio")
result = requests.get("https://www.google.com/search?q=decastilho+endereco")
teste.write(result.text)
teste.close
print(result.text) """

""" api_key = 'AIzaSyANiNu5fL8MGJmlpa07jzITuQLgOivwnUg'
query = 'decastilho'
service_url = 'https://kgsearch.googleapis.com/v1/LocalBusiness:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.parse.urlencode(params)
response = json.loads(urllib.request.urlopen(url).read())
for element in response['itemListElement']:
  print(element) """
