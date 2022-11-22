# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#
# *Примеры:*
#
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

def get_number(input_string):
    try:
        num = float(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число число.')
        return get_number(input_string)

def corent_10(num):
    while num > 10:
        num /  10
    return num
def corent_num(num):
    if (num * 10) % 10 == 0:
        print(f'У числа {num} нет дробной части!')


corent_num(corent_10(get_number('dd')))