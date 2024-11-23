import json
import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'JAKEY',
    password = '234',
    db = 'jobsearch',
    cursorclass = pymysql.cursors.DictCursor
)

with db.cursor() as cursor:
    cursor.execute('SELECT * FROM jobs;') #This is the SQL statement
    result = cursor.fetchall()


    for i in result:
        print(i.keys()) #Gives the different column names (the keys) from the result that you get from cursor.fetchall()
        print(i['job_name']) #EXAMPLE: Returns the data from job_id
        print()



# TO DO:

# Make possible SQL statements for the filter options that you discuss with Anubhav (Anubhav is going to take the information and present it on the website)
# 