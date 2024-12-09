import json
import re

theFile = open("jobs.txt", "r")

variable_names = [
    "Python", "Java", "C++", "C#", "Go", "Ruby", "Swift", "JavaScript", 
    "TypeScript", "HTML", "CSS", "PHP", "C", "Rust", "Assembly", "Haskell", 
    "Scala", "F#", "Bash", "PowerShell", "Perl", "SQL", "R", "MATLAB", "Kotlin", 
    "Objective-C", "Writing clean, maintainable, and scalable code", 
    "Debugging and troubleshooting", "Adherence to coding standards and design patterns", 
    "Git", "GitHub", "GitLab", "Bitbucket", "SVN", "Mercurial", "Object-Oriented Design", 
    "System design and architecture", "SOLID principles", "Unit testing", "JUnit", "pytest", 
    "Mocha", "Integration and functional testing", "Test automation tools", "Selenium", 
    "Cypress", "TDD", "BDD", "Technical documentation", "Markdown", "Confluence", "Swagger", 
    "OpenAPI", "React", "Angular", "Vue.js", "Svelte", "Bootstrap", "TailwindCSS", 
    "Material-UI", "Node.js", "Express", "Django", "Flask", "Ruby on Rails", "Spring Boot", 
    "ASP.NET Core", "Flutter", "React Native", "Android SDK", "iOS SDK", "TensorFlow", 
    "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "D3.js", "Unity", "Unreal Engine", 
    "Godot", "CryEngine", "MySQL", "PostgreSQL", "MariaDB", "Oracle DB", "Microsoft SQL Server", 
    "MongoDB", "CouchDB", "Firebase", "DynamoDB", "Cassandra", "Neo4j", "Amazon Neptune", 
    "Elasticsearch", "Solr", "Docker", "Kubernetes", "Jenkins", "Travis CI", "CircleCI", 
    "GitHub Actions", "AWS", "Azure", "Google Cloud", "Heroku", "DigitalOcean", "Terraform", 
    "Ansible", "CloudFormation", "Prometheus", "Grafana", "Splunk", "ELK stack", "OWASP principles", 
    "Metasploit", "Burp Suite", "Secure coding practices", "TLS", "SSL", "RSA", "AES", 
    "Problem-solving and algorithmic thinking", "Communication and collaboration", "Scrum", 
    "Kanban", "Time management", "Prioritization", "Visual Studio Code", "IntelliJ IDEA", 
    "Eclipse", "PyCharm", "Vim", "Sublime Text", "Jira", "Trello", "Asana", "Postman", "Insomnia", 
    "Figma", "Adobe XD", "Sketch", "Tableau", "Power BI", "Ethereum", "Solidity", "Artificial Intelligence", 
    "Machine Learning", "Internet of Things", "Augmented Reality", "Virtual Reality", "Hadoop", 
    "Apache Spark", "Kafka", "Arduino", "Raspberry Pi", "RTOS", "TCP/IP", "UDP", "Network security", 
    "Qiskit", "IBM Q Experience"
]

output_file = "providersSchema2.sh"

output = open(output_file, "w")

count = 1

totalCount = 1

for i in range(25): 

    fileName = theFile.readline().strip()

    print(fileName)

    # File paths
    input_file = 'jobDataTxt/' + fileName + '.txt'  # Replace with the actual input file
    output_file = 'jobSkillsSchema/' + fileName + '.sh'

    # output = open(output_file, "w")

    # fileName = '.net%20developer.txt' 

    # Load the JSON data
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract the "jobs" list and process each job
        jobs = data.get("jobs", [])
        processed_jobs = []

        onlyDescription = ""
        for job in jobs:

            content = job.get("description", "")

            # Get all variable job names from content if there are any
            matches = [var for var in variable_names if var in content] 

            # print(matches)

            # # Get parameters from 'description'
            # job_description = job.get("description", "")
            # # print(description) 

            # # Extract Job Title (assuming it's at the beginning of the description)
            # title_match = re.search(r'Job\s*Title[:\-]?\s*([A-Za-z0-9\s\.\(\)\-\,]+)', job_description)
            # title = title_match.group(1).strip() if title_match else None

            # # Extract Salary (find the first "$" and keep scanning until the last digit)
            # salary_match = re.search(r'\$\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*(?:-\s*\$\d{1,3}(?:,\d{3})*(?:\.\d+)?)?', job_description)
            # salary = salary_match.group(0).strip() if salary_match else None

            # # Output the results
            # print("Job Title:", title)
            # print("Pay:", salary)

            # Create a simplified dictionary for each job
            
            # jobType = fileName.replace("%20", "_"),
            # title = job.get("title", ""),
            # company = job.get("company", ""),
            # # description = job.get("description", ""),
            # location = job.get("location", ""),
            # datePosted = job.get("datePosted", ""),
            # jobProvider = provider.get("jobProvider", "")
            # url = provider.get("url", "")
            # "jobProviders": [
            #     {"name": provider.get("jobProvider", ""), "url": provider.get("url", "")}
            #     for provider in job.get("jobProviders", [])
            # ],

            for provider in job.get("jobProviders", []):
                jobProvider = provider.get("jobProvider", "")
                url = provider.get("url", "")
                output.write("INSERT INTO jobProviders VALUES(" + str(totalCount) + ",'" + str(url) + "','" + str(jobProvider) + "'," + str(count) + ");\n")
            #     # print("INSERT INTO jobSkills VALUES(" + str(count) + "," + str((variable_names.index(var) + 1)) + ");\n")
            #     # print(f"Saved file to {output_file}")
                totalCount += 1

            # for var in matches:
            #     jobProvider = provider.get("jobProvider", "")
            #     url = provider.get("url", "")
            #     output.write("INSERT INTO jobProviders VALUES('" + str(url) + "','" + str(jobProvider) + "'," + str(count) + ");\n")
            #     # print("INSERT INTO jobSkills VALUES(" + str(totalCount) + "," + str(count) + "," + str((variable_names.index(var) + 1)) + ");\n")
                # output.write("INSERT INTO jobSkills VALUES(" + str(totalCount) + "," + str(count) + "," + str((variable_names.index(var) + 1)) + ");\n")
                # print(f"Saved file to {output_file}")
                # totalCount += 1
            
            
            # print("INSERT INTO jobs VALUES(" + str(count) + "," + str(title)[1:-2] + "," + str(jobType)[1:-2] + "," + str(company)[1:-2] + "," + str(location)[1:-2] + "," + str(datePosted)[1:-2] + ");\n")
            # output.write("INSERT INTO jobs VALUES(" + str(count) + "," + str(title)[1:-2] + "," + str(jobType)[1:-2] +  "," + str(company)[1:-2] + "," + str(location)[1:-2] + "," + str(datePosted)[1:-2] + ");\n")
            count += 1

        # # Save the processed data to a new JSON file
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     json.dump({"jobs": processed_jobs}, f, indent=4)

        # print(f"Processed {len(processed_jobs)} jobs and saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")
