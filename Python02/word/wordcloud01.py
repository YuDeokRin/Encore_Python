# -*-coding:utf-8 -*-

#C:\Users\Drin>conda activate testenv

#(testenv) C:\Users\Drin>conda install -c conda-forge wordcloud


from wordcloud import WordCloud
import json

cloud = WordCloud(font_path='Goyang.ttf', background_color='white', max_words=30, width=400, height=300)
with open('webtoons.json', encoding='utf8') as file:
    webtoon = json.load(file)    

#print(webtoon)

res = dict()
for webtoon in webtoon['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud.png')