 <style>
    .tab {
      tab-size: 4;
    }
  </style>

# Airflow Projects
Youtube Playlist for referance:
<br>Link - https://youtube.com/playlist?list=PLh_t6gayq9phGUKuyLlP5NU7HISwt-yfN&feature=shared
<br>Thank You @Data Rollup from Youtube for the amazing tips.

<h2>Steps to Install Airflow using WSL-2</h2>

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
<h3>Instructions:</h3>
<br>1) Update Package Manager: 
<pre class="tab">sudo apt update </pre>
2) Install MySQL on Ubuntu: 
<pre class="tab">sudo apt install mysql-server</pre>
3) Creating Database for Airflow:
<pre class="tab">CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;</pre>
<pre class="tab">CREATE USER 'airflow_user' IDENTIFIED BY 'airflow_pass';</pre>
<pre class="tab">GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';</pre>
4) Define Connection in airflow.cfg:
<pre class="tab">sql_alchemy_conn = mysql+mysqldb://airflow_user:airflow_pass@127.0.0.1:3306/airflow_db</pre>
5) Installing MYSQL client on Ubuntu:
<pre class="tab">sudo apt install libmysqlclient-dev</pre>
6) Exporting Environment Variables:
<pre class="tab">export MYSQLCLIENT_CFLAGS="$(mysql_config --cflags)"</pre>
<pre class="tab">export MYSQLCLIENT_LDFLAGS="$(mysql_config --libs)"</pre>
7) Pip install MYSQL Client:
<pre class="tab">pip install mysqlclient</pre>
8) Migrate Airflow:
<pre class="tab">airflow db migrate</pre>
9) Creating an Airflow User:
<pre class="tab">airflow users create --username <Username> --password <Password> --role Admin --firstname <FirsName> --lastname <LastName> --email <Email></Email></pre>
Example:<br>airflow users create --username admin --password admin --role Admin --firstname admin --lastname admin --email admin@example.com

<h3>Commands to run already created Airflow Server :</h3>
<h4>- To run the server all at once, but might create errors if pre-existing server is still up</h4>
<pre class="tab">airflow standalone</pre>
<h4>- To run the server from scratch, better to run this way as the server is already create before</h4> 
<pre class="tab">airflow db inti</pre>
- Use diffterent tabs for scheduler and webserver if you are using VS Code with WSL Remote Access 
<pre class="tab">airflow scheduler</pre>
<pre class="tab">airflow webserver -p 8080</pre>


<br>lsof -i tcp:8080
<br>kill <port_number>
--------------------------------------------------------------------------


