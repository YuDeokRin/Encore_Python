# -*-coding:utf-8 -*-


from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test
encore = db.encore


#result01 = encore.insert_one({'name': 'you-dr', 'kor':100, 'eng':100, 'math':100})
#print(result01.inserted_id)

result02 = encore.insert_many([
        {'name': 'encore1', 'kor':100, 'eng':4, 'math':20},
        {'name': 'encore2', 'kor':10, 'eng':40, 'math':60}
    ])
print(result02.inserted_ids)