
import sys
import GstoreConnector
import time
import multiprocessing
import sys
import time
# before you run this example, make sure that you have started up ghttp service (using bin/ghttp port)
IP = "127.0.0.1"
Port = 9000
httpType = "ghttp"
username = "root"
password = "123456"
filename = "res.txt"
BENCHMARK_ROOT='/home/ubuntu'
PREFIX_NAME = 'GSTORE'
ENGINE='gstore'
LIMIT = None
QUERIES_FILE = sys.argv[1]
TIMEOUT = 60

RESUME_FILE = f'{BENCHMARK_ROOT}/results/{PREFIX_NAME}_{ENGINE}_limit_{LIMIT}.csv'
# start a gc with given IP, Port, username and password
gc =  GstoreConnector.GstoreConnector(IP, Port, username, password, http_type=httpType)


def execute_queries():
    with open(QUERIES_FILE) as queries_file:
        i = 0
        for line in queries_file:
            print(f'Executing query {line}')
            query_sparql(line, i)
            i +=1

def execute_sparql_wrapper(query_pattern, query_number):
    count = 0
    start_time = time.time()
    gc.query("lubm", "json", query_pattern, "POST")
    elapsed_time = int((time.time() - start_time) * 1000) # Truncate to milliseconds
    with open(RESUME_FILE, 'a') as file:
        file.write(f'{query_number},{count},OK,{elapsed_time}\n')

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



with open(RESUME_FILE, 'w') as file:
    file.write('query_number,results,status,time\n')

print('benchmark is starting. TIMEOUT', TIMEOUT, 'seconds')
execute_queries()
