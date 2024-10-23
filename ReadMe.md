# Introduction to Fipslogs

This project is a simple flask-based microservice with the following purpose:
This application runs e.g every 10 min, getting the needed resources, logs and status of the pod in the selected namespace. 
The logs of each pods can be saved for 24hrs in a database and be analyzed. 


Building your own Flask image that captures the status of pods, their resource usage and logs every 10 minutes is different from using established monitoring tools like Dynatrace or Splunk. Here are some of the benefits and considerations as well as the required Kubernetes resources and the appropriate database for this approach:

a) Advantages of a custom Flask image compared to Dynatrace and Splunk:
Cost control:

b) Dynatrace and Splunk are commercial tools that must be paid per resource, event or data volume. Having your own Flask image can be more cost effective, especially if only limited metrics and logs are required.
Flexibility:

c) A Flask service gives you full control over the type of data you collect, store and analyze. You can customize specific queries to your needs and process the data differently than commercial tools offer.
Data protection and control:

d) You keep the data in your infrastructure, which can be important if you don't want to send sensitive data to external providers.
Lightweight solution:

e) Having your own purpose-built solution can be lighter than big tools like Dynatrace and Splunk, which offer many more features you may not need.
Simple storage and temporary logs:

Logs are only stored for one day. A dedicated and lightweight solution makes it possible to tightly control storage requirements.

## Kubernetes resources that are required:

a) Flask application as a deployment:

    Deployment: The Flask image is provided as a deployment in Kubernetes. It ensures the scalability and management of the Flask pods.
    CronJob: You could alternatively use a Kubernetes CronJob that is executed every 10 minutes to check the status of the pods and collect the relevant data.

b) Service account:

    You will need a service account with the appropriate permissions to access the Kubernetes API. This should have the permissions to query the pod information (status, resource consumption and logs).
c) Resources for pod status, resource consumption and logs:

    kubectl (via Python Kubernetes Client API) can be used to query the following data:
    Pod status: check pod states (e.g. Running, CrashLoopBackOff).
    Resource consumption: Via the Kubernetes Metrics API endpoint (or via kubectl top pods).
    Logs: Collecting logs via kubectl logs <pod-name> for the corresponding pods.

d) Resource limits for the Flask service:

    Since the Flask service runs every 10 minutes and should generate relatively little load, you probably only need minimal resources for the pod. This depends on the size of the cluster and the number of pods, but low CPU and RAM requests/limits should be sufficient.

## Possible Databases:

Since you only want to save the logs and data for one day, the following database solutions make sense:

a) SQLite:

    SQLite could be sufficient for a small, temporary solution. It is an embedded, file-based database that does not require a separate server installation. It is well suited if the requirements for parallelism and write speed are low.

b) InfluxDB (time series database):

    If the focus is on time-based metrics and resource consumption, a time-series database such as InfluxDB would be ideal. InfluxDB is specifically optimized for time-stamped data and can handle the data structure and metrics of Kubernetes well.

c) MongoDB:

    If you prefer a schemaless solution that allows flexibility in data structure (e.g. JSON data), MongoDB could be a suitable choice. It is scalable and flexible enough to store logs and metrics in different formats.

d) PostgreSQL/MySQL:

    If you prefer structured data like tables or relational mapping, relational databases like PostgreSQL or MySQL could also be an option. Both offer robust support for various queries, but this may be overkill for data that only needs to be stored temporarily.

### Run Docker Image

1. docker build -t <my-kubectl-python-image> .
2. docker run --rm -p 5000:5000 my-kubectl-python-image

