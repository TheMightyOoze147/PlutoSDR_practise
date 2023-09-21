import random

# Сгенерировать массив случайных чисел размером 1024 в пределах [-1000:1000].
array = []
for i in range(1024):
    array.append(random.randrange(-1000, 1000))
print(f'Массив случайных чисел: \n{array}')
# Отсортировать данный массив.
array.sort()
print(f'Отсортированный массив: \n{array}')
# Удалить все отрицательные числа.
new_array = []
for i in (array):
    if i >= 0:
        new_array.append(i)
print(f'Массив без отрицательных чисел: \n{new_array}')