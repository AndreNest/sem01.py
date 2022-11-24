# 5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)
def num( a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if(( a % i == 0) and(b % i == 0 )):
            total = i
    return print(f'НОД = {total}')
num(get_number('Введите первое число: '), get_number('Введите второе число: '))


