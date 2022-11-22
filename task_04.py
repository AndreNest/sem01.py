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
total = get_number('Введите число: ')
print(int(total * 10 % 10))