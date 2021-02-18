    # ********************___02_selenium_00__draft___************************
'''
Заходит на сайт тренеровок парсинга, парсит цитаты с 10 страниц
Legend:
🟢  1)  Создать проект
🟡  2)  Найти на сайте ссылку и скачать файл
🔴  3)  Сделать невозможное

'''
# import requests
# from fake_useragent import UserAgent

from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
import pandas as pd

webdriver = "/home/danya/.local/bin/"

driver = Firefox(webdriver)

# url = 'https://quotes.toscrape.com/'
# url = 'https://2ip.ru/'
# url = 'https://www1.thepiratebay3.to/top/all'

pages = 10
for page in range(1, pages):
    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
    driver.get(url)
    items = len(driver.find_elements_by_class_name("quote"))
    total = []
    for item in range(items):
        quotes = driver.find_elements_by_class_name("quote")
        for quote in quotes:
            quote_text = quote.find_element_by_class_name('text').text
            author = quote.find_element_by_class_name('author').text
            new = ((quote_text, author))
            total.append(new)
    df = pd.DataFrame(total, columns=['quote', 'author'])
    df.to_csv('quoted.csv')
driver.close()




'''
response = driver.get(url)
# response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
# response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
file=open(("test.html"),"w")
file.write(str(soup))
file.close()
'''