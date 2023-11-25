from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # 'email': ['your-email@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'parallel_job_dag',
    default_args=default_args,
    description='My First Dag',
    schedule_interval="*/2 * * * *", # This job to get executed every 2 minutes
    start_date=datetime(2023, 11, 24),
    catchup=False,
    tags=['dev'],
)

start_task = BashOperator(task_id='start_task', bash_command='echo "Start task"', dag=dag)

task1 = BashOperator(task_id='task1', bash_command='echo "task 1"', dag=dag)
task2 = BashOperator(task_id='task2', bash_command='echo "task 2"', dag=dag)
task3 = BashOperator(task_id='task3', bash_command='echo "task 3"', dag=dag)

end_task = BashOperator(task_id='end_task', bash_command='echo "End task"', dag=dag)

start_task >> [task1, task2, task3] >> end_task
