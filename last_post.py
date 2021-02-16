"""
Updates the pages in mongodb
with the date of the page's most recent post
"""

from app_utils import sql_query
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = db_client["sharktank"]
db_coll = db_mongo["pages"]

# Retrieve data from SQL db
query_string = """
    SELECT id,name,link
    FROM pages
"""
query_result = sql_query(query_string,sleep=0.0001)

# Update the mongo database
counter_start = 26326 #start with 26326 next run
total = len(query_result)
for i in range(counter_start,total+1):
    the_id = query_result[i][0]
    query_lastdate_string = f"""
        SELECT MAX(created_time)
        FROM m_posts
        WHERE from_profile = '{the_id}'
    """
    query_lastdate = sql_query(query_lastdate_string,sleep=0.0001)

    to_set = { "$set": { "last_post": query_lastdate[0][0] } }
    to_update = db_coll.update_one({"id": the_id}, to_set)

    print("Updated document id: ", the_id, " . ", i, " out of ",total, " done.")

# test_query = db_coll.find_one({"id": "1000023020035303"})

# test_update = db_coll.update_one({"id": "1000023020035303"}, { "$set": { "last": "a" } })
# print(test_update)