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

output_file = open("jobsSchema.sh", "w")

for i in range(len(variable_names)):
    output_file.write("INSERT INTO skills VALUES(" + str(i) + ",'" + variable_names[i] + "');\n")