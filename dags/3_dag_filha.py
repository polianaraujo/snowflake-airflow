"""
DAG filha
"""

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
import datetime, pendulum, pprint

def print_filha(**kwargs):
    print("DAG filha")
    pprint.pprint(kwargs)
    return "filha"

with DAG(
    dag_id="3_DAG_filha",
    schedule="0 18 * * *",
    start_date=pendulum.datetime(2023, 6, 20, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id="start")
    wait_principal = ExternalTaskSensor(
        task_id = "wait_principal",
        external_dag_id = "DAG_principal",
        external_task_id = "python_principal",
        execution_delta = datetime.timedelta(hours=1)
        poke_interval = 30,
        mode = "reschedule",
    )
    python_filha = PythonOperator(task_id="python_filha", python_callable=print_filha)
    end = EmptyOperator(task_id="end")

start >> wait_principal >> python_filha >> end