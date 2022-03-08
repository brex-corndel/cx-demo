# cx-demo

Python Demo to show simple cx_oracle demo. This has been developed against an Oracle 18XE Docker image with the Sample HR Schema.

Development is local and the scripts are then packed in a Dockerfile for Distribution. CI is then done through Jenkins using the jenkinsfile. Production is an Autonomous Oracle DB in the Oracle Cloud Infeastructure(OCI).

NOTE : Some aspects of this code are for demonstration purposes. This is not intended to be a complete Application so use at your discretion.

# Build the Docker File

docker build --target development --tag epa_test .

docker build --target test --tag epa_test .

docker build --target production --tag epa_test .

docker run epa_test

