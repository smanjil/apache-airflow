
from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 9, 24, 10, 00, 00),
    'concurrency': 1,
    'retries': 0
}


def greet():
    print('Writing in file...')

    with open('../greet.txt', 'a+', encoding='utf-8') as f:
        now = datetime.now()
        t = now.strftime('%Y-%m-%d %H:%M')
        f.write(f'{t}\n')

    return 'Greeted'


def respond():
    return 'Greet responded again...'


with DAG('my_simple_dag',
         default_args=default_args,
         schedule_interval='*/10 * * * *') as dag:
    opr_hello = BashOperator(task_id='say_hi', bash_command='echo "Hi!!!"')
    opr_greet = PythonOperator(task_id='greet', python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep_me', bash_command='sleep 5')
    opr_respond = PythonOperator(task_id='respond', python_callable=respond)

opr_hello >> opr_greet >> opr_sleep >> opr_respond
