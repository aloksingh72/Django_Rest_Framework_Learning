import requests
import json
URL  ="http://127.0.0.1:8000/stucreate/"

data ={
    'name':'Rahul',
    'rollno':'102',
    'city':'Delhi'
}
# to convet the python data into json
json_data = json.dumps(data)
r = requests.post(url= URL,
                  data = json_data, 
                  headers={'Content-Type': 'application/json'})

print(r.status_code)
# print(r.json())
print(r.text)
# data = r.json()
# print(data)