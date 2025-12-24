import json


studentdata = {
    "name" : "trijal",
    "roll no" : 2501010072,
    "skills" : ["gaming","web dev","python"],
    "habits" : "bad"
}


with open('json/writing.json','w') as file:
    json.dump(studentdata,file,indent=4)

print("data saved sucessfully")

with open('json/writing.json','r') as file :
    studentdataload = json.load(file)

print(studentdataload)