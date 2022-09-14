# airflow-dependenttasks
this repo showcases how airflow external task sensor operator can be used to trigger tasks that are dependent on each other.

The parent_dag.py file has the parent dag with two dependent dags as child_one and child_two. Copy them in your local airflow to see the dependencies.


[DAG Dependencies](/dag_deps.png)
