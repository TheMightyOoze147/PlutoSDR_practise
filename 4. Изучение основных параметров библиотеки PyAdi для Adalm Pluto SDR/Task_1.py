import adi
import matplotlib.pyplot as plt
import time

sdr = adi.Pluto("ip:192.168.2.1")
sdr.rx_lo = 2437000000 #Шестой канал Wi-Fi - 2.437 [GHz]

for r in range(30):
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.xlabel("Время")
    plt.ylabel("Амплитуда")
    plt.legend(("Real", "Imaginary"), loc='upper left')
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)
    
plt.show()