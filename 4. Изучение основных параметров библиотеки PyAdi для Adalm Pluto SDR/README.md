# Задание

1. При помощи приложения на Android\iOS - **WifiAnalyzer** найти работающие точки доступа на несущей частоте **2.4** [GHz];
2. Определить канал наиболее мощной из них. При помощи **Google** найти несущую частоту в данном канале;
3. Принять радиосигнал на несущей частоте выбранной точки доступа **WiFi**; Показать на графике.
    1. Графики подписать по имеющейся на данный момент информации. 
4. При подозрительной активности радиоканала зафиксировать “снимок” экрана с явными признаками передатчика. Проще говоря, визуально отличить шумы от передачи данных;

# Выполнение
1. Несущая точки доступа определялась по номеру канала в WifiAnalyzer. В исследуемом случае номер канала точки доступа - 6. Через интернет было установлено, что шестому каналу соответсвует несущая примерно 2.437 [GHz]
2. Точка доступа называлась Dron
3. Скришнот: 
![Screenshot](https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Wi-Fi%20signal%20graphic/W3I5O7o5kHo.jpg)

4. В результате выполнения программы были получены графики: 
<details>
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Wi-Fi%20signal%20graphic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-09-28%2001-04-06.png" name="first">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Wi-Fi%20signal%20graphic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-09-28%2001-04-24.png" name="second">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Wi-Fi%20signal%20graphic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-09-28%2001-04-35.png" name="third">
  <img src="https://github.com/TheMightyOoze147/PlutoSDR_practise/blob/main/third_party/Wi-Fi%20signal%20graphic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-09-28%2001-04-42.png" name="fourth">
</details>