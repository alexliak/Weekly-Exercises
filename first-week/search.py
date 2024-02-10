from time import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

list_sizes = [100, 200, 400, 800, 1600]

for size in list_sizes:
    data = generate_list(size)
    start_time = time()
    bubble_sort(data)
    end_time = time()
    print(f"Size: {size}, Time: {end_time - start_time:.5f} seconds")
