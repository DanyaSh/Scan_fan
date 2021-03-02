# ********************___04_SelRu_00__first___************************
#MAIN
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
url = 'https://rutracker.org'
driver.get(url)
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
            driver.find_element_by_id(id_="thx-btn").click()                            #To say thanks
            driver.back()
        print(x)
    if i!=10:
        driver.find_element_by_link_text("След.").click()
    print("***Page_"+str(i)+"_close")
    i+=1
driver.close()