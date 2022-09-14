from asyncio.base_tasks import _task_repr_info
from airflow import DAG
from airflow.utils.dates import days_ago
# Operators; we need this to operate!
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
import datetime

with DAG(
    "fd1dep", 
    default_args= {"project_id":"fd1dep"}, 
    schedule_interval="2 * * * *",
    start_date=days_ago(1), 
    description="fd1dep", 
    is_paused_upon_creation=False
    ) as dag:

    ft0dep = ExternalTaskSensor(
        task_id="ft0dep", external_dag_id="fd1", 
        external_task_id="ft2",
        execution_delta=datetime.timedelta(minutes=2))
    
    
    ft1dep = DummyOperator(task_id="ft1dep")

    ft2dep = DummyOperator(task_id="ft2dep")


ft0dep >> ft1dep >> ft2dep