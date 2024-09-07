from SPARQLWrapper import SPARQLWrapper, JSON
import time
import os
BENCHMARK_ROOT = '/data2/benchmark'

QUERY_ROOT = ''
PORT = 1111

ENDPOINTS = 'http://localhost:8890/sparql'

RESUME_FILE = f'{BENCHMARK_ROOT}/results/result.csv'
ERROR_FILE  = f'{BENCHMARK_ROOT}/results/errors/error.log'


def execute_sparql_wrapper(query_pattern, query_number):
    query = query_pattern

    sparql_wrapper = SPARQLWrapper(ENDPOINTS)
    # sparql_wrapper.setTimeout(TIMEOUT+10) # Give 10 more seconds for a chance to graceful timeout
    sparql_wrapper.setReturnFormat(JSON)
    sparql_wrapper.setQuery(query)


    start_time = time.time()

    try:
         # Compute query
        results = sparql_wrapper.query()
        elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds

        with open(RESUME_FILE, 'a') as file:
            file.write(f'{query_number},OK,{elapsed_time}\n')

    except Exception as e:
        elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds
        with open(RESUME_FILE, 'a') as file:
            file.write(f'{query_number},ERROR({type(e).__name__}),{elapsed_time}\n')

        with open(ERROR_FILE, 'a') as file:
            file.write(f'Exception in query {str(query_number)} [{type(e).__name__}]: {str(e)}\n')


with open(RESUME_FILE, 'w') as file:
    file.write('query_number,status,time\n')

with open(ERROR_FILE, 'w') as file:
    file.write('') # to replaces the old error file

for index, item in enumerate(os.listdir(QUERY_ROOT)):
    item_path = os.path.join(QUERY_ROOT, item)
    if os.path.isfile(item_path):
        # Open the file for reading ('r')
        with open(item_path, 'r') as file:
            # Read the content of the file
            content = file.read()
            execute_sparql_wrapper(content, index)
