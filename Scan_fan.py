    # ********************___02_selenium_02__run_top_48h_all_torrents___************************
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

'''
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
url = 'https://www.pirateproxy-bay.com'
driver.get(url)

driver.find_element_by_link_text("Top 100").click()
driver.find_element_by_xpath("//a[@href='/top/48hall']").click()
len_lines = 101
lines = []
lines_stop = []
for x in range (1, len_lines+1):
    column1 = driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[1]")
    indicator=column1.text[0]+column1.text[1]+column1.text[2]+column1.text[3]
    if indicator!='Porn':
        driver.find_element_by_xpath("//tbody/tr["+str(x)+"]/td[2]").click()
        driver.find_element_by_xpath("//a[@title='Get this torrent']").click()
        driver.back()
        pass
    else:
        pass
driver.close()