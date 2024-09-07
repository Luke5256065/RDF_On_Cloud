from SPARQLWrapper import SPARQLWrapper, JSON
import multiprocessing
import sys
import time


BENCHMARK_ROOT='/home/ubuntu'
PREFIX_NAME = 'VIRTUOSO'
ENGINE='Virtusos'
LIMIT = None
QUERIES_FILE = sys.argv[1]
TIMEOUT = 60

RESUME_FILE = f'{BENCHMARK_ROOT}/results/{PREFIX_NAME}_{ENGINE}_limit_{LIMIT}.csv'
ERROR_FILE  = f'{BENCHMARK_ROOT}/results/errors/{PREFIX_NAME}_{ENGINE}_limit_{LIMIT}.log'

SERVER_LOG_FILE  = f'{BENCHMARK_ROOT}/scripts/log/{PREFIX_NAME}_{ENGINE}_limit_{LIMIT}.log'

VIRTUOSO_LOCK_FILE = f'{BENCHMARK_ROOT}/virtuoso/wikidata/virtuoso.lck'

def parse_to_sparql(query):
    if not LIMIT:
        return f'SELECT * WHERE {{ {query} }}'
    return f'SELECT * WHERE {{ {query} }} LIMIT {LIMIT}'

def execute_queries():
    with open(QUERIES_FILE) as queries_file:
        i = 0
        for line in queries_file:
            print(f'Executing query {line}')
            query_sparql(line, i)
            i +=1


def execute_sparql_wrapper(query_pattern, query_number):
    query = parse_to_sparql(query_pattern)

    sparql_wrapper = SPARQLWrapper('http://localhost:8890/sparql')
    # sparql_wrapper.setTimeout(TIMEOUT+10) # Give 10 more seconds for a chance to graceful timeout
    sparql_wrapper.setReturnFormat(JSON)
    sparql_wrapper.setQuery(query)

    count = 0
    start_time = time.time()

    try:
        # Compute query
        results = sparql_wrapper.query()
        json_results = results.convert()
        for _ in json_results["results"]["bindings"]:
            count += 1

        elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds

        with open(RESUME_FILE, 'a') as file:
            file.write(f'{query_number},{count},OK,{elapsed_time}\n')

    except Exception as e:
        elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds
        with open(RESUME_FILE, 'a') as file:
            file.write(f'{query_number},,ERROR({type(e).__name__}),{elapsed_time}\n')

        with open(ERROR_FILE, 'a') as file:
            file.write(f'Exception in query {str(query_number)} [{type(e).__name__}]: {str(e)}\n')


def query_sparql(query_pattern, query_number):
    start_time = time.time()

    try:
        p = multiprocessing.Process(target=execute_sparql_wrapper, args=[query_pattern, query_number])
        p.start()
        # Give 2 more seconds for a chance to graceful timeout or enumerate the results
        p.join(TIMEOUT + 2)
        if p.is_alive():
            p.kill()
            p.join()
            raise Exception("PROCESS_TIMEOUT")

    except Exception as e:
        elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds
        with open(RESUME_FILE, 'a') as file:
            file.write(f'{query_number},,TIMEOUT({type(e).__name__}),{elapsed_time}\n')

        with open(ERROR_FILE, 'a') as file:
            file.write(f'Exception in query {str(query_number)} [{type(e).__name__}]: {str(e)}\n')
            sys.exit(0)


with open(RESUME_FILE, 'w') as file:
    file.write('query_number,results,status,time\n')

with open(ERROR_FILE, 'w') as file:
    file.write('') # to replaces the old error file

print('benchmark is starting. TIMEOUT', TIMEOUT, 'seconds')
execute_queries()
