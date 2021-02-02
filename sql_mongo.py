"""
Queries from Sharktank DB then stores to MongoDB
"""

from app_utils import sql_query

sql_query_string = f"""
    SELECT COUNT(message)
    FROM m_posts
    WHERE created_date = '2021-01-01'
"""

x = sql_query(sql_query_string)
print(x)