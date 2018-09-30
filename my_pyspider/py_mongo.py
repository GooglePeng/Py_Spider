#!/usr/bin/env python
#-*- coding:utf-8 -*- 

# Author: Occam
# Email: 15292093662@163.com
# Date: 2018-09-30
# Version: 
# Info：测试python与MongoDB是否可以连接通并向数据库插入数据


import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['Students']
col = db['member']

'''
student={'_id':1,'name':'python','age':200}
result = col.insert(student)
print(result)
'''
studentany=[
    {'_id':1,'name':'python','age':300},
    {'_id':2,'name':'c','age':400},
    {'_id':3,'name':'java','age':500}]

result = col.insert_many(studentany)
print(result)
print(result.inserted_ids)
