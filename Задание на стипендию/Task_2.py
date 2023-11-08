import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Построение аналогового сигнала с частотой fc = 50 [Hz]
fc = 50
w = 2 * np.pi * fc
t = np.arange(0, 1, 0.001)
A = 2
x_t = A * np.cos(w * t)

#Дискретизация сигнала с частотой дискретизации fs = 200 [Hz] 
#и наборами отсчётов n = 64, 128, 256
fs = 200
Ts = 1/fs
n64 = np.arange(0, 64, 1)
n128 = np.arange(0, 128, 1)
n256 = np.arange(0, 256, 1)
x_d64 = A * np.cos(w * n64 * Ts)
x_d128 = A * np.cos(w * n128 * Ts)
x_d256 = A * np.cos(w * n256 * Ts)

#Рассчёт значения аналоговой частоты, которая соответствует нормированной
#частоте Ω = 0.1Pi рад, Ω = 0.3Pi рад
Calculated_fs_01Pi = (0.1 * np.pi * fs)/(2 * np.pi)
Calculated_fs_03Pi = (0.3 * np.pi * fs)/(2 * np.pi)

#Построение модуля спектра для дискретных сигналов с 
#n = 64, 128, 256
spectre64 = abs(np.fft.fft(x_d64))
spectre128 = abs(np.fft.fft(x_d128))
spectre256 = abs(np.fft.fft(x_d256))

fspec64 = np.arange(-len(spectre64)/2, len(spectre64)/2, 1) * fs/64
fspec128 = np.arange(-len(spectre128)/2, len(spectre128)/2, 1) * fs/128
fspec256 = np.arange(-len(spectre256)/2, len(spectre256)/2, 1) * fs/256

plt.figure(0, figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.stem(fspec64, spectre64)
plt.title('Колчиество отсчётов n = 64')
plt.xlabel('Частота [Гц]')
plt.subplot(1, 3, 2)
plt.stem(fspec128, spectre128)
plt.title('Колчиество отсчётов n = 128')
plt.xlabel('Частота [Гц]')
plt.subplot(1, 3, 3)
plt.xlabel('Частота [Гц]')
plt.title('Колчиество отсчётов n = 256')
plt.stem(fspec256, spectre256)

print(Calculated_fs_01Pi, Calculated_fs_03Pi)
#Вывод графиков на экран
plt.figure(1, figsize=(12, 6))
plt.xlabel('Время [c]')
plt.title('Исходный сигнал\nx(t) = A * cos(w * t)')
plt.plot(t, x_t)
fig = plt.figure(2, figsize=(12, 6))
fig.suptitle('Дискретизированный сигнал\nx(n) = A * cos(w * n * Ts)')
plt.subplot(1, 3, 1)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 64')
plt.stem(n64, x_d64)
plt.subplot(1, 3, 2)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 128')
plt.stem(n128, x_d128)
plt.subplot(1, 3, 3)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 256')
plt.stem(n256, x_d256)

fs = 256
t = np.arange(0, 1, 1/fs)
signal_sum = np.cos(2 * np.pi * 5 * t) + np.cos(2 * np.pi * 20 * t)
plt.figure(4)
plt.plot(t, signal_sum)
fc = 5/fs #Нормированная частота среза
N = 50 #Длина фильтра
n = np.arange(0, N)
h = np.sinc(2 * fc * (n - (N - 1) / 2))  #Импульсная характеристика ФНЧ
sum_spectre = np.fft.fft(signal_sum)
freqs_sum = np.fft.fftfreq(len(sum_spectre), 1/fs)

filtered_signal = np.convolve(signal_sum, h, mode='same')
filtered_spectre = np.fft.fft(filtered_signal)
freqs_filt = np.fft.fftfreq(len(filtered_spectre), 1/fs)

plt.figure(3)
plt.subplot(1, 2, 1)
plt.title('Исходный сигнал')
plt.stem(freqs_sum, abs(sum_spectre))
plt.xlim(-25, 25)

plt.subplot(1, 2, 2)
plt.title('Отфильтрованный сигнал')
plt.stem(freqs_filt, abs(filtered_spectre))
plt.xlim(-25, 25)
