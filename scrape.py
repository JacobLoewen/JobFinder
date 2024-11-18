import http.client

conn = http.client.HTTPSConnection("jobs-api14.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4e151f24e1msh9db78f9b92104c2p197027jsndaedb63ba0c8",
    'x-rapidapi-host': "jobs-api14.p.rapidapi.com"
}

count = 0

with open("jobs.txt", 'r') as fJobs:
    for count, line in enumerate(fJobs):
        pass
lines = count + 1

with open("jobs.txt", 'r') as fJobs:

    for i in range(lines):

        job = (fJobs.readline()).strip()

        conn.request("GET", "/v2/list?query=" + job + "&location=Canada", headers=headers)

        res = conn.getresponse()
        data = res.read()

        newData = data.decode("utf-8")

        print(newData)

        # f = open("jobData/full_stack_developer.txt", "w")

        with open('jobData2/' + job + '.txt', 'w', encoding='utf-8') as f:
            f.write(newData)