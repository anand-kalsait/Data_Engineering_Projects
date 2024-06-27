<h1>Airflow Project with OpenWeatherMap API</h1> 

<h2>Steps to Install Airflow using WSL-2</h2>

<h3>Prerequisites</h3>
You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11 to use the commands below.
<br>If you are on earlier versions please see the manual install page.

<br>TIP - Use PowerShell OR Command Prompt in Adminstrator mode to run the WSL commands
<br>Link to refer WSL Installation - 
<br>https://youtu.be/wjbbl0TTMeo?feature=shared

<h3>To use WSL remotely in VS Code</h3>
Youtube Link - https://youtube.com/shorts/UfPnQIBo5_I?feature=shared

<h4>Use the following Commands to get started after WSL and Ubuntu Installation</h4>
- To Update the System Files
<pre class="tab">sudo apt update && sudo apt upgrade -all</pre>
<br>- To full upgrade
<pre class="tab">sudo apt full-upgrade</pre>
- To install Python
<pre class="tab">sudo apt install python3w</pre>
- To install Pip
<pre class="tab">sudo apt install python3-pip</pre>
- To install Pip and Venv together
<pre class="tab">sudo apt install -y python3 python3-pip python3-venv</pre>
- Creating a Venv named airflow-venv
<pre class="tab">python3 -m venv airflow-venv</pre>
- To activate the Venv
<pre class="tab">source airflow-venv/bin/activate</pre>
- To install Airflow from Apache
<pre class="tab">pip install apache-airflow</pre>
- To insatll various Python Packages one by one (not all at once ^_^)
<pre class="tab">pip install "package_names" like - s3fs,pandas,numpy,datetime,json,airflow,airflow.providers,csv</pre>
- To deactivate the venv
<pre class="tab">deactivate</pre> 
- To shutdown the Ubuntu Distro
<pre class="tab">sudo poweroff </pre>

<h2>To Migrate Default SQLite Database to MySQL Database</h2>

<h3>Instructions:</h3>

1) Update Package Manager: 
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
<pre class="tab">airflow users create --username Username --password Password --role Admin --firstname FirsName --lastname LastName --email Email</pre>
Example:<br>airflow users create --username admin --password admin --role Admin --firstname admin --lastname admin --email admin@example.com<br>

Refer to the link below:
<br>Link - https://youtu.be/v8gbHZbttGs?feature=shared

<h2>Commands to run already created Airflow Server</h2>

<h4>- To run the server all at once, but might create errors if pre-existing server is still up</h4>
<pre class="tab">airflow standalone</pre>

<h4>- To run the server from scratch, better to run this way as the server is already create before</h4> 
<pre class="tab">airflow db inti</pre>

<h4>- Use diffterent tabs for scheduler and webserver if you are using VS Code with WSL Remote Access</h4> 
<pre class="tab">airflow scheduler</pre>
<pre class="tab">airflow webserver -p 8080</pre>

<h4>- To stop the server</h4>
<pre class="tab">Crtl+C</pre>

<h4>- To force stop the server use kill command with the port number given by 'lsof' command below</h4>
<pre class="tab">lsof -i tcp:8080</pre>
<pre class="tab">kill port_number </pre>

<h2>Youtube Playlist for referance</h2>

<br>Link for OpenWeatherMap API Project - <br>https://youtu.be/uhQ54Dgp6To?feature=shared
<br>Thank You @tuplespectra from Youtube for the amazing tips.<br>

<br>Link for Airflow Installation Playlist- <br>https://youtube.com/playlist?list=PLh_t6gayq9phGUKuyLlP5NU7HISwt-yfN&feature=shared
<br>Thank You @Data Rollup from Youtube for the amazing tips.<br>


