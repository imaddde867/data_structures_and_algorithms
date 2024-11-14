import sys
sys.path.insert(0, r"C:\Users\vladt\OneDrive - O365 Turun yliopisto\Desktop\project_root")
import time
from data_structures.stack import Stack
from custom_object import CustomObject
import random
import string

def test_stack_performance(data_type, n):
    stack = Stack()
    data = []

    # Generate data based on the data type
    if data_type == 'int':
        data = list(range(n))
    elif data_type == 'string':
        data = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(n)]
    elif data_type == 'custom':
        data = [CustomObject(i) for i in range(n)]
    else:
        raise ValueError("Unsupported data type.")

    # Measure push time
    start_time = time.time()
    for item in data:
        stack.push(item)
    push_time = time.time() - start_time

    # Measure pop time
    start_time = time.time()
    while not stack.is_empty():
        stack.pop()
    pop_time = time.time() - start_time

    print(f"Stack Performance with {n} {data_type} items:")
    print(f"Total push time: {push_time:.4f} seconds")
    print(f"Total pop time: {pop_time:.4f} seconds\n")

if __name__ == "__main__":
    n = 100000  # Number of items
    test_stack_performance('int', n)
    test_stack_performance('string', n)
    test_stack_performance('custom', n)
