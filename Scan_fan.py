    # ********************___03_Proxy_00_draft___************************
'''
Legend:
🟢  0)  Быть четким поцанчиком
🟡  0)  Не останавливаться на достигнутом
🔴  0)  Сделать невозможное

🔴  1)  Заменить Readme
🔴  2)  Заменить код windows
🔴  3)  Пропускать ссылки с ошибкой
🔴  4)  Сделать имя пользователя переменной
🔴  5)  Почему ошибка появляется?
port proxy 443
https://hidemy.name/ru/proxy-list/?ports=443&type=s#list
'''
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# import pandas as pd
# from requests import Request, Session

import re
import os
import requests
import lxml.html
from lxml import html
from bs4 import BeautifulSoup
import time
import config
import random
from fake_useragent import UserAgent
UserAgent().chrome

list_proxy=[]
free_proxy_site='https://hidemy.name/ru/proxy-list/?ports='+str(config.port)+'&type=s#list'
def find_proxy(url_proxy):
    '''
    proxy='alogin:parol@10.1.1.1:3128' #данные прокси; логин, пароль и айпи адрес с портом
    proxy = {'http': 'http://' + proxy, 'https': 'https://' + proxy} #делаем прокси доступным в http, https
    '''
    response = requests.get(url=url_proxy, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'lxml')
    # list_proxy=[]
    proxy=soup.tbody.find_all('tr')
    for x in proxy:
        list_proxy.append(x.td.text)
    # print(list_proxy)

print('Получаем прокси')
find_proxy(free_proxy_site)
# print(list_proxy)
# proxies = {'https': list_proxy[random.randint(0, (len(list_proxy)-1))]}
# proxies = {'https': list_proxy[1]}
proxies = {'https': '116.228.227.211'}
session = requests.session()
session.headers = {'User-Agent': UserAgent().chrome}

url = 'https://rutracker.org/forum/login.php'
login_data = {
    'login_username':config.login,
    'login_password':config.password,
    'login':'%E2%F5%EE%E4'
}
print('Авторизуемся')
r_post=session.post(url=url, proxies=proxies, data=login_data)

url = 'https://rutracker.org/forum/tracker.php?f=1105'
search_data = {
    'f[]':'1105',
    'o':'11',
    's':'2',
    'tm':'-1',
    # 'new':'1', #only new after last request
    'pn':'',
    'nm':''
}
print('Запрос торрентов')
r_post=session.post(url=url, proxies=proxies, data=search_data)
soup = BeautifulSoup(r_post.text, 'lxml')
list_lines=soup.tbody.find_all('tr')
dict_pretty={}
i=0
while i<=9:
    for line in list_lines:
        pretty=False
        try:
            col_value=line.find(class_='row4 small nowrap tor-size').a.text
            value=float(col_value[0:-5])
            dim_value=col_value[-4]
            sid=float(line.find(class_='row4 nowrap').b.text)
            leech=float(line.find(class_='row4 leechmed bold').text)
        except:
            break
        if sid>0 and leech>0 and leech/sid>config.minLS:
                if dim_value=="M":
                    pretty = True
                elif dim_value=="G" and value<config.maxGB:
                    pretty = True
                else:
                    pretty = False
        else:
            link='https://rutracker.org/forum/'+line.find(class_='row4 med tLeft t-title-col').find(class_='wbr t-title').a.attrs['href']
            pretty = False
        if pretty==True:
            link='https://rutracker.org/forum/'+line.find(class_='row4 med tLeft t-title-col').find(class_='wbr t-title').a.attrs['href']
            dict_pretty[link]={
                'link':link,
                'sid':sid,
                'leech':leech,
                'LS':leech/sid,
                'value':value,
                'col_value':col_value,
                'dim_value':dim_value
            }
        n=float(list_lines.index(line))
        print('Генерируем список_'+str((n/5)+i*10)+'%\r', end='')
    
    url_list=soup.find(class_='small bold').find_all('a')
    url='https://rutracker.org/forum/'+str(url_list[-1].attrs['href'])
    r_get=session.get(url=url, proxies=proxies)
    soup = BeautifulSoup(r_get.text, 'lxml')
    list_lines=soup.tbody.find_all('tr')
    # print('запрос на новую страницу')

    i+=1
print('Генерируем список_100%  ')

#_______________________________________Create priority list______________________________________
list_pretty=[]
dict_pretty_sort={}

for key, value in dict_pretty.items():
    # dict_pretty_sort[link]=(dict_pretty[link])['link']
    dict_pretty_sort[key]=value['LS']

dict_pretty_sort2=dict_pretty_sort
list_sort_val = sorted(dict_pretty_sort.values()) # Sort the values
list_sort_key = []

for val in list_sort_val:
    for k in dict_pretty_sort.keys():
        try:
            if dict_pretty_sort2[k] == val:
                list_sort_key.append(k)
                del dict_pretty_sort2[k]
                break
        except KeyError:
            pass

#_______________________________________Create upload list______________________________________

list_upload=[]
list_value=[]
now_value=0.00
for link in list_sort_key:
    #variabels
    atr_empt=False
    atr_value=False
    atr_len=False
    len_torrents=list_sort_key.index(link)
    dim_value=(dict_pretty[link])['dim_value']
    if dim_value=='G':
        nvalue=(dict_pretty[link])['value']
    else:
        nvalue=((dict_pretty[link])['value']/1024)
    new_value=now_value+nvalue

    #new variabels
    if list_sort_key.index(link)==0:
        atr_empt=True
    else:
        if new_value < config.your_maxGB:
            atr_value=True
        else:
            atr_value=False
        if len_torrents < config.max_len_tor:
            atr_len=True
        else:
            atr_len=False

    #update list_upload
    if atr_empt==True or (atr_value==True and atr_len==True):
        now_value=new_value
        list_upload.append(link)
        list_value.append(nvalue)
    else:
        error=link
# print('ready')

for link in list_upload:
    if os.path.exists('torrents')==False:
        os.mkdir('torrents')
    elif os.path.isdir('torrents')==False:
        os.mkdir('torrents')
    
    # change link page to link file
    url=link.replace('viewtopic', 'dl')
    f=open('torrents/'+ str(list_sort_key.index(link)) +'.torrent', 'wb')
    tor = session.get(url, proxies=proxies)
    f.write(tor.content)
    f.close()
    print('Проанализированно файлов_'+str(list_sort_key.index(link))+'\r', end='')
print('End_program                                            ')
print(list_value)
print(sum(list_value))




'''
        if os.path.exists('torrents')==False:
            os.mkdir('torrents')
        elif os.path.isdir('torrents')==False:
            os.mkdir('torrents')
        
        # change link page to link file
        url=link.replace('viewtopic', 'dl')

        f=open('torrents/'+ str(list_sort_key.index(link)) +'.torrent', 'wb')
        tor = session.get(url, proxies=proxies)
        f.write(tor.content)
        f.close()
        print('Проанализированно файлов_'+str(list_sort_key.index(link))+'\r', end='')
print('End_program                                            ')
'''

'''
f=open(r'D:\file_bdseo.zip',"wb") #открываем файл для записи, в режиме wb
# ufr = requests.get("http://site.ru/file.zip") #делаем запрос
bb3 = requests.get(url, proxies=proxy) #делаем запрос уже с прокси
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()

'''

'''
https://rutracker.org/forum/viewtopic.php?t=4476451 #page link
https://rutracker.org/forum/dl.php?t=4476451        #file link

form_token=7b28820ea2a3002461300553559d0852
https://rutracker.org/forum/dl.php?t=4476451
'''








'''
print(list_sort_key[0:20])
print('ready')
for i in sorted_values:
    for k in dict_pretty_sort.keys():
        if dict_pretty_sort[k] == i:
            dict_pretty_sorted[k] = dict_pretty_sort[k]
            break
'''
    



















'''Мусорка 5
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
'''
'''
list_linesP=[]
for tag in soup.find_all(re.compile("tCenter hl-tr"), 'tr'):
    list_linesP.append(tag)
'''
# print(list_lines)
# print(list_linesP)
# <tr id="trs-tr-5624667" class="tCenter hl-tr" role="row">
'''
file=open(("test.html"),"w")
file.write(str(soup))
file.close()
'''
'''
https://rutracker.org/forum/tracker.php?nm=2021
f%5B%5D=-1&o=11&s=2&pn=&nm=2021
'''
'''
url = 'https://rutracker.org/forum/tracker.php?nm=2021'
r_get=session.get(url=url, proxies=proxies)
soup = BeautifulSoup(r_get.text, 'lxml')
file=open(("test.html"),"w")
file.write(str(soup))
file.close()
'''
# response=requests.post(url=url, files=login_data)
# '116.228.227.211'
# '51.68.207.81'
# r_get=session.get(url=url, proxies=proxies, headers={'User-Agent': UserAgent().chrome})
# login_username=vavancheg&login_password=21091992&login=%E2%F5%EE%E4
# url = 'http://rutracker.org/forum/login.php?redirect=tracker.php?nm=2021'
# user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# response = requests.get(url=url, proxies=proxies, headers={'User-Agent': UserAgent().chrome})
# response = requests.get(url=url, proxies=proxies)
# session = requests.Session()
# response = requests.get(url=url, proxies=proxies, headers={'User-Agent': UserAgent().chrome})
# print(response.request.headers)
# r = session.post(form.action, data=form.form_values())
# response = session.get(url=url, proxies=proxies, headers={'User-Agent': UserAgent().chrome})
# r = session.post(form.action, data=form.form_values())
'''
soup = BeautifulSoup(response.text, 'lxml')
soup.find_all('Вход')
print(response.status_code)
'''
'''
# url = 'https://quotes.toscrape.com/'
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
