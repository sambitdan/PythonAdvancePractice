# Multithreading - thread based parallelism, is using our processor's threads 
# The threading ,module provides a way to run multiple threads (smaller units of a process) concurrently within a single processor.
#  It allows for creation and management of threads, making it possible to execute tasks in parallel, sharing memory space. 
# Threads are useful when tasks are particularly useful when tasks are I/O bound, such as file operations or making network requests, 
# where much of the time is spent waiting for external resources.
# Threadpool Executor is modern way to use multithreads

"""
Think of a Python program as a restaurant:

Process = a separate restaurant → has its own kitchen, workers, and resources.
Thread = multiple workers inside the same restaurant → they share the same kitchen/resources.
Feature	Multithreading	Multiprocessing
Execution unit	Threads	Processes
Memory	Shared memory	Separate memory
CPU usage	Limited in Python by GIL for CPU-bound code	Can use multiple CPU cores
Best for	I/O-bound tasks	CPU-bound tasks
Creation	Faster/lighter	Heavier
Communication	Easier because memory is shared	More difficult; IPC/queues needed
Crash isolation	Lower	Higher
Example	Downloading 10 files	Processing 10 large datasets
"""

import time

def fetch_data(url:str):

    print (f"fetching data from:{url}")
    time.sleep(5)
    print ("Data Fetched from",url)

    return "Data From " + url

urls_list = [
    "https://example.com/api/data1",
    "https://example.com/api/data2",
    "https://example.com/api/data3",
    "https://example.com/api/data4",
    "https://example.com/api/data5",
]

# Fetching data without multi-threading

# for i in urls_list:
#     fetch_data(i)

# Using multi-threading
results =[]
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    result = executor.map(fetch_data,urls_list)
    results.extend(result)

print(results) # first fetching the data in parallel and then fetched the data in parallel.

# In multi-threading the parameter should be only one if there is multiple parameterwe first create a dict then fetch the keys