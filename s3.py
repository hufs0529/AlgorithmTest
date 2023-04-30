from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
# from airflow.providers.postgres.operators.s3_to_redshift import S3ToRedshiftOperator
from urllib import parse
from ast import literal_eval
import requests

def get_sise(code, start_time, end_time, time_from='day'):
    get_param = {
        'symbol': code,
        'requestType': 1,
        'startTime': start_time,
        'endTime': end_time,
        'timeframe': time_from
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.finance.naver.com/siseJson.naver?%s" % (get_param)
    response = requests.get(url)
    return literal_eval(response.text.strip())

def collect_stock_data():
    stock_codes = ['005930', '035420']
    stock_data = {}
    for code in stock_codes:
        data = get_sise(code, '20210601', '20210603', 'day')
        stock_data[code] = data
    return stock_data

def store_stock_data_to_s3():
    hook = S3Hook(aws_conn_id='stock-s3')
    data = collect_stock_data()
    bucket_name = 'airflow-stock'
    for code, stock_data in data.items():
        csv_string = ''
        for daily_data in stock_data:
            date, close_price, volume, open_price, high_price, low_price, _ = daily_data
            row = [date, str(close_price), str(volume), str(open_price), str(high_price), str(low_price)]
            csv_string += ','.join(row) + '\n'
        key = f'stock_data/{code}.csv'
        hook.load_string(csv_string, key, bucket_name)


default_args = {
    'owner': 'your-name',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='collect_stock_data_s3',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1) # run every midnight
)
# '0 0 * * * '
collect_operator = PythonOperator(
    task_id='collect_stock_data',
    python_callable=collect_stock_data,
    dag=dag
)

store_operator = PythonOperator(
    task_id='store_stock_data_to_s3',
    python_callable=store_stock_data_to_s3,
    dag=dag
)

collect_operator >> store_operator