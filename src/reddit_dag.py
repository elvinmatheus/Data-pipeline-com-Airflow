from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from reddit_etl import run_reddit_etl

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

    run_etl = PythonOperator(
        task_id='data_pipeline_completo', # Identificador exclusivo para a tarefa
        python_callable = run_reddit_etl, # A função que será executada quando a tarefa for acionada
        )