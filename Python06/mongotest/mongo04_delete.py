# -*-coding:utf-8 -*-


from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test

result01 = db.encore.delete_one({'name': 'kim-sd'})
print(result01)
print(result01.delete_count)


result02 = db.score.delete_many()
print(result02)
print(result02.delete_count)
