    # ********************___02_selenium_04__draft___************************
'''
Зайти на сайт pirate через хром инкогнито с vpn и запустить torrent
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🟢  1)  Pirate
🟢  2)  Pirate top 100
🟢  3)  Go link
🟢  4)  Run torrent
🔴  5)  Заменить Readme
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

# For linux
chrome_options.add_argument('user-data-dir=/home/danya/.config/google-chrome')

# For Windows
# chrome_options.add_argument('user-data-dir=C:\\Users\\Name_Profile\\AppData\\Local\\Google\\Chrome\\User Data')

chrome_options.add_argument("--incognito")
catalog = "/home/danya/.local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options)

# url = 'https://quotes.toscrape.com/'
# url = 'https://2ip.ru/'
url = 'https://www.pirateproxy-bay.com'
driver.get(url)
# time.sleep(300)


# text_top100 = driver.find_element_by_name(title="Top 100")
driver.find_element_by_link_text("Top 100").click()
driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
# len_lines = 101
len_lines = 3
lines = []
lines_stop = []
for x in range (1, len_lines+1):

    # line = driver.find_element_by_xpath("//tr")
    # line = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]")
    column1 = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[1]")
    indicator=column1.text[0]+column1.text[1]+column1.text[2]+column1.text[3]
    # print(indicator)
    if indicator!='Porn':
        driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[2]").click()
        driver.find_element_by_xpath("//a[@title='Get this torrent']").click()
        driver.back()
        # lines.append(line)
        pass
    else:
        # lines_stop.append(line)
        pass
# print(len(lines))
# print(len(lines_stop))
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

'''
<a title="Top torrents uploaded in the last 48 hours" href="/top/48hall">48h</a>
'''
