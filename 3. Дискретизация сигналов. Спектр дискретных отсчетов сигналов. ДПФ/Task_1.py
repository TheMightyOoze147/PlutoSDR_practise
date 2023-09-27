 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack
 
plt.figure()
Ts4 = 1e-3 #Задание частоты дискретизации 1000 отсчётов/сек
fs4 = 1/Ts4
an_freq = ((0.4 * np.pi * fs4)/(2 * np.pi)) #Рассчёт аналоговой частоты
t = np.arange(-5, 11)*Ts4
s =  np.cos(100*t*(2*np.pi))
plt.subplot(3, 1, 1)
plt.plot(t, s)
plt.title("График при частоте дискретизации 1000 отсчётов/сек")
plt.subplot(3, 1, 2)
plt.stem(t, s)
plt.show()

s = np.cos(an_freq*t*(2*np.pi))
sp = fftpack.fft(s)
freqs=np.arange(0,fs4,fs4/len(s))

plt.stem(freqs, np.abs(sp))
plt.xlabel('Частота в герцах [Hz]')
plt.ylabel('Модуль спектра')
plt.title(f'Спектр сигнала при аналоговой частоте {an_freq:.0f} [Hz] для нормированной частоты 0.4pi рад')
plt.grid()