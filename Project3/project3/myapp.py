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
    response = requests.get(url = URL,data = json_data)
    data = response.json()
    print(data)

# get_data()


# create the data
# C --> creating the data
def post_data():
    data = {
        'name':'Man Mohan',
        'rollno':109,
        'city':'Kanpur',
    }
    json_data = json.dumps(data)
    response = requests.post(url = URL,data = json_data)
    data = response.json()
    print(data)

# post_data()


# U--> updating the data
def update_data():
    data = {
        'id':4,
        'name':'Suraj',
        'city':'Prayagraj',

    }
    json_data = json.dumps(data)
    response = requests.put(url = URL,data = json_data)
    data = response.json()
    print(data)

# update_data()

#D---> Delete the data

def delete_data():
    data = {
        'id':5
    }
    json_data  = json.dumps(data)
    response = requests.delete(url = URL,data = json_data)
    data = response.json()
    print(data)

delete_data()