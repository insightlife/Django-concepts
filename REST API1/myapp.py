import requests
import json

url="http://127.0.0.1:8000/"

def get_operation(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)

def post_operation():
    data={
        'name':'dhruva',
        'roll':3,
        'city':'Ranchi'
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data= r.json()
    print(data)


def update_operation():
    data={
        'id':2,
        'name':'sai',
        'roll':30,
        'city':'Rourkela'
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data= r.json()
    print(data)

def delete_operation():
    data={'id':2}
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data= r.json()
    print(data)

#post_operation()

#get_operation(2)

#update_operation()

#delete_operation()