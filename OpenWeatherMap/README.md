 <style>
    .tab {
      tab-size: 4;
    }
  </style>

# Airflow Projects
Youtube Playlist for referance:
<br>Link - https://youtube.com/playlist?list=PLh_t6gayq9phGUKuyLlP5NU7HISwt-yfN&feature=shared
Thank You @Data Rollup from Youtube for the amazing tips.

<h2>Steps to Install Airflow on Windows using WSL</h2>

<br>sudo apt update && sudo apt upgrade -all
<br>sudo apt full-upgrade
<br>sudo apt install python3
<br>sudo apt install python3-pip
<br>sudo apt install -y python3 python3-pip python3-venv
<br>python3 -m venv airflow-venv
<br>pip install apache-airflow
<br>pip install package_name like s3fs,pandas,numpy,datetime,json,airflow,airflow.providers,csv
<br>source airflow-venv/bin/activate
<br>deactivate
<br>sudo poweroff 

<h2>To Migrate Default SQLite Database to MySQL Database:</h2>
Refer to the link below:
<br>Link - https://youtu.be/v8gbHZbttGs?feature=shared
<br>Instructions:
<br>1) Update Package Manager: 
<br> <pre class="tab">   sudo apt update </pre>
<br>2) Install MySQL on Ubuntu: 
<br>    sudo apt install mysql-server
<br>3) Creating Database for Airflow:
<br>    CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
<br>    CREATE USER 'airflow_user' IDENTIFIED BY 'airflow_pass';
<br>    GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';
<br>4) Define Connection in airflow.cfg:
<br>    sql_alchemy_conn = mysql+mysqldb://airflow_user:airflow_pass@127.0.0.1:3306/airflow_db
<br>5) Installing MYSQL client on Ubuntu:
<br>    sudo apt install libmysqlclient-dev
<br>6) Exporting Environment Variables:
<br>    export MYSQLCLIENT_CFLAGS="$(mysql_config --cflags)"
<br>    export MYSQLCLIENT_LDFLAGS="$(mysql_config --libs)"
<br>7) Pip install MYSQL Client:
<br>    pip install mysqlclient
<br>8) Migrate Airflow:
<br>    airflow db migrate
<br>9) Creating an Airflow User:
<br>    airflow users create --username <Username> --password <Password> --role Admin --firstname <FirsName> --lastname <LastName> --email <Email>
<br>    Eg. airflow users create --username admin --password admin --role Admin --firstname admin --lastname admin --email admin@example.com

# Airflow Commands:
<br>airflow db inti
<br>airflow scheduler
<br>airflow webserver -p 8080


<br>lsof -i tcp:8080
<br>kill <port_number>
--------------------------------------------------------------------------


