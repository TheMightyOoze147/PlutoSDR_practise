# Задания

1. Задайте частоту дискретизации 1000 отсчетов/c.  Определите значение аналоговой частоты сигнала, которая соответствует нормированной частоте  рад. Приведите временные диаграммы 

2. Задавайте различные частоты сигналов при частоте дискретизации 500 отсчетов/с и наблюдайте форму спектров отсчетов.  При выборе частот сигналов используйте теорему Котельникова. Для корректного вычисления спектра функциями fft задавайте количество  отсчетов сигнала порядка 200 в команде arrange.

# О работе
В ходе первого задания необходимо было вывести график для частоты дискретизации равной 1000 отсчётов/сек, а так же с той же частотой дискретизации найти аналоговую частоту, при которой нормарованная частота равняется 0.4pi радиан
Аналоговая частота оказалась равна 200 [Hz]

В ходе второго задания необходимо было вывести графики спектров сигналов с различными частотами при частоте дискретизации 500 отсчётов/сек. При такой частоте дискретизации по теореме Котельникова максимальная аналоговая частота равна 500/2 = 250 [Hz], соответственно был выбран диапазон частот от 50 до 250 с шагом в 50
# Полученные графики:

## Первая задача
<details>
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_1/Freq%20200.0%20%5BHz%5D%20--%20fixed.png" name="200hz">
</details>

## Вторая задача
<details>
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_2/Freq%2050%20%5BHz%5D.png" name="50hz">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_2/Freq%20100%20%5BHz%5D.png" name="100hz">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_2/Freq%20150%20%5BHz%5D.png" name="150hz">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_2/Freq%20200%20%5BHz%5D.png" name="200hz">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Spectre_Task_2/Freq%20250%20%5BHz%5D.png" name="250hz">
</details>