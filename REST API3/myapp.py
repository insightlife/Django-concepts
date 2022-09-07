import requests
import json

url="http://127.0.0.1:8000/stget"

def get_operation(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)

def post_operation():
    data={
        'name':'dhruva',
        'roll':3,
        'city':'Ranchi'
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=url,headers=headers,data=json_data)
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


post_operation()

#get_operation(2)

#update_operation()

#delete_operation()