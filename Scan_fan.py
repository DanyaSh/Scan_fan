    # ********************___02_selenium_01__Chrome+incognito+vpn___************************
'''
Зайти на сайт через хром инкогнито с vpn
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🟢  1)  Хром
🟢  2)  Инкогнито
🟢  3)  VPN

'''
from selenium import webdriver
import pandas as pd
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir=/home/danya/.config/google-chrome')
chrome_options.add_argument("--incognito")
catalog = "/home/danya/.local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options)

# url = 'https://quotes.toscrape.com/'
url = 'https://2ip.ru/'
# url = 'https://www1.thepiratebay3.to/top/all/'
# url = 'https://www.pirateproxy-bay.com'
driver.get(url)
time.sleep(300)
driver.close()
