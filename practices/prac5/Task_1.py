from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt


fc0 = 10 # Частота косинуса
fc1 = 140
fs=320 # частота дискретизации, избыточная 
t=np.arange( 0, 0.2,  1/fs) # длительность сигнала 0.2 с
x=np.cos(2*np.pi*fc0*t) + np.cos(2*np.pi*fc1*t) # формирование временного сигнала
plt.figure(1)
plt.plot(t,x) 
#plt.stem(t,x) # для отображения временных отсчетов сигнала, выбрать длительность 0.2 сек
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$') 
N=256 # количество точек ДПФ
X = fft(x,N)/N # вычисление ДПФ и нормирование на N

plt.figure(2)
k = np.arange(0, N)
plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
plt.xlabel('k')
plt.ylabel('$x[k]$') 
plt.savefig("Сумма сигналов.jpg")

df=fs/N
kf = k*df
plt.figure(3)
plt.stem(kf,abs(X)) # выводим модуль ДПФ в частотах 
plt.xlabel('Гц')
plt.ylabel('$x[k]$') 
plt.savefig("Модуль ДПФ.jpg")

k2 = np.arange(-N/2, N/2)
kf2=k2*df
X2 = fftshift(X) # сдвиг ДПФ на центр 
plt.figure(4)
plt.stem(kf2,abs(X2))
plt.xlabel('Гц')
plt.ylabel('$x[k]$') 
plt.savefig("ДПФ.jpg")


plt.figure(5)
#X=np.array([0,0,1])
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
plt.xlabel('c')
plt.ylabel('$x[n]$') 
plt.savefig("ОДПФ.jpg")


plt.figure(6)
X=np.array([0,0,1])
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
plt.xlabel('c')
plt.ylabel('$x[n]$') 
plt.savefig("ОДПФ task 6.jpg")


plt.figure(7)
X=np.array([0,0,1j,0,0,0,0,0])
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
plt.xlabel('c')
plt.ylabel('$x[n]$') 
plt.savefig("ОДПФ для комплексного числа.jpg")

plt.figure(7)
X=np.array([0,0,2-1j,0,0,0,0,0]) 
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
plt.xlabel('c')
plt.ylabel('$x[n]$') 
plt.savefig("ОДПФ для комплексного числа_2.jpg")