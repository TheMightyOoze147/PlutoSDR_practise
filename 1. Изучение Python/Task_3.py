import matplotlib.pyplot as plt
import numpy as np

A = 1
w = 2*np.pi
f = 10/1000

t = np.arange(0, 1000, 1)  # создание массива от 0 до 10 с 10000
y_sin = A * np.sin(w*f*t)  # создание массива значений по синусоидальному закону
y_cos = A * np.cos(w*f*t)
# вывод значений массива на график
plt.plot(t, y_sin)  
plt.plot(t, y_cos)
plt.title('A * sin(w*f*t) - Blue\nA * cos(w*f*t) - Orange')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.show()