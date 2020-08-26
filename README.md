# Apache Airflow demonstration (Python 3.8)

## Airflow initialization
```
$ export AIRFLOW_HOME=~/Documents/apache-airflow/
$ airflow initdb

-- airflow.cfg - consists of initial settings required for airflow (also db connection)

$ airflow webserver (starts a webserver and webpage with examples and DAGs)
$ airflow scheduler

-- Set load_examples = False in airflow.cfg to not see the example DAGs
```