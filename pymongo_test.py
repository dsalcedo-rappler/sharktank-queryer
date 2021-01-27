"""
Tests connection to a local MongoDB server by creating a test document
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create DB
mydb = myclient["test-database"]

# Create collection
mycol = mydb["test-collection"]

# Insert a document
entry = [{"name": "Dylan", "age": 26}]
x = mycol.insert_many(entry)

print(x)