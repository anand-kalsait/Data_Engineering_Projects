from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import timedelta, datetime

default_agrs = {
    "owner":'airflow',
    'startdate':datetime(2024, 6, 13)    
}

with DAG('ETL',
         catchup=False,
         default_args=default_agrs) as dag:
    
    start = EmptyOperator(task_id='Start')
    e = EmptyOperator(task_id='Extraction')
    t = EmptyOperator(task_id='Transform')
    l = EmptyOperator(task_id='Load')
    end = EmptyOperator(task_id='End')

start >> e >> t >> l >> end