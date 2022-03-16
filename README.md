# cx-demo

Python Demo to show simple cx_oracle demo. This has been developed against an Oracle 18XE Docker image with the Sample HR Schema.

Development is local and the scripts are then packed in a Dockerfile for Distribution. CI is then done through Jenkins using the jenkinsfile. Production is an Autonomous Oracle DB in the Oracle Cloud Infeastructure(OCI).

NOTE : Some aspects of this code are for demonstration purposes. This is not intended to be a complete Application so use at your discretion.

# Running Locally using poetry

poetry run python how_long/app.py

![image](https://user-images.githubusercontent.com/71491954/157334147-44914b1a-4fa1-437c-85c3-642dde4a40f4.png)


poetry run pytest

![image](https://user-images.githubusercontent.com/71491954/157334007-fd6d1eaa-3683-45ec-afdb-87b839f163d7.png)


# Run the database against localhost. 

To Find the IP to run against for the JDBC string run the following

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' MYORADB3

connection = cx_Oracle.connect(user="hr", password="Welcome_1", dsn="172.17.0.2/XEPDB1")

# Build the Docker File

docker build --target development --tag epa_test .

docker build --target test --tag epa_test .

docker build --target production --tag epa_test .

docker run epa_test

![image](https://user-images.githubusercontent.com/71491954/157327087-e7f6088c-b8f9-40fb-995d-0d79a1b65828.png)

# CI with Jenkins - github to Dockerhub

![image](https://user-images.githubusercontent.com/71491954/157337009-d15a99fb-6a28-42f7-97f0-5369c12978bf.png)

# Continuous Deployment to the OCI Cloud

This is run within the Cloud from Cloud Shell. It can be run from Jenkins with oci_cli installed and configured to talk to the Cloud.

docker pull container-registry.oracle.com/database/ords:latest

mkdir ords_volume ; echo 'CONN_STRING=user/password@hostname:port/service_name' > ords_volume/conn_string.txt

docker run  --rm --name ords -v `pwd`/ords_volume/:/opt/oracle/variables -p 8181:8181 container-registry.oracle.com/database/ords:latest

docker run -d --name DBCONT1 -e INIT_SGA_SIZE=1024 -e INIT_PGA_SIZE=1024 container-registry.oracle.com/database/enterprise:21.3.0.0

Docker logs DBCONT1

http://localhost:8181/ords

# Webhooks Relay

This is configured to allow working with Local Jenkins

https://my.webhookrelay.com/tokens

# Run the agent locally in Docker

export RELAY_KEY=< from webhooks Relay >
export RELAY_SECRET=< from  webhooks Relay >
Export BUCKETS=github-jenkins

docker pull webhookrelay/webhookrelayd

docker run -d --restart always \
  --name webhookrelayd \
  --network host \
  --env RELAY_KEY=$RELAY_KEY \
  --env BUCKETS=$BUCKETS \
  --env RELAY_SECRET=$RELAY_SECRET webhookrelay/webhookrelayd

  Check the logs as follows :-

  docker logs webhookrelayd

