import adi
import matplotlib.pyplot as plt
from scipy.fftpack import ifft
import numpy as np
import time

sdr = adi.Pluto("ip:192.168.2.1")
sdr.rx_lo = 2412000000 #Шестой канал Wi-Fi - 2.437 [GHz]
for i in range(50):
    rx = sdr.rx()

    N = 256
    X = ifft(rx, N)/N

    plt.figure()
    k = np.arange(0, N)
    plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
    plt.xlabel('k')
    plt.ylabel('$x[k]$') 
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)
    plt.savefig(f'Sceptre-{i}.png')










