# -*-coding:utf-8 -*-


from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['test']
encore= db['encore']

aggr = encore.aggregate([
        {'$match': {'kor': {'$gt': 80}}},
        {'$group': {'_id':'kor', 'sum': {'$sum': '$kor'}}}
    ])

print(aggr)
pprint(list(aggr))
