# -*-coding:utf-8 -*-

import json
from pymongo import MongoClient
from pprint import pprint

# 1. starbucks.json 파일을 python으로 가지고 온다.

with open('starbucks.json', 'r' , encoding='utf-8') as f:
    json_data = f.readline()
    
#print(json_data) 



# 2. 가지고 온 json을 dictionary로 변경한다.
starbucks_dict = json.loads(json_data)
#print(starbucks_dict)

# 3. dictionary 안에 있는 'list' 라는 키의 값 (배열 -> list타입)을 mongodb에 저장한다.
# database는 test로, coolection은 starbucks01로 저장한다. 
client = MongoClient('localhost', 27017)
db = client.test
starbucks01 = db.starbucks01

res = starbucks01.insert_many(starbucks_dict['list'])
print(len(res.inserted_ids))


# 4. 다시 가져와보자 

all = starbucks01.find({})
for data in all:
    pprint(data)