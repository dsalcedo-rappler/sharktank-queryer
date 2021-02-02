"""
Queries messages from m_posts and posts containing a given keyword
"""
from app_utils import sql_query, gen_dates
from datetime import date
import pymongo
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("keyword")
args = parser.parse_args()

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = db_client["sharktank"]
db_coll_posts = db_mongo[args.keyword + "_posts"]
db_coll_mposts = db_mongo[args.keyword + "_mposts"]

sdate_posts = date(2017,4,27)
edate_posts = date(2018,6,25)
dates = gen_dates(sdate_posts,edate_posts)

sdate_mposts = date(2020,12,17)
edate_mposts = date(2020,12,31)
mdates = gen_dates(sdate_mposts,edate_mposts)

# for day in dates:
#     sql_query_string = f"""
#         SELECT message,from_profile,id
#         FROM posts
#         WHERE created_date = '{day}'
#         AND message LIKE '%{args.keyword}%'
#     """
#     query_result = sql_query(sql_query_string,sleep=5.0)
#     print("Queried ", args.keyword, " for ",day)

#     if len(query_result) > 0:
#         messages = []
#         for entry in query_result:
#             messages.append({
#                 "keyword": args.keyword,
#                 "date": day,
#                 "message": entry[0],
#                 "profile": entry[1],
#                 "post_id": entry[2]
#             })
#         db_coll_posts.insert_many(messages)

for day in mdates:
    sql_query_string = f"""
        SELECT message,from_profile,id
        FROM m_posts
        WHERE created_date = '{day}'
        AND message LIKE '%{args.keyword}%'
    """
    query_result = sql_query(sql_query_string,sleep=5.0)
    print("Queried ", args.keyword, " for ",day)

    if len(query_result) > 0:
        messages = []
        for entry in query_result:
            messages.append({
                "keyword": args.keyword,
                "date": day,
                "message": entry[0],
                "profile": entry[1],
                "post_id": entry[2]
            })
        db_coll_mposts.insert_many(messages)