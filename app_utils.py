import mysql.connector
from mysql.connector import Error
import time
import pandas as pd

def gen_dates(sdate,edate):
    dates0 = pd.date_range(sdate,edate,freq='d')
    dates = list(dates0.strftime('%Y-%m-%d'))
    return dates

def sql_query(query_string,sleep=30.0):
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
        time.sleep(sleep)
        return records