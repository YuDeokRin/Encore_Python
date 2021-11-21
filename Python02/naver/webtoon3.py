# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'


resp = requests.get(url)
#print(resp.text) 

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

webtoon_list = soup.find('ul', {'class' : 'img_list'})
#print(webtoon_list)

webtoons = webtoon_list.select('dl')
#print(webtoons)

for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    print(f'{star}\t [{title}]')