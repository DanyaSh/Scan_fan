    # ********************___03_Proxy___************************
'''READY
Bot uploads torrents to working directory from rutracker.org based on preference in config.py file
'''
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import MaxRetryError
from requests.packages.urllib3.exceptions import ProxyError as urllib3_ProxyError
import os
import requests
from bs4 import BeautifulSoup
import time
import config
import random
from fake_useragent import UserAgent

UserAgent().chrome
good_proxy=''
list_proxy=[]
free_proxy_site='https://hidemy.name/ru/proxy-list/?ports='+str(config.port)+'&type=s#list'
def find_proxy(url_proxy):
    response = requests.get(url=url_proxy, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'lxml')
    proxy=soup.tbody.find_all('tr')
    for x in proxy:
        list_proxy.append(x.td.text)
    session_test = requests.session()
    session_test.headers = {'User-Agent': UserAgent().chrome}
    url = 'https://rutracker.org/forum/login.php'
    login_data = {
        'login_username':config.login,
        'login_password':config.password,
        'login':'%E2%F5%EE%E4'
    }
    for proxy in list_proxy:
        proxies = {'https': proxy}
        try:
            print('requests_proxy')
            r_post=session_test.post(url=url, proxies=proxies, data=login_data)
            print('check_proxy_ok')
        except ConnectionError as ce:
            if (isinstance(ce.args[0], MaxRetryError) and isinstance(ce.args[0].reason, urllib3_ProxyError)):
                print('bad_proxy:_'+str(list_proxy.index(proxy)))
                list_proxy.remove(proxy)
                pass
print('Get_proxy')
find_proxy(free_proxy_site)
proxies = {'https': list_proxy[random.randint(0, (len(list_proxy)-1))]}
session = requests.session()
session.headers = {'User-Agent': UserAgent().chrome}
url = 'https://rutracker.org/forum/login.php'
login_data = {
    'login_username':config.login,
    'login_password':config.password,
    'login':'%E2%F5%EE%E4'
}
print('Authorization')
r_post=session.post(url=url, proxies=proxies, data=login_data)
url = 'https://rutracker.org/forum/tracker.php?f='+config.selection
search_data = {
    'f[]':config.selection,
    'o':'11',
    's':'2',
    'tm':'-1',
    # 'new':'1', #only new after last request
    'pn':'',
    'nm':''
}
print('Get_torrents')
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
        print('Generating a list _'+str((n/5)+i*10)+'%\r', end='')
    url_list=soup.find(class_='small bold').find_all('a')
    url='https://rutracker.org/forum/'+str(url_list[-1].attrs['href'])
    r_get=session.get(url=url, proxies=proxies)
    soup = BeautifulSoup(r_get.text, 'lxml')
    list_lines=soup.tbody.find_all('tr')
    i+=1
print('Generating a list _100%  ')
list_pretty=[]
dict_pretty_sort={}
for key, value in dict_pretty.items():
    dict_pretty_sort[key]=value['LS']
dict_pretty_sort2=dict_pretty_sort
list_sort_val = sorted(dict_pretty_sort.values(), reverse=True) # Sort the values
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
list_upload=[]
list_value=[]
now_value=0.00
for link in list_sort_key:
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
    if atr_empt==True or (atr_value==True and atr_len==True):
        now_value=new_value
        list_upload.append(link)
        list_value.append(nvalue)
    else:
        error=link
for link in list_upload:
    if os.path.exists('torrents')==False:
        os.mkdir('torrents')
    elif os.path.isdir('torrents')==False:
        os.mkdir('torrents')
    url=link.replace('viewtopic', 'dl')
    f=open('torrents/'+ str(list_sort_key.index(link)) +'.torrent', 'wb')
    tor = session.get(url, proxies=proxies)
    f.write(tor.content)
    f.close()
    print('Analyzed files_'+str(list_sort_key.index(link))+'\r', end='')
print("Redy_to_have_"+str(sum(list_value))+"_GB                               ")
print('End_program')