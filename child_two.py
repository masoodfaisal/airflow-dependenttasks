from asyncio.base_tasks import _task_repr_info
from airflow import DAG
from airflow.utils.dates import days_ago
# Operators; we need this to operate!
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
import datetime

with DAG(
    "fd1dep2", 
    default_args= {"project_id":"fd1dep2"}, 
    schedule_interval="5 * * * *",
    start_date=days_ago(1), 
    description="fd1dep2", 
    is_paused_upon_creation=False
    ) as dag:

    ft0dep2 = ExternalTaskSensor(
        task_id="ft0dep2", external_dag_id="fd1", 
        external_task_id="ft2",
        execution_delta=datetime.timedelta(minutes=5))
    ft1dep2 = DummyOperator(task_id="ft1dep2")

    ft2dep2 = DummyOperator(task_id="ft2dep2")
    # BashOperator(task_id='ft2dep2',bash_command='date',)


ft0dep2 >> ft1dep2 >> ft2dep2