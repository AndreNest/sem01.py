# 1) Решить следующую задачу: генерируем среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры.
# После того, как введем последнее число - программа выводит среднее арифметическое, максимальное и минимальное значение.
# (не пользуемся списками и встроенными функциями) Количество чисел задаётся в начале работы программы
import sys


def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)
def get_number_float(input_string):
    try:
        num = float(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)
def arithmetic_mean(num):
    sum = 0
    min = sys.maxsize
    max = -sys.maxsize
    for i in range(num):
        input_num = get_number_float('Введите вещественное число: ')
        sum = sum + input_num
        if input_num < min:
            min = input_num
        if input_num > max:
            max = input_num

    sred = sum/num
    print(f'Максимально число: {max}, минимальное число: {min}, среднее арифмитичекое: {sred}')



arithmetic_mean(get_number('Сколько чисел мы будем вваодить? '))
