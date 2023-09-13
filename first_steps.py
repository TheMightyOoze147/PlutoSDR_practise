import numpy as np

def diag_swap(array):
    #Функция смены чисел на диагоналях
    main_diag = np.diag(array) #Создается массив, состоящий из чисел на диагонали
    reversed_arr = np.fliplr(array) #Отзеркаливание матрицы для нахождения побочной диагонали
    side_diag = np.diag(reversed_arr)
    #Разрешение на редактирование массива с диагональю
    main_diag.flags.writeable = True
    side_diag.flags.writeable = True
    #Смена чисел по диагоналям
    for i in range (len(main_diag)):
        buff = main_diag[i]
        main_diag[i] = side_diag[len(side_diag) - i - 1]
        side_diag[len(side_diag) - i - 1] = buff
    

def main():
    x = int (input ("Введите количество строк: "))
    j = int (input ("Введите количество столбцов: "))
    #Создание матрицы
    arr = np.random.randint(100, size=(x, j))
    print("\nМатрица до изменений: \n", arr)
    diag_swap(arr)
    print("\nМатрица после изменений: \n", arr)

if __name__ == "__main__":
    main()