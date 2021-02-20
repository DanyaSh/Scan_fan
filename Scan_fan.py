    # ********************___02_selenium_02__run_top_48h_all_torrents___************************
'''MASTER
Зайти на сайт pirate через хром инкогнито с vpn и запустить torrent
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🟢  1)  Заменить Readme
🟢  2)  Заменить код windows
🟢  3)  Пропускать ссылки с ошибкой
🟢  4)  Сделать имя пользователя переменной
🔴  5)  Почему ошибка появляется?
'''
from selenium import webdriver
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
driver = webdriver.Chrome(executable_path=catalog, chrome_options=chrome_options)
url = 'https://www.pirateproxy-bay.com'
driver.get(url)

driver.find_element_by_link_text("Top 100").click()
driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
len_lines = 100
lines = []
lines_stop = []
for x in range (1, len_lines+1):
    column1 = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[1]")
    indicator=column1.text[0]+column1.text[1]+column1.text[2]+column1.text[3]
    if indicator!='Porn':
        try:
            driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[2]").click()
            driver.find_element_by_xpath("//a[@title='Get this torrent']").click()
            driver.back()
        except:
            driver.get(url)
            driver.find_element_by_link_text("Top 100").click()
            driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
    else:
        pass
driver.close()
