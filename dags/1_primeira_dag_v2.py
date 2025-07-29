"""
primeira DAG v1: hello world
"""
from airflow.decorators import dag
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime

@dag(
    start_date=datetime(2023,6,1),
    schedule="@daily",
    doc_md=__doc__,
)
def a_primeira_DAG_v2():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")
    start >> hello >> end

criar_DAG = a_primeira_DAG_v2()