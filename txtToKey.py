import json
import pprint

file = open("jobData2/.net%20developer.txt")  

jsonData = file.read() # Accesses the JSON data (Which is currently a string in the file)
data = json.loads(jsonData) # Converts the string into a python dictonary

for i in range(len(data)):
    # print(i)
    pprint.pprint(data['jobs'][i]['title'])

# print(data['jobs'][0]['title'])

# print(data['jobs'][0].keys())

# pprint.pprint(data['jobs'][1]['title'])


# print(data['jobs'])