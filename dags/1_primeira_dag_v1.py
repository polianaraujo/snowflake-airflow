"""
primeira DAG v1: hello world
"""
from airflow.models.dag import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime

minha_DAG = DAG(
    dag_id="a_primeira_DAG_v1",
    start_date=datetime(2023,6,1),
    schedule="@daily",
    doc_md=__doc__,
)
start = EmptyOperator(task_id="start", dag=minha_DAG)
hello = BashOperator(task_id="hello", bash_command="echo hello world", dag=minha_DAG)
end = EmptyOperator(task_id="end", dag=minha_DAG)

start >> hello >> end