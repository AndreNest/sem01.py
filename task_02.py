# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
import sys


def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)

def max_num(x):
    max_numb = -sys.maxsize
    for i in range(x):
        num = int(get_number('Введите число: '))
        if num > max_numb:
            max_numb = num
    print(f'Максимальное число = {max_numb}')

max_num(get_number('сколько чисел будет введено? '))