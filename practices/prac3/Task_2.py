 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack

Ts = 2e-3
fs = 1/Ts

t = np.arange(-5, 11)*Ts
"""
По теореме Котельникова, максимальная аналоговая частота 250 [Hz], 
однако в цикле 300, всё потому, что цикл for 
не включает последнее значение в шаг
"""
for fr in range(50, 300, 50): 
    plt.figure(fr) 
    s =  np.cos(fr*t*(2*np.pi))
    sp = fftpack.fft(s)
    freqs=np.arange(0,fs,fs/len(s))
    plt.title(f'Частота {fr} [Hz]')
    plt.stem(freqs, np.abs(sp))
    plt.xlabel('Частота в герцах [Hz]')
    plt.ylabel('Модуль спектра')
    plt.grid()