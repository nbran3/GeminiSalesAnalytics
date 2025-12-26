from airflow.models import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from ingest import ingest_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 12, 1),
    'retries': 1,
}

with DAG(
    dag_id="bronze_layer",
    default_args=default_args,
    catchup=False,
    tags=['bronze', 'Gemini'],
    max_active_runs=1
) as dag:
    bronze_data = PythonOperator(
        task_id='ingest_bronze_layer',
        python_callable = ingest_data
    )