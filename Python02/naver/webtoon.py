# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request


url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'

# url  서버와 통신
resp = urllib.request.urlopen(url)
#print(resp) 

soup = BeautifulSoup(resp, 'html.parser')
#print(soup)

webtoon_list = soup.find('ul', {'class' : 'img_list'})
#print(webtoon_list)

webtoons = webtoon_list.select('dl')
#print(webtoons)

for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    print(f'{star}\t [{title}]')