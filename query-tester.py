import mysql.connector
from mysql.connector import Error

import time
import pandas as pd
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
    start_code = time.time()

    sdate = date(2018,8,1)
    edate = date(2018,8,1)
    args0 = pd.date_range(sdate,edate,freq='d')
    args = list(args0.strftime('%Y-%m-%d'))

    result = []
    for day in args:
        sql_select_query = f"""
            SELECT COUNT(message)
            FROM m_posts
            WHERE created_date = '{day}'
            AND message LIKE '%presstitute%'
        """

        query_result = sql_query(sql_select_query)
        result.append(query_result)

    print(result)