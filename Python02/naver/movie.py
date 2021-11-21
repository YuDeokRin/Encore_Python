# -*-coding:utf-8 -*-

# pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request

url = 'https://movie.naver.com/movie/running/current.naver'

resp = urllib.request.urlopen(url)
#print(resp)

soup = BeautifulSoup(resp, 'html.parser')
#print(soup)


movies = soup.find_all('dl', class_='lst_dsc')
#print(len(movies))
#print(type(movies))
print(movies[0])


for movie in movies:
    #첫번째 'a'태그 가져온다.
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
    print(f'{star}\t [{title}]')