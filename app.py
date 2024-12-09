import json
import pymysql
from flask import Flask, redirect, url_for, request, render_template

import sys
print("Version", sys.path)

import cryptography
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')  # This will render the login.html file

@app.route('/jobs')
def jobs():

    return render_template('indexofficial.html')

    # db = pymysql.connect(
    #     host = 'localhost',
    #     user = 'JAKEY',
    #     password = '234',
    #     db = 'jobsearch',
    #     cursorclass = pymysql.cursors.DictCursor
    # )

    # with db.cursor() as cursor:
    #     # cursor.execute('SELECT * FROM jobs WHERE job_type = \'business_intelligence_developer\';') #This is the SQL statement
    #     cursor.execute(
    #         '''SELECT j.job_id, j.job_name, j.company_name, j.location, JSON_ARRAYAGG(k.skill_name) AS skill_name
    #         FROM jobs j JOIN jobskills s ON j.job_id = s.job_id 
    #         JOIN skills k ON s.skill_id = k.skill_id
    #         GROUP BY job_id;'''
    #     )

    #     jobInfo = cursor.fetchall()

    #     for job in jobInfo:
    #         job['skill_name'] = json.loads(job['skill_name'])
    #         # job['skill_name'][1:-2].split(", ")

    #     print(jobInfo)

    #     return render_template("indexofficial.html", job_list=jobInfo)




        # jobStuff = []
        # for i in result:
        #     job_details = {
        #         "jobTitle": str(i['job_name']),
        #         "company": str(i['company_name']),
        #         "location": str(i['location']),
        #         "skills": []
        #     }

        #     # Fetch jobs for the job id using parameterized queries to prevent SQL injection
        #     cursor.execute('''
        #         SELECT s.skill_name 
        #         FROM jobs i
        #         JOIN jobskills j ON i.job_id = j.job_id
        #         JOIN skills s ON j.skill_id = s.skill_id
        #         WHERE i.job_id = %s;
        #     ''', (i['job_id'],))  # Use tuple to pass parameters safely

        #     skills = cursor.fetchall()
        #     for j in skills:
        #         job_details['skills'].append(str(j['skill_name']))
            
        #     # Add the job details to the jobStuff list
        #     jobStuff.append(job_details)

            # Return the result as a formatted JSON-like string (with proper indentation)
    # return f"Welcome {jobStuff}"
        # return 'Welcome %s' % name

@app.route('/login', methods=['POST'])
def loginPost():
    # user = request.form['nm']
    return redirect(url_for('jobs'))


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/getJobs', methods=['POST'])
def getJobs():
    db = pymysql.connect(
        host = 'localhost',
        user = 'JAKEY',
        password = '234',
        db = 'jobsearch',
        cursorclass = pymysql.cursors.DictCursor
    )

    with db.cursor() as cursor:
        # cursor.execute('SELECT * FROM jobs WHERE job_type = \'business_intelligence_developer\';') #This is the SQL statement
        cursor.execute(
            '''SELECT j.job_id, j.job_name, j.job_type, j.company_name, j.location, JSON_ARRAYAGG(k.skill_name) AS skill_name
            FROM jobs j JOIN jobskills s ON j.job_id = s.job_id 
            JOIN skills k ON s.skill_id = k.skill_id
            GROUP BY job_id;'''
        )

        jobInfo = cursor.fetchall()

        for job in jobInfo:
            job['skill_name'] = json.loads(job['skill_name'])
            # job['skill_name'][1:-2].split(", ")

        print(jobInfo)

        return jobInfo
    