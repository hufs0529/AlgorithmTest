load_operator = S3ToRedshiftOperator(
    task_id='load_stock_data_to_redshift',
    s3_bucket='your-s3-bucket-name',
    s3_key='stock_data/',
    schema='public',
    table='stock_data',
    copy_options=['JSON \'auto\''],
    redshift_conn_id='your-redshift-connection-id',
    aws_conn_id='aws_default',
    dag=dag
)