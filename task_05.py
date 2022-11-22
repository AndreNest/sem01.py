# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)

def set_num(x):
    if x % 5 == 0 or x % 10 or x % 15:
        if x % 30 != 0:
            print('Число подходит под условия задача!')
        else:
            print('число не подходит под условия!')

set_num(get_number('Введите число: '))