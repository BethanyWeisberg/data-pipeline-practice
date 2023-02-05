from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(
    'elt_pipeline_sample',
    description='A sample ELT pipeline',
    schedule_interval=timedelta(hours=6),
    start_date = days_ago(1),
)

extract_iss_location_task = BashOperator(
    task_id='extract_iss_location',
    bash_command='python /Users/computer9338/airflow/dags/rest_api_extract.py',
    dag=dag,
)

load_iss_location_task = BashOperator(
    task_id='load_iss_location',
    bash_command='python /Users/computer9338/airflow/dags/load_to_redshift.py',
    dag=dag,
)

append_iss_location_task = BashOperator(
    task_id='transform_data_model',
    bash_command='python /Users/computer9338/airflow/dags/append_iss_location.py',
    dag=dag,
)

extract_iss_location_task >> load_iss_location_task
load_iss_location_task >> append_iss_location_task
