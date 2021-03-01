# ********************___04_SelRu_00__draft___************************
'''
Зайти на сайт Rutracker через хром с vpn и искать самые популярные и выгодные торренты
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🔴  1)  Заменить Readme
🟢  2)  Заменить Сайт (сразу с поиском 2021 и приоритету по личам)
🔴  3)  Выбрать самые выгодные торренты
'''
# ***********************************************************************

# import requests
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
'''
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive (FAST GET)
#caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options, desired_capabilities=caps)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import config

chrome_options = webdriver.ChromeOptions()

# For linux
chrome_options.add_argument('user-data-dir=/home/'+ config.user_name +'/.config/google-chrome')
catalog = '/home/'+ config.user_name +'/.local/bin/chromedriver' #Каталог куда скачали webdriver (должен быть в PATH)

# For Windows
# chrome_options.add_argument('user-data-dir=C:\\Users\\'+ config.user_name +'\\AppData\\Local\\Google\\Chrome\\User Data')
# catalog = "C:\\Users\\"+ config.user_name +"\\AppData\\Local\\Temp\\chromedriver.exe" #Каталог куда скачали webdriver (должен быть в PATH)

chrome_options.add_argument("--incognito")
chrome_options.add_argument
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options)

# url = 'https://quotes.toscrape.com/'
# url = 'https://2ip.ru/'
# url = 'https://www.pirateproxy-bay.com'
# url = 'https://rutracker.org/forum/tracker.php?nm=2021'
url = 'https://rutracker.org'

# Авторизация
driver.get(url)
# time.sleep(10)
driver.find_element_by_link_text("Вход").click()
driver.find_element_by_name(name="login_username").send_keys(config.login)
driver.find_element_by_name(name="login_password").send_keys(config.password)
driver.find_element_by_name(name="login").click()
driver.find_element_by_id(id_="search-text").send_keys(2021)
driver.find_element_by_id(id_="search-submit").click()
select=Select(driver.find_element_by_name(name="o")) #sort by lich
select.select_by_value("11")
driver.find_element_by_id(id_="tr-submit-btn").click()

len_pages = 10
len_lines = 50

i=1
while i<=10:
    for x in range (1, len_lines+1):

        #find value
        pretty=False
        try:
            col_value = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[6]/a")
            col_sid = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[7]/b")
            col_lich = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[8]")
        except:
            break

        sid=float(col_sid.text)
        lich=float(col_lich.text)
        dim_value=col_value.text[-4]
        value=float(col_value.text[0:-5])

        if sid>0 and lich>0 and lich/sid>config.minLS:
            if dim_value=="M":
                pretty = True
            elif dim_value=="G" and value<config.maxGB:
                pretty = True
            else:
                pretty = False

        if pretty==True:
            driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[4]/div/a").click()
            driver.find_element_by_link_text("Скачать по magnet-ссылке").click()
            # time.sleep(10)
            driver.find_element_by_id(id_="thx-btn").click()                            #To say thanks
            driver.back()
        print(x)
    if i!=10:
        driver.find_element_by_link_text("След.").click()
    print("***Page_"+str(i)+"_close")
    i+=1
driver.close()



# Мусорка 4
# '16.49 GB ↓'
# <input id="tr-submit-btn" class="bold" type="submit" value="Поиск" style="width: 140px;">
# text_top100 = driver.find_element_by_name(title="Top 100")
# driver.find_element_by_link_text("Количество личей").click()
# time.sleep(5)
'''
# driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
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
