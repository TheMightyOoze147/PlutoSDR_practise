import numpy as np
import matplotlib.pyplot as plt
import time
import random

rng = np.random.default_rng()
py_list_timings = []
np_array_timings = []
size_of_arrays = []
for i in range(10, 5000000, 100000):
    rng = np.random.default_rng()
    py_list = []
    for x in range(0, i):
        n = random.randint(-500, 500)
        py_list.append(n)

    py_list_start = time.time()
    py_list.sort()
    py_list_end = time.time()
    py_list_result = py_list_end - py_list_start
    py_list_timings.append(py_list_result)
    
    np_array = rng.integers(low=-500, high=500, size=i)
    np_array_start = time.time()
    np.sort(np_array)
    np_array_end = time.time()
    np_array_result = np_array_end - np_array_start
    np_array_timings.append(np_array_result)
    size_of_arrays.append(len(py_list))

plt.plot(size_of_arrays, py_list_timings, label = 'Python list')
plt.plot(size_of_arrays, np_array_timings, label = 'NumPy array')
plt.title('Скорость встроенной сортировки и сортировки NumPy')
plt.ylabel('Время')
plt.xlabel('Количество элементов')
plt.grid()
plt.legend()
plt.show()