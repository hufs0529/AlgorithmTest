import boto3
import csv
import json
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
        data = get_sise(code, '20230101', '20230331', 'day')
        stock_data[code] = data
    return stock_data

def store_stock_data_to_s3():
    s3 = boto3.client(service_name="s3",
                      region_name="ap-northeast-2",
                      aws_access_key_id='',
                      aws_secret_access_key='')
    
    data = collect_stock_data()
    bucket_name = 'airflow-stock'
    for code, stock_data in data.items():
        csv_string = ''
        for daily_data in stock_data:
            date, close_price, volume, open_price, high_price, low_price, _ = daily_data
            row = [date, str(close_price), str(volume), str(open_price), str(high_price), str(low_price)]
            csv_string += ','.join(row) + '\n'
        key = f'stock_data/{code}.csv'
        s3.put_object(Body=csv_string, Bucket=bucket_name, Key=key)

store_stock_data_to_s3()
