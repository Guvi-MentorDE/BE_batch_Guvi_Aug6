from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitPySparkJobOperator,
    DataprocDeleteClusterOperator
)
from airflow.providers.google.cloud.sensors.gcs import (
    GCSObjectExistenceSensor,
    GCSObjectsWithPrefixExistenceSensor)
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_workflow',
    default_args=default_args,
    description='A DAG to run Spark job on Dataproc',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=['example'],
)

# Define cluster config
CLUSTER_NAME = 'cluster-3e36'
PROJECT_ID = 'bionic-will-406116'
REGION = 'us-central1'
#REGION = 'us-central1-c'
#ZONE = 'us-central1-b'
BUCKET_1 = 'dedatadev'
FILE_PREFIX = 'custs.txt'

pyspark_job = {
    'main_python_file_uri': 'gs://bin_spark/spark_df2.py'
}

gcs_object_with_prefix_exists = GCSObjectsWithPrefixExistenceSensor(
        bucket=BUCKET_1,
        prefix=FILE_PREFIX,
        mode='poke',
        task_id="gcs_object_with_prefix_exists_task",
    )

submit_pyspark_job = DataprocSubmitPySparkJobOperator(
    task_id='submit_pyspark_job',
    main=pyspark_job['main_python_file_uri'],
    cluster_name=CLUSTER_NAME,
    region=REGION,
    project_id=PROJECT_ID,
    dag=dag,
)

end_task = BashOperator(task_id='end_task', bash_command='echo "End task"', dag=dag)



gcs_object_with_prefix_exists >> submit_pyspark_job >> end_task