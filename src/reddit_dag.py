from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime
from reddit_etl import run_extract, run_transform, run_load
import os

dag_path = os.getcwd()

default_args = {
    'retries': 5, # Número de tentativas que devem ser feitas em caso de falha da tarefa
    'retry_delay': timedelta(minutes=10), # Intervalo de tempo entre as retentativas em caso de falha.
}

with DAG(
    dag_id = 'reddit_dag', # identificador exclusivo para o DAG
    default_args = default_args,
    start_date = datetime(2023, 6, 26),
    schedule_interval = timedelta(days = 1), 
    description = 'Data pipeline com Airflow',
    cacthup = False
) as etl_dag:

    extract = PythonOperator(
        task_id = 'extract_task',
        python_callable = run_extract
    )

    sensor1 = FileSensor(
        task_id = 'json_file_sensor_task',
        filepath = f'{dag_path}/top_posts.json',
        poke_interval = 60,
        timeout = 600
    )

    transform = PythonOperator(
        task_id = 'Transform',
        python_callable = run_transform
    )

    sensor2 = FileSensor(
        task_id = 'csv_file_sensor_task',
        filepath = f'{dag_path}/career_posts.csv',
        poke_interval = 60,
        timeout = 600
    )

    load = PythonOperator(
        task_id = 'Load',
        python_callable = run_load
    )

    extract >> sensor1 >> transform >> sensor2 >> load