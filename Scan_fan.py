    # ********************___02_selenium_00__draft___************************
'''
Legend:
🟢  1)  Создать проект
🟡  2)  Найти на сайте ссылку и скачать файл
🔴  3)  Сделать невозможное

'''
from selenium.webdriver import Firefox
import pandas as pd

webdriver = "geckodriver"

driver = Firefox(webdriver)

url = 'https://quotes.toscrape.com/'
# url = 'https://2ip.ru/'
# url = 'https://www1.thepiratebay3.to/top/all'

driver.get(url)