# 2. Дискретизация сигналов. Вычисление ДПФ
Аналоговый сигнал x(t)=Acos(ωt) при дискретизации с интервалом времени T_s преобразуется в последовательность дискретных значений (чисел) x(n)=Acos(ωnT_s)=Acos(Ωn)
Часть 1.
1. Задайте сигнал с частотой f, Гц, выберите частоту дискретизации fs отсч/сек. Получите набор отсчетов сигнала размером 64, 128, 256, изобразите выборку отсчетов командой plt.stem
2. Определите значение аналоговой частоты сигнала, которая соответствует нормированной частоте Ω=0.1π рад, Ω=0.3π при fs первого раздела
3. При помощи функции fft модуля numpy вычислите ДПФ сигнала из раздела 1 для трех наборов отсчетов. Изобразите модуль спектра ДПФ с указанием частотной оси в Гц.

Часть 2. 
Основы цифровой фильтрации
Сформируй те сигнал, состоящий из суммы двух гармонических колебаний (косинусов) разных частот. Выберите частоту дискретизации для данного сигнала. Изобразите спектр ДПФ полученных отсчетов.
Рассчитайте отсчеты цифрового фильтра ФНЧ с частотой среза для подавления сигнала с большей частотой. Импульсная характеристика ФНЧ вычисляется по выражению h(n)=  (sin⁡(Ω_cn))/πn, Ω_c – нормированная частота среза. Примените полученную импульсную характеристику фильтра к входному сигналу.
Изобразите спектр ДПФ сигнала после фильтрации

# Выполнение
Задание 2.
Часть 1.
Задан сигнал с частотой fc = 50 [Hz]

```python
fc = 50
w = 2 * np.pi * fc
t = np.arange(0, 1, 0.001)
A = 2
x_t = A * np.cos(w * t)
```

<img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%B8%D0%BF%D0%B5%D0%BD%D0%B4%D0%B8%D1%8E/pics/Figure%202023-11-08%20232944%20(1).png" width="512"/>
И продискретизирован с частотой дискретизации fs = 200 [Hz] для трёх наборов отсчётов размерами 64, 128 и 256

```python
fs = 200
Ts = 1/fs
n64 = np.arange(0, 64, 1)
n128 = np.arange(0, 128, 1)
n256 = np.arange(0, 256, 1)
x_d64 = A * np.cos(w * n64 * Ts)
x_d128 = A * np.cos(w * n128 * Ts)
x_d256 = A * np.cos(w * n256 * Ts)
```

<img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%B8%D0%BF%D0%B5%D0%BD%D0%B4%D0%B8%D1%8E/pics/Figure%202023-11-08%20232944%20(2).png" width="512"/>

Так же были найдены аналоговые частоты, которые соотвествтуют нормированным частотам Ω = 0.1π и Ω = 0.3π

```python
Calculated_fs_01Pi = (0.1 * np.pi * fs)/(2 * np.pi)
Calculated_fs_03Pi = (0.3 * np.pi * fs)/(2 * np.pi)
```

Это частоты fc = 10.0 и fc = 29.9 соответственно
Наконец, были найдены спектры для данных сигналов с разным количеством отсчётов

```python
spectre64 = abs(np.fft.fft(x_d64))
spectre128 = abs(np.fft.fft(x_d128))
spectre256 = abs(np.fft.fft(x_d256))
fspec64 = np.arange(-len(spectre64)/2, len(spectre64)/2, 1) * fs/64
fspec128 = np.arange(-len(spectre128)/2, len(spectre128)/2, 1) * fs/128
fspec256 = np.arange(-len(spectre256)/2, len(spectre256)/2, 1) * fs/256
```

<img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%B8%D0%BF%D0%B5%D0%BD%D0%B4%D0%B8%D1%8E/pics/Figure%202023-11-08%20232944%20(0).png" width="512"/>

Часть 2.

Был задан сигнал, состоящий из двух гармонических колебаний с частотами f1 = 5 [Hz] и f2 = 20 [Hz]

```python
t = np.arange(0, 1, 1/fs)
signal_sum = np.cos(2 * np.pi * 5 * t) + np.cos(2 * np.pi * 20 * t)
```

<img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%B8%D0%BF%D0%B5%D0%BD%D0%B4%D0%B8%D1%8E/pics/Figure%202023-11-08%20234704.png" width="512"/>
И фильтр

```python
fc = 5/fs #Нормированная частота среза
N = 50 #Длина фильтра
n = np.arange(0, N)
h = np.sinc(2 * fc * (n - (N - 1) / 2))  #Импульсная характеристика ФНЧ
```

После чего рассчитаны спектры исходного сигнала и отфильтрованного

```python
sum_spectre = np.fft.fft(signal_sum)
freqs_sum = np.fft.fftfreq(len(sum_spectre), 1/fs)

filtered_signal = np.convolve(signal_sum, h, mode='same')
filtered_spectre = np.fft.fft(filtered_signal)
freqs_filt = np.fft.fftfreq(len(filtered_spectre), 1/fs)
```

<img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%B8%D0%BF%D0%B5%D0%BD%D0%B4%D0%B8%D1%8E/pics/Figure%202023-11-08%20232944%20(3).png" width="512"/>
