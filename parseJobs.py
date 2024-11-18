import json
import pprint

file = open("data.txt")  

f2 = open("jobs.txt", "w")



jsonData = file.read() # Accesses the JSON data (Which is currently a string in the file)
data = json.loads(jsonData) # Converts the string into a python dictonary

print(data['jobTitles'][0].keys())

pprint.pprint(len(data['jobTitles']))

for i in range(25):
    theStr = data['jobTitles'][i]['jobTitle']

    theParsedStr = ""

    for j in range(len(theStr)):
        if theStr[j] == " ":
            theParsedStr += "%20"
        else:
            theParsedStr += theStr[j]

    f2.write(theParsedStr + "\n")
    # pprint.pprint(data['jobTitles'][i]['jobTitle'])


# print(data['jobs'])