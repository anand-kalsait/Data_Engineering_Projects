# Airflow Projects
Youtube Playlist for referance:
Link - https://youtube.com/playlist?list=PLh_t6gayq9phGUKuyLlP5NU7HISwt-yfN&feature=shared
Thank You @Data Rollup from Youtube for the amazing tips.

<h2>Steps to Install Airflow on Windows using WSL</h2>

sudo apt update && sudo apt upgrade -all
sudo apt full-upgrade
sudo apt install python3
sudo apt install python3-pip
sudo apt install -y python3 python3-pip python3-venv
python3 -m venv airflow-venv
pip install apache-airflow
pip install package_name like s3fs,pandas,numpy,datetime,json,airflow,airflow.providers,csv
source airflow-venv/bin/activate
deactivate
sudo poweroff 

# To Migrate Default SQLite Database to MySQL Database:
Refer to the link below:
Link - https://youtu.be/v8gbHZbttGs?feature=shared

Instructions:
1) Update Package Manager: 
sudo apt update

2) Install MySQL on Ubuntu: 
sudo apt install mysql-server

3) Creating Database for Airflow:
CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'airflow_user' IDENTIFIED BY 'airflow_pass';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';

4) Define Connection in airflow.cfg:
sql_alchemy_conn = mysql+mysqldb://airflow_user:airflow_pass@127.0.0.1:3306/airflow_db

5) Installing MYSQL client on Ubuntu:
sudo apt install libmysqlclient-dev

6) Exporting Environment Variables:
export MYSQLCLIENT_CFLAGS="$(mysql_config --cflags)"
export MYSQLCLIENT_LDFLAGS="$(mysql_config --libs)"

7) Pip install MYSQL Client:
pip install mysqlclient

8) Migrate Airflow:
airflow db migrate

9) Creating an Airflow User:
airflow users create --username <Username> --password <Password> --role Admin --firstname <FirsName> --lastname <LastName> --email <Email>
Eg. airflow users create --username admin --password admin --role Admin --firstname admin --lastname admin --email admin@example.com

# Airflow Commands:
airflow db inti
airflow scheduler
airflow webserver -p 8080
export MYSQLCLIENT_CFLAGS="$(mysql_config --cflags)"
export MYSQLCLIENT_LDFLAGS="$(mysql_config --libs)"
pip install mysqlclient
airflow db migrate

lsof -i tcp:8080
kill
--------------------------------------------------------------------------


