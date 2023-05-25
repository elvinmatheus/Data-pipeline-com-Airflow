from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from reddit_etl import run_reddit_etl

default_args = {
    'owner': 'airflow', # Define o nome do proprietário ou responsável pelo fluxo de trabalho
    'depends_on_past': False, # Indica se a tarefa depende do sucesso das tarefas anteriores
    'start_date': datetime(2023, 5, 24, 23, 58), # Define a data de início do fluxo de trabalho ou da tarefa
    'email': ['airflow@example.com'], # Lista de endereços de e-mail para os quais notificações relacionadas à tarefa devem ser envidas.
    'email_on_failure': False, # Indica se deve ser enviado um e-mail em caso de falha na execução da tarefa. 
    'email_on_retry': False, # Indica se deve ser enviado um e-mail ao reexecutar a tarefa
    'retries': 1, # Número de retentativas que devem ser feitas em caso de falha da tarefa
    'retry_delay': timedelta(minutes=1) # Intervalo de tempo entre as retentativas em caso de falha.
}

dag = DAG(
    'reddit_dag', # identificador exclusivo para o DAG
    default_args=default_args, 
    description='My first ETL code',
    schedule_inteval = timedelta(days=1) # Define o agendamento do DAG
)

run_etl = PythonOperator(
    task_id='complete_reddit_etl', # Identificador exclusivo para a tarefa
    python_callable = run_reddit_etl, # A função que será executada quando a tarefa for acionada
    dag=dag # A instância do objeto DAG ao qual a tarefa pertence
)