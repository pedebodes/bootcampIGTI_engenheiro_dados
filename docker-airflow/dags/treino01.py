#primeira DAg com airflow

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import task
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from datetime import datetime, timedelta

#argumentos default
default_args = {
    'owner': 'Gilberto Oliveira',
    'depends_on_past':False,
    "start_date": datetime(2021, 3, 17,12),
    "email": ["gilbertoliveir@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

# definir a DAG - Fluxo
dag = DAG(
    'Treino-01',
    description='extrai dados do titanic da internet e calcula idade media dos passageiros',
    default_args=default_args,
    schedule_interval=timedelta(minutes=2)
)

get_data=BashOperator(
    task_id='get-data',
    bash_command='curl https://raw.githubusercontent.com/A3Data/hermione/master/hermione/file_text/train.csv -o ~/train.csv',
    dag=dag    
)

def calculate_idade_media():
    df =pd.read_csv('~/train.csv')
    med = df.Age.mean()
    return med


def print_idade(**context):
    value = context['task_instance'].xcom_pull(task_ids='calcula_idade_media')
    print(f'A idade media do titanic era {value} anos.')
    


task_idade_media = PythonOperator(
    task_id='calcula_idade_media',
    python_callable=calculate_idade_media,
    dag=dag
)

task_print_idade = PythonOperator(
    task_id='mostra_idade',
    python_callable=print_idade,
    dag=dag    
)

get_data >> task_idade_media >> task_print_idade

# # Comecar a adicionar tarefas
# #tarefa Bash
# hello_bash = BashOperator(
#     task_id='Hello_Basch',
#     bash_command='echo "Hello Airflow que fiz com bash" ',
#     dag=dag
# )

# #tarefa python
# def say_hello():
#     print("hello airflow form python que eu fiz")

# hello_python = PythonOperator(
#     task_id='Hello_Python',
#     python_callable=say_hello,
#     dag=dag
# )


# hello_bash >> hello_python






