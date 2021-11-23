# -*-coding:utf-8 -*-


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['test']
encore = db['encore']


result01 = encore.update_one(
    {'name':'hong-gd'},
    {
        '$set':{
                'eng': 0 
            }
        }
    
    )

print(result01.matched_count)
print(result01.modified_count)

result02 = encore.update_many(
    {'math':{'$lt': 50}},
    {'$set': {'math':0}}
    
    )

print(result02)
print(result02.matched_count)
print(result02.modified_count)

