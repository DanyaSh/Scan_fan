    # ********************___02_selenium_00__draft___************************
'''
Legend:
🟢  1)  Создать проект
🟡  2)  Найти на сайте ссылку и скачать файл
🔴  3)  Сделать невозможное

'''
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from selenium import webdriver
from lxml import html
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=D:\\project\\User Data") # директория сохранения профиля браузера
dcap = dict(DesiredCapabilities.CHROME)
chrome = webdriver.Remote(command_executor='http://127.0.0.1:9515', desired_capabilities=dcap, options=chrome_options)
chrome.get('https://какой-то сайт/')
tree = html.fromstring(chrome.page_source)
link_l = [] #список ссылок на странице
list_group = tree.xpath('//a') # выбираем все ссылки на странице с помощью Xpath
for lg in list_group:
    link = lg.xpath('./@href') #получаем ссылку
    link_l.append(link) # добавляем ссылку в список
print (link_l) 