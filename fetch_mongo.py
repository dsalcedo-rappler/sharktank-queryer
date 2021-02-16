"""
Performs queries from mongodb then exports as csv
"""

import pymongo
import pandas as pd

keyword = "ressa"

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_mongo = db_client["sharktank"]
db_coll_posts = db_mongo[keyword+"_posts"]
db_coll_mposts = db_mongo[keyword+"_mposts"]

query = {"keyword": keyword}

docs = db_coll_posts.find(query)
query_list = []
for doc in docs:
    query_list.append(doc)
df = pd.DataFrame(query_list)
df = df.replace(r"\n",' ', regex=True)
print(df.head())

mdocs = db_coll_mposts.find(query)
mquery_list = []
for mdoc in mdocs:
    mquery_list.append(mdoc)
mdf = pd.DataFrame(mquery_list)
mdf = mdf.replace(r"\n",' ', regex=True)

all_df = pd.concat([df,mdf])
all_df.to_csv(keyword+".csv",index=False)

sample_df = all_df.sample(n=15000)
sample_df.to_csv(keyword+"_sample15k.csv",index=False)