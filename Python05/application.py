# -*-coding:utf-8 -*-


from flask import Flask, render_template

# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import json

import flask_cors
app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/crawling')
def movieJson():
    url ='https://movie.naver.com/movie/running/current.naver'
    #제목과 별점을 가져와서 
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    movies = soup.find_all('dl',class_= 'lst_dsc')
    
    # {'title':'제목', 'star':'별점'}, {}, {} ,,,] 만들고
    result_list = list()
    for movie in movies:
        temp_dict = dict()
        temp_dict['title']= movie.find('a').text
        temp_dict['star']= movie.select('.num')[0].text
        result_list.append(temp_dict)
    
    # {'movies' :[{}, {}, ...]} 형태로 만들어서 json으로 변환하고,
    result_dict = {'movies': result_list}
    result_json = json.dumps(result_dict, ensure_ascii=False)
    print(result_json)
    # json리턴!
    return result_json



    
if __name__ == '__main__':
    app.run(host='localhost', port='8686')
    
    