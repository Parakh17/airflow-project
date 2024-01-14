from datetime import datetime
from airflow import DAG

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 12, 30, 10,00)
}


def stream_data():
    import json
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()

    res = res['results'][0]
    return res


def format_data(res):
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = res['street']['number']

stream_data()