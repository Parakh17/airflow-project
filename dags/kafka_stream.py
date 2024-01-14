from datetime import datetime
from airflow import DAG
import uuid
import json
import requests
from kafka 

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 12, 30, 10,00)
}


def get_data():
    
    res = requests.get("https://randomuser.me/api/")
    res = res.json()

    res = res['results'][0]
    return res



def format_data(res):
    
    data = {}
    data['id'] = uuid.uuid4()
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                        f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code']= location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data()

stream_data()