    # ********************___02_selenium_02__draft___************************
'''
Зайти на сайт через хром инкогнито с vpn
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🔴  1)  Pirate
🔴  2)  Pirate top 100
🔴  3)  Get link

'''
# import requests
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options

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















# Мусорка 2
# chrome_options.add_argument('headless')

'''
Мусорка 1
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

'''
Мусорка 0
response = driver.get(url)
# response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
# response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
file=open(("test.html"),"w")
file.write(str(soup))
file.close()
'''

'''
<a href="https://www1.thepiratebay3.to/top" title="Top 100" class="clickopen_" data-open="https://www.get-express-vpn.com/offer/torrent-vpn-2?a_fid=proxyspace&amp;offer=3monthsfree" rel="nofollow">Top 100</a>
'''