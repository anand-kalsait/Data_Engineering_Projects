# Data_Engineering_Projects
Various small projects on Data Engineering............

APACHE Airflow Instructions:
Open Visual Studio Code

Open the folder with the docker-compose file

Create a new file .env and add the following lines

Copy the below in .env file:
"AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
AIRFLOW_UID=50000"

In terminal, run the following command:
docker-compose up -d

Use the following to create Admin:
"docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin"
Eg. docker-compose run airflow-worker airflow users create --role Admin --username alex_lol --email alex_lol@gmail.com --firstname alex --lastname lol --password alex@12345

Then you can use the Airflow dashboard with the command "airflow" in the terminal and goto localhost:8080 for the admin panel in your browser.

