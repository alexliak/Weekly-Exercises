from time import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Define the function to find even numbers in a list
def find_even_number(data):
    counter = 0
    for value in data:
        if value % 2 == 0:
            counter += 1
    return counter

# Sizes of data to test
values = [10000, 100000, 1000000, 10000000]
execution_times = []

# Measure execution time for each data size
for v in values:
    data = [random.randint(1, 1000) for _ in range(v)]
    start_time = time()
    find_even_number(data)  # Call the function but we don't need its return value here
    end_time = time()
    execution_times.append(end_time - start_time)

# Plotting with Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=values, y=execution_times, marker='o', color='b', label='Execution Time')

# Setting the scale of x and y axes to logarithmic to handle the wide range of values
plt.xscale('log')
plt.yscale('log')
plt.title('Execution Time of find_even_number Function')
plt.xlabel('Number of Elements in List')
plt.ylabel('Execution Time (seconds)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
