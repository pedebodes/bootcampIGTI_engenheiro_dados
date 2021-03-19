import prefect
from prefect import task,Flow

@task
def hello_wolrd():
    logger = prefect.context.get('logger')
    logger.info('hello, cloud merda')
    
# flow = Flow('hello-Flow_BOSTA',tasks=[hello_wolrd])

with Flow('Hello World') as flow:
    hello_wolrd()
    

# flow.run() #executar localmentre
flow.register(
    project_name="teste"
)

flow.run_agent()