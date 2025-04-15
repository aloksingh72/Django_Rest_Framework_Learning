import requests
import json


URL ="http://127.0.0.1:8000/studentapi/"

# Performing the CRUD operations
# R--> Reading of data
# Read operations from the database
def get_data(id  = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    response = requests.get(url = URL,headers = headers, data = json_data)
    data = response.json()
    print(data)

# get_data()


# create the data
# C --> creating the data
def post_data():
    data = {
        'name':'rohan',
        'rollno':140,
        'city':'ranchi',
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    response = requests.post(url = URL,headers=headers,data = json_data)
    data = response.json()
    print(data)

# post_data()


# U--> updating the data
def update_data():
    data = {
        'id':4,
        'name':'Raju',
        'city':'Prayagraj',

    }
    headers = {'content-Type':'application/json'}
    
    json_data = json.dumps(data)
    response = requests.put(url = URL,headers=headers,data = json_data)
    data = response.json()
    print(data)

# update_data()

#D---> Delete the data

def delete_data():
    data = {
        'id':2
    }
    headers = {'content-Type':'application/json'}
    json_data  = json.dumps(data)
    response = requests.delete(url = URL,headers=headers,data = json_data)
    data = response.json()
    print(data)

delete_data()