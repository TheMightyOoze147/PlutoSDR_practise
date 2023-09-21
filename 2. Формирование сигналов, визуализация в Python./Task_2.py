import math
import numpy as np
import matplotlib.pyplot as plt

A = 1 #Амплитуда
w = 2*np.pi #Коэффициент
f = 0.1 #Частота

t = np.arange(0, 25, 0.25)  # создание массива от 0 до 10 с 10000
y_sin = A * np.sin(w*f*t)  # создание массива значений по синусоидальному закону

plt.plot(t, y_sin)  
plt.title('Аналоговый')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()

plt.stem(t, y_sin)
plt.title('Дискретный')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()

plt.step(t, y_sin)
plt.title('Квантованный')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(t, y_sin)  
ax1.set_title('Аналоговый')
ax1.set_xlabel('Время')
ax1.set_ylabel('Амплитуда')
ax1.grid()


ax2 = fig.add_subplot(3, 1, 2)
ax2.stem(t, y_sin)
ax2.set_title('Дискретный')
ax2.set_xlabel('Время')
ax2.set_ylabel('Амплитуда')
ax2.grid()


ax3 = fig.add_subplot(3, 1, 3)
ax3.step(t, y_sin)
ax3.set_title('Квантованный')
ax3.set_xlabel('Время')
ax3.set_ylabel('Амплитуда')
ax3.grid()

plt.show()