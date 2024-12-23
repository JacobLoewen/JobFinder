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

    return render_template('index.html')
    

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
            '''SELECT j.job_id, j.job_name, j.job_type, j.company_name, j.location, JSON_ARRAYAGG(k.skill_name) AS skill_name, JSON_ARRAYAGG(p.provider_url) AS joburl
            FROM jobs j JOIN jobskills s ON j.job_id = s.job_id 
            JOIN skills k ON s.skill_id = k.skill_id
            JOIN jobproviders p ON p.job_id = j.job_id
            GROUP BY job_id;'''
        )

        jobInfo = cursor.fetchall()

        for job in jobInfo:
            job['skill_name'] = json.loads(job['skill_name'])
            job['joburl'] = json.loads(job['joburl'])
            # job['skill_name'][1:-2].split(", ")

        print(jobInfo)

        return jobInfo
    