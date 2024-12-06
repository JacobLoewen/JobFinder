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
    # cursor.execute('SELECT * FROM jobs WHERE job_type = \'business_intelligence_developer\';') #This is the SQL statement
    cursor.execute('SELECT * FROM jobs;')
    result = cursor.fetchall()


    for i in result:
        # print(i.keys()) #Gives the different column names (the keys) from the result that you get from cursor.fetchall()
        print("{ jobTitle: \"" + str(i['job_name']) + "\", company: \"" + str(i['company_name']) + "\", location: \"" + str(i['location']) + "\", skills: [\"", end="") #EXAMPLE: Returns the data i job_name, company_name, location
        #Fetch jobs for the job id:
        cursor.execute('SELECT i.job_id, s.skill_name FROM jobs i, jobskills j, skills s WHERE i.job_id = ' + str(i['job_id']) + ' AND i.job_id = j.job_id AND j.skill_id = s.skill_id;')
        skills = cursor.fetchall()
        for j in skills:
            print(str(j['skill_name']) + "\", \"", end="")
        print("] },\n")

    #Above is the complete MySQL data to give to the scirpt in HTML



# TO DO:

# Make possible SQL statements for the filter options that you discuss with Anubhav (Anubhav is going to take the information and present it on the website)
# 