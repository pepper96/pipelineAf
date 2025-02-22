from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloworld():
    print("Hellow World")

with DAG(dag_id = "hellow_world_dag",
         start_date = datetime(year=2025,month=2,day=22),
         schedule_interval = "@daily",
         catchup=False) as dag:
    
    task1 = PythonOperator(
        task_id = "Hellow_world",
        python_callable = helloworld
    )


task1