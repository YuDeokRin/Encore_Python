# -*-coding:utf-8 -*-

from pymongo import MongoClient
from pprint import pprint


# 1. 접속
client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017')


#db = client.test
db = client['test']

#collection = db.encore
collection = db['encore']


# 2. 사용
cursor = collection.find()
#print(cursor)

#for doc in cursor:
    #pprint(doc)
    
# 조건 걸어서 하나만 가져오자!
# 이름이 hong-gd인 document만 가져오자 !
hong = collection.find_one({'name': 'hong-gd'})
pprint(hong)

hong2 = collection.find({'name': 'hong-gd'})
print(hong2)
#for doc in hong2:
    #pprint(doc)
    
#documents의 총 갯수
print(collection.count_documents({}))

kor = collection.find({'kor': {'$gt':50}}, {'_id':0})
for doc in kor:
    pprint(doc)


