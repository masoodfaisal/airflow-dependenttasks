from airflow import DAG
from airflow.utils.dates import days_ago
# Operators; we need this to operate!
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

with DAG(
    "fd1", 
    default_args= {"project_id":"fd1"}, 
    schedule_interval="0 * * * *",
    start_date=days_ago(1), 
    description="fd1", 
    is_paused_upon_creation=False
    ) as dag:


    ft1 = DummyOperator(task_id="ft1")

    ft2 = DummyOperator(task_id="ft2")


ft1 >> ft2