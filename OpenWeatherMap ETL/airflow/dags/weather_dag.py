from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor 
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
import pandas as pd
import json
import os
from csv import writer

# Function to convert Kelvin Temperature to Celsius Temperature
def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = temp_in_kelvin - 273.15
    return temp_in_celsius

# Function to Load Data into a CSV file in the current Directory
def transform_load_data(task_instance):
    data = task_instance.xcom_pull(task_ids = 'extract_weather_data')
    city = data['name']
    weather_description = data['weather'][0]['description']
    temp_celsius = kelvin_to_celsius(data['main']['temp'])
    feels_like_celsius = kelvin_to_celsius(data['main']['feels_like'])
    min_temp_celsius = kelvin_to_celsius(data['main']['temp_min'])
    max_temp_celsius = kelvin_to_celsius(data['main']['temp_max'])
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    time_of_record = datetime.fromtimestamp(data['dt'] )
    dt_time_of_record = time_of_record.strftime("%Y-%m-%d %I:%M:%S %p")
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    dt_sunrise= sunrise.strftime("%Y-%m-%d %I:%M:%S %p")
    sunset = datetime.fromtimestamp(data['sys']['sunset'])
    dt_sunset = sunset.strftime("%Y-%m-%d %I:%M:%S %p")
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %I:%M:%S %p")

    transformed_data = {
        'City': city,
        'Description': weather_description,
        'Temperature (C)': temp_celsius,
        'Feels like (C)': feels_like_celsius,
        'Minimum Temp (C)': min_temp_celsius,
        'Maximum Temp (C)': max_temp_celsius,
        'Pressure': pressure,
        'Humidity': humidity,
        'Wind Speed': wind_speed,
        'Time Of Record': dt_time_of_record,
        'Sunrise (Local Time)': dt_sunrise,
        'Sunset (Local Time)': dt_sunset,
        'Time of Data Save': dt_string
    }

    transformed_data_list = [transformed_data]
    df_data = pd.DataFrame(transformed_data_list)
    csv_name = 'current_weather_data_pune.csv'
    lisdir = os.listdir()
    if csv_name in lisdir:
        with open('current_weather_data_pune.csv','a',newline="") as csv_obj:
            writer_obj = writer(csv_obj)
            writer_obj.writerow(list(transformed_data.values()))
            csv_obj.close()
    else:
        dt_string = 'current_weather_data_pune'
        df_data.to_csv(f"{dt_string}.csv", index=False)



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "start_date": datetime(2024, 6, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'email_on_success':True,
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

# Creating a DAG
with DAG('weather_dag',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         catchup=False) as dag:
        
    # Defining tasks    
    is_weather_api_ready = HttpSensor(
        task_id = 'is_weather_api_ready',
        http_conn_id='weathermap_api',
        endpoint= '/data/2.5/weather?id=1259229&appid=<API_Token>'
    )
    
    extract_weather_data = SimpleHttpOperator(
        task_id = 'extract_weather_data',
        http_conn_id = 'weathermap_api',
        endpoint = '/data/2.5/weather?id=1259229&appid=<API_Token>',
        method = 'GET',
        response_filter = lambda r: json.loads(r.text),
        log_response = True 
    )

    transform_load_weather_data = PythonOperator(
        task_id = 'transform_load_weather_data',
        python_callable= transform_load_data,
        dag = dag
    )
    
    # Connecting tasks with their respective dependancies
    is_weather_api_ready >> extract_weather_data >> transform_load_weather_data


