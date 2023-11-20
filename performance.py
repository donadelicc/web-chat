import logging
import time
from datetime import datetime

logging.basicConfig(filename='request_logs.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def timeit(method):
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        logging.info(f"{method.__name__} - Execution time: {(end_time - start_time):.2f} seconds")
        return result
    return timed

## ----- EKSPMEL PÅ BRUK AV "timeit" -----

@timeit
def load_vector_store(file_path):
    # Last inn VectorStore her
    pass

@timeit
def handle_request(query):
    # Behandle forespørselen her
    pass

## ---------------------------------------

def log_request(query):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Time: {timestamp}, Query: {query}")


def analyse_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    # Eksempel på hvordan du kan analysere loggene
    # Her kan du bruke mer avansert logikk for å trekke ut innsikt

    for log in logs:
        print(log)

analyse_logs('request_logs.log')
