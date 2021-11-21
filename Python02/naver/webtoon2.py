# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json
url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'


resp = requests.get(url)
#print(resp.text) 

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

webtoon_list = soup.find('ul', {'class' : 'img_list'})
#print(webtoon_list)

webtoons = webtoon_list.select('dl')
#print(webtoons)

values = list()

for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    #print(f'{star}\t [{title}]')
    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star
    #print(tmp)
    values.append(tmp)

#print(values)

res = dict()
res['webtoons'] = values
#print(res)

res_json = json.dumps(res, ensure_ascii=False)
print(res_json)

with open('webtoons.json', 'w', encoding='utf-8')as f :
    f.write(res_json)


