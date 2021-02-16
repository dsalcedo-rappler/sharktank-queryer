"""
Tests connection to MySQL database
"""

from app_utils import sql_query

query_string = """
    SELECT id
    FROM m_posts
    LIMIT 10
"""

query = sql_query(query_string,sleep=2.0)

print(query)