import os
import pytest
import requests
from selenium import webdriver

base_url="https://jsonplaceholder.typicode.com"

user_id=None
token=None

def test_get():
    global user_id
    headers={"Content-Type":"application/json"}
    response=requests.get(f'{base_url}/users/1',headers=headers)
    assert response.status_code==200
    data=response.json()
    assert data["id"]==1
    assert data["name"]=="Leanne Graham"
    print(data)
    user_id=data["id"]
    print(user_id)

def test_getById():
    headers={"Content-Type":"application/json"}
    response=requests.get(f'{base_url}/users/{user_id}',headers=headers)
    assert response.status_code==200
    data=response.json()
    print(data)

def test_post():
    headers={"Content-Type":"application/json"} 
    payload={
        'name': 'Abhishek D', 
        'username': 'yhiu', 
        'email': 'giug@april.biz', 
        'address': 
        {
            'street': 'gui Light', 
            'suite': 'Apt. 556', 
            'city': 'Gwenborough', 
            'zipcode': '92998-3874', 
            'geo': 
            {
                'lat': '-37.3159', 
                'lng': '81.1496'
                }
                }, 
                'phone': '1-770-736-8031 x56442', 
                'website': 'hildegard.org', 
                'company': 
                {
                    'name': 'Romaguera-Crona', 
                    'catchPhrase': 'Multi-layered client-server neural-net', 
                    'bs': 'harness real-time e-markets'
                    }
    }
    response=requests.post(f'{base_url}/users',headers=headers,json=payload)
    assert response.status_code==201
    data=response.json()
    print(data)
    user_id=data["id"]
    print(user_id)    

def test_put():
    headers={"Content-Type":"application/json"}
    payload={
        'name': 'fgfh', 
        'username': 'yhiu', 
        'email': 'giug@april.biz', 
        'address': 
        {
            'street': 'gui Light', 
            'suite': 'Apt. 556', 
            'city': 'Gwenborough', 
            'zipcode': '92998-3874', 
            'geo': 
            {
                'lat': '-37.3159', 
                'lng': '81.1496'
                }
                }, 
                'phone': '1-770-736-8031 x56442', 
                'website': 'hildegard.org', 
                'company': 
                {
                    'name': 'Romaguera-Crona', 
                    'catchPhrase': 'Multi-layered client-server neural-net', 
                    'bs': 'harness real-time e-markets'
                    }
    }
    response=requests.put(f'{base_url}/users/{user_id}',headers=headers,json=payload)
    assert response.status_code==200
    data=response.json()
    print(data)

def test_patch():
    headers={"Content-Type":"application/json"}
    payload={
        'name': 'vnbhvcnv',         
    }
    response=requests.patch(f'{base_url}/users/{user_id}',headers=headers,json=payload)
    assert response.status_code==200
    data=response.json()
    print(data)

def test_delete():
    headers={"Content-Type":"application/json"}
    response=requests.delete(f'{base_url}/users/{user_id}',headers=headers)
    assert response.status_code==200
    data=response.json()
    print(data)

def test_queryparams():
    headers={"Content-Type":"application/json"}
    params={"id":1}
    response=requests.get(f'{base_url}/users',headers=headers,params=params)
    assert response.status_code==200
    data=response.json()
    print(data)    

def test_access_token():
    global token
    headers={"Content-Type":"application/json"}
    body={}
    response=requests.post(f'{base_url}/posts',headers=headers,json=body)
    assert response.status_code==201
    data=response.json()
    token=data["token"]
    print(token)

def test_authorization_header():
    headers={"Authorization": f" Bearer {token}"}
    body={}
    response=requests.get(f'{base_url}/users',headers=headers,json=body)
    assert response.status_code==200
    data=response.json()
    print(data)    

@pytest.mark.parameterize("username","password",[("",""),("","")])
def test_8(username,password):
    response=requests.post(f'{base_url}/users/{username}')
    assert response.status_code==200
    data=response.json()
    print(data)