"""
Moves the pages database to mongodb
"""

from app_utils import sql_query
import pandas as pd
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = db_client["sharktank"]
db_coll = db_mongo["pages"]



# Retrieve data from SQL db
query_string = """
    SELECT id,name,link
    FROM pages
"""
query_result = sql_query(query_string,sleep=5.0)
print(len(query_result))
# Compare if found in leaderboard
df = pd.read_csv("sharktank_leaderboard_2.csv")
test = 'https://www.facebook.com/'+query_result[0][0]
# print(test)
# print(test in df['URL'].values)

all_entries = []
for entry in query_result:
    test = 'https://www.facebook.com/'+entry[0]
    in_leaderboard = test in df['URL'].values
    all_entries.append({
        "id": entry[0],
        "name": entry[1],
        "url": entry[2],
        "in_leaderboard": in_leaderboard
    })
print(len(all_entries))
# db_coll.insert_many(all_entries)