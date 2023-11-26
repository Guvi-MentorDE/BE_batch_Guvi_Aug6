from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitPySparkJobOperator,
    DataprocDeleteClusterOperator
)
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pyspark_job',
    default_args=default_args,
    description='A DAG to run Spark job on Dataproc',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=['example'],
)

# Define cluster config as per your cuslter name and project name. Change the region if required , check in the config section.
CLUSTER_NAME = 'cluster-3e36'
PROJECT_ID = 'bionic-will-406116'
REGION = 'us-central1'
#REGION = 'us-central1-c'
#ZONE = 'us-central1-b'



pyspark_job = {
    'main_python_file_uri': 'gs://bin_spark/spark_df2.py'  #change as per your bucket name 
}

submit_pyspark_job = DataprocSubmitPySparkJobOperator(
    task_id='submit_pyspark_job',
    main=pyspark_job['main_python_file_uri'],
    cluster_name=CLUSTER_NAME,
    region=REGION,
    project_id=PROJECT_ID,
    dag=dag,
)


submit_pyspark_job