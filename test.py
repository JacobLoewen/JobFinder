with open("jobs.txt", 'r') as fJobs:
    for count, line in enumerate(fJobs):
        pass
lines = count + 1

with open("jobs.txt", 'r') as fJobs:
    for i in range(lines):
        print((fJobs.readline()).strip())
