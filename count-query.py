"""
Creates a timeline of the number of posts containing the indicated keyword
"""

import mysql.connector
from mysql.connector import Error

import time
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
        if (connection.is_connected()):
            cursor.close()
            connection.close()
        return records

if __name__ == "__main__":
    start_code = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", 
                        help="Keyword to be queried")
    parser.add_argument("year", 
                        help="Year to be queried")                        
    args = parser.parse_args()

    sdate = date(int(args.year),1,1)
    edate = date(int(args.year),12,31)
    dates0 = pd.date_range(sdate,edate,freq='d')
    dates = list(dates0.strftime('%Y-%m-%d'))

    result = []
    for day in dates:
        sql_select_query = f"""
            SELECT COUNT(message)
            FROM m_posts
            WHERE created_date = '{day}'
            AND message LIKE '%{args.keyword}%'
        """

        query_result = sql_query(sql_select_query)
        result.append({
            "date": day,
            "count": query_result[0][0]
        })
        print("Queried ",args.keyword," for ",day)

    df = pd.DataFrame(result)
    filename = "timeline_"+args.keyword+"_"+args.year+".csv"
    df.to_csv(filename,index=False)

    end_code = time.time()
    print("Query complete. Time spent: ",end_code - start_code," seconds")
    print("File exported as ",filename)