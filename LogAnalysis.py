#!/usr/bin/env python
import psycopg2
# Connecting the database and creating object
connection = psycopg2.connect(
    database="news", user="vagrant", password="vagrant")
cursor = connection.cursor()

# Database queries
# Database query 1: What are the three most popular articles of all time?
aricles_db = """select * from atriclesdata"""
# Database query 2: Who are the most popular article authors of all time?
authors_db = """select * from pop_auth"""
# Database query 3: On which day did more than 1% of requests lead to errors?
error_db = "select * from finalresult where percent>1"

# Print the top three articles of all time
try:
    cursor.execute(aricles_db)
    result1 = cursor.fetchall()
    connection.commit()
    print("These Are The Popular 3 Articles All Time:")
    for i, value in enumerate(result1):
        print('\t' + str(result1[i]) + " views")
except Exception as e:
    print(e)
# Print the top authors of all time
try:
    cursor.execute(authors_db)
    result2 = cursor.fetchall()
    print("These are The Popular 3 Authors All Time Are:")
    for i, value in enumerate(result2):
        print('\t' + str(result2[i]) + " views")
except Exception as e:
    print(e)
# Print the days in which there were more than 1% bad requests
try:
    cursor.execute(error_db)
    fetcheddata = cursor.fetchall()
    print("This Days got 1% of errors:")
    i = 0
    while(i < len(fetcheddata)):
        print(str(fetcheddata[i]) + "errors")
        i = i + 1
except Exception as e:
    print(e)
cursor.close()
connection.close()
