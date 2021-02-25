    # ********************___03_Proxy_00___************************
'''
Legend:
🟢  1)  Создать проект
🟡  2)  Найти на сайте ссылку и скачать файл
🔴  3)  Сделать невозможное

'''
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

UserAgent().chrome

# url = 'https://quotes.toscrape.com/'
url = 'https://2ip.ru/'
# url = 'https://www1.thepiratebay3.to/top/all'
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
# response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
file=open(("test.html"),"w")
file.write(str(soup))
file.close()