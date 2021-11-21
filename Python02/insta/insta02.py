# -*-coding:utf-8 -*-


#pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time


tag = input('search tag :')
url = 'https://www.instagram.com/explore/tags/' + tag


#webdriver 검색해서, 설치되어 있는 chrome과 같은 버젼의 chromedriver 다운로드!
driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')


driver.get(url)
print(driver.page_source)

# driver.implicitly_way(3)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.find_all('div', class_="KL4Bh"))