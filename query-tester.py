"""
Test for MySQL connection
"""

import mysql.connector
from mysql.connector import Error

import pandas as pd
import argparse
from datetime import date

def sql_query(query_string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3309',
            database='fbdb',
            user='socialmon',
            password='rapplers'
        )
        cursor = connection.cursor()
        cursor.execute(query_string)
        records = cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        return records

if __name__ == "__main__":
    sql_select_query = f"""
        SELECT COUNT(DISTINCT id)
        FROM m_profilelatest
        WHERE void = 0
        AND vanity_url NOT LIKE '%/'
        AND vanity_url NOT LIKE '/group%'
    """

    query_result = sql_query(sql_select_query)

    print(query_result)