from datetime import datetime
from airflow import DAG

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 12, 30, 10,00)
}
