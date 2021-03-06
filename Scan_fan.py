    # ********************___03_Proxy_00___************************
'''
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🟢  1)  Заменить Readme
🟢  2)  Заменить код windows
🟢  3)  Пропускать ссылки с ошибкой
🟢  4)  Сделать имя пользователя переменной
🔴  5)  Почему ошибка появляется?
port proxy 443
https://hidemy.name/ru/proxy-list/?ports=443&type=s#list
'''
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# import pandas as pd
# from fake_useragent import UserAgent
# UserAgent().chrome

import requests
from bs4 import BeautifulSoup
import time
import config

free_proxy_site='https://hidemy.name/ru/proxy-list/?ports=443&type=s#list'

def find_proxy(url_proxy):
    response = requests.get(url=url_proxy)
    soup = BeautifulSoup(response.text, 'lxml')
    # proxy = soup.html.body.wrap.services_proxylist.services
    wrap = soup.html.body.wrap
    # service=wrap.next_sibling
    # proxy = service.inner.table_block.table.tr.td
    print(wrap)

# document.querySelector("body > div.wrap > div.services_proxylist.services > div > div.table_block > table > tbody > tr:nth-child(1) > td:nth-child(1)")
# <td>116.228.227.211</td>
# body > div.wrap > div.services_proxylist.services > div > div.table_block > table > tbody > tr:nth-child(1) > td:nth-child(1)
# /html/body/div[1]/div[4]/div/div[4]/table/tbody/tr[1]/td[1]
    pass

find_proxy(free_proxy_site)

'''
proxies = {'https': '116.228.227.211'}

# url = 'https://quotes.toscrape.com/'
# url = 'https://rutracker.org/'
# url = 'https://2ip.ru/'
url = 'https://www1.thepiratebay3.to/top/all'

# response = requests.get(url=url, proxies=proxies, headers={'User-Agent': UserAgent().chrome})
# response = requests.get(url=url, proxies=dict(http='socks5://user:pass@host:port', https='socks5://user:pass@host:port'))
# response = requests.get(url)
response = requests.get(url=url, proxies=proxies)

soup = BeautifulSoup(response.text, 'lxml')

file=open(("test.html"),"w")
file.write(str(soup))
file.close()
'''














'''Мусорка 4
chrome_options = webdriver.ChromeOptions()

# For linux
chrome_options.add_argument('user-data-dir=/home/'+ config.user_name +'/.config/google-chrome')
catalog = '/home/'+ config.user_name +'/.local/bin/chromedriver' #Каталог куда скачали webdriver (должен быть в PATH)

# For Windows
# chrome_options.add_argument('user-data-dir=C:\\Users\\'+ config.user_name +'\\AppData\\Local\\Google\\Chrome\\User Data')
# catalog = "C:\\Users\\"+ config.user_name +"\\AppData\\Local\\Temp\\chromedriver.exe" #Каталог куда скачали webdriver (должен быть в PATH)

chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options)

# url = 'https://quotes.toscrape.com/'
# url = 'https://2ip.ru/'
url = 'https://www.pirateproxy-bay.com'
driver.get(url)
# time.sleep(300)


# text_top100 = driver.find_element_by_name(title="Top 100")
driver.find_element_by_link_text("Top 100").click()
driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
len_lines = 100
# len_lines = 3
lines = []
lines_stop = []
for x in range (1, len_lines+1):

    # line = driver.find_element_by_xpath("//tr")
    # line = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]")
    column1 = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[1]")
    indicator=column1.text[0]+column1.text[1]+column1.text[2]+column1.text[3]
    # print(indicator)
    if indicator!='Porn':
        try:
            driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[2]").click()
            driver.find_element_by_xpath("//a[@title='Get this torrent']").click()
            # driver.find_element_by_link_text("MAGNET").click()
            driver.back()
            # lines.append(line)
        except:
            driver.get(url)
            driver.find_element_by_link_text("Top 100").click()
            driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
    else:
        # lines_stop.append(line)
        pass
# print(len(lines))
# print(len(lines_stop))
driver.close()
'''







'''Мусорка 3
# Error get this torrent
<a style="background-image: url('/static/img/icons/icon-magnet.gif');" href="magnet:?xt=urn:btih:DA51F364517AEF3934664A5E8C869C30A4BC0BE4&amp;dn=Kenan.S01E01.HDTV.x264-PHOENiX%5BTGx%5D&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&amp;tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce" title="Get this torrent" target="_blank">&nbsp;Magnet</a>
'''

# Мусорка 2
# time.sleep(1)
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
