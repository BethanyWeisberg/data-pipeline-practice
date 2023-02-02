from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago

dag = DAG(
    'elt_pipeline_sample',
    description='A sample ELT pipeline',
    schedule_interval=timedelta(days=1),
    start_date = days_ago(1),
)

extract_iss_location_task = BashOperator(
    task_id='extract_iss_location',
    bash_command='python /p/rest_api_extract.py',
    dag=dag,
)

load_iss_location_task = BashOperator(
    task_id='load_iss_location',
    bash_command='python /p/load_to_redshift.py',
    dag=dag,
)

