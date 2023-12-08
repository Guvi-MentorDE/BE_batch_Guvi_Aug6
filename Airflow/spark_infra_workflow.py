from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitPySparkJobOperator,
    DataprocDeleteClusterOperator
)
from airflow.utils.dates import days_ago
from airflow.contrib.operators.dataproc_operator import DataprocClusterCreateOperator,DataProcPySparkOperator,DataprocClusterDeleteOperator



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

CLUSTER_NAME = 'spark-airflow-demo'
PROJECT_ID = 'bionic-will-406116'
dag = DAG(
    'gcp_dataproc_spark_job',
    default_args=default_args,
    description='A DAG to run Spark job on Dataproc',
    schedule_interval=timedelta(days=1),
    #scheduled_interval:"30 2 * * *"
    start_date=days_ago(1),
    tags=['emp_workflow'],
    project_id=PROJECT_ID
)

# Define cluster config
CLUSTER_NAME = 'spark-airflow-demo'
PROJECT_ID = 'bionic-will-406116'
REGION = 'us-central1'
#ZONE = 'us-central1-b'
CLUSTER_CONFIG = {
    'master_config': {
        'num_instances': 1,
        'machine_type_uri': 'n1-standard-2',  # Changed machine type
        'disk_config': {
            'boot_disk_type': 'pd-standard',
            'boot_disk_size_gb': 50
        }
    },
    'worker_config': {
        'num_instances': 2,  # Reduced the number of worker nodes to 1
        'machine_type_uri': 'n1-standard-2',  # Changed machine type
        'disk_config': {
            'boot_disk_type': 'pd-standard',
            'boot_disk_size_gb': 32
        }
    },
    'software_config': {
        'image_version': '2.1-debian11'  # This is an example, please choose a supported version.
    }
}

# create_cluster = DataprocCreateClusterOperator(
#     task_id='create_cluster',
#     cluster_name=CLUSTER_NAME,
#     project_id=PROJECT_ID,
#     region=REGION,
#     cluster_config=CLUSTER_CONFIG,
#     dag=dag,
# )
with DAG("flights_delay_etl",default_args=default_args) as dag :

    create_cluster = DataprocClusterCreateOperator(

            task_id ="create_dataproc_cluster",
            cluster_name="mycluster",
            master_machine_type="n1-standard-1",
            worker_machine_type="n1-standard-2",
            num_workers=2,
            cluster_config=CLUSTER_CONFIG,
            region=REGION
        )


    pyspark_job = {
        'main_python_file_uri': 'gs://bin_spark/spark_df2.py'
    }

    submit_pyspark_job1 = DataprocSubmitPySparkJobOperator(
        task_id='submit_pyspark_job',
        main=pyspark_job['main_python_file_uri'],
        cluster_name=CLUSTER_NAME,
        region=REGION,
        project_id=PROJECT_ID,
        dag=dag,
    )



    submit_pyspark_job2 = DataprocSubmitPySparkJobOperator(
        task_id='submit_pyspark_job',
        main=pyspark_job['main_python_file_uri'],
        cluster_name=CLUSTER_NAME,
        region=REGION,
        project_id=PROJECT_ID,
        dag=dag,
    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id='delete_cluster',
        project_id=PROJECT_ID,
        cluster_name=CLUSTER_NAME,
        region=REGION,
        trigger_rule='all_done',  # ensures cluster deletion even if Spark job fails
        dag=dag,
    )

    create_cluster >> submit_pyspark_job1 >> submit_pyspark_job2 >> delete_cluster