import sys
sys.path.insert(0, r"C:\Users\vladt\OneDrive - O365 Turun yliopisto\Desktop\project_root")
import time
from data_structures.queue import Queue
from custom_object import CustomObject
import random
import string

def test_queue_performance(data_type, n):
    queue = Queue()
    data = []

    # Generates data based on the data type
    if data_type == 'int':
        data = list(range(n))
    elif data_type == 'string':
        data = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(n)]
    elif data_type == 'custom':
        data = [CustomObject(i) for i in range(n)]
    else:
        raise ValueError("Unsupported data type.")

    # Measures enqueue time (going in)
    start_time = time.time()
    for item in data:
        queue.enqueue(item)
    enqueue_time = time.time() - start_time

    # Measures dequeue time (coming out)
    start_time = time.time()
    while not queue.is_empty():
        queue.dequeue()
    dequeue_time = time.time() - start_time

    print(f"Queue Performance with {n} {data_type} items:")
    print(f"Total enqueue time: {enqueue_time:.4f} seconds")
    print(f"Total dequeue time: {dequeue_time:.4f} seconds\n")

if __name__ == "__main__":
    n = 100000  # Number of items in use
    test_queue_performance('int', n)
    test_queue_performance('string', n)
    test_queue_performance('custom', n)
