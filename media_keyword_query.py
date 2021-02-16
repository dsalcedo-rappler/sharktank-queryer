"""
Queries messages from m_posts and posts containing a given keyword: media/journalist
"""
from app_utils import sql_query, gen_dates
from datetime import date
import pymongo
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("keyword")
# args = parser.parse_args()

keyword = "media" #args.keyword

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = db_client["sharktank"]
db_coll_posts = db_mongo[keyword + "_posts"]
db_coll_mposts = db_mongo[keyword + "_mposts"]

sdate_posts = date(2016,1,1)
edate_posts = date(2018,6,25)
dates = gen_dates(sdate_posts,edate_posts)

sdate_mposts = date(2018,6,25)
edate_mposts = date(2020,12,31)
mdates = gen_dates(sdate_mposts,edate_mposts)

# Query from posts db from jan 1 2016 to june 25 2018
for day in dates:
    sql_query_string = f"""
        SELECT message,from_profile,id
        FROM posts
        WHERE created_date = '{day}'
        AND (message LIKE '%{keyword}%' OR message LIKE '%journalist%')
    """
    query_result = sql_query(sql_query_string,sleep=5.0)
    print("Queried ", keyword, " for ",day)

    if len(query_result) > 0:
        messages = []
        for entry in query_result:
            messages.append({
                "keyword": keyword,
                "date": day,
                "message": entry[0],
                "profile": entry[1],
                "post_id": entry[2]
            })
        db_coll_posts.insert_many(messages)

# Query from m_posts db from jun 25 2018 to present
for day in mdates:
    sql_query_string = f"""
        SELECT message,from_profile,id
        FROM m_posts
        WHERE created_date = '{day}'
        AND (message LIKE '%{keyword}%' OR message LIKE '%journalist%')
    """
    query_result = sql_query(sql_query_string,sleep=5.0)
    print("Queried ", keyword, " for ",day)

    if len(query_result) > 0:
        messages = []
        for entry in query_result:
            messages.append({
                "keyword": keyword,
                "date": day,
                "message": entry[0],
                "profile": entry[1],
                "post_id": entry[2]
            })
        db_coll_mposts.insert_many(messages)