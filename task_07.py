# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.

def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)

def multiplication_table(num):
    for i in range(1, 11):
        print(f'{i} x {num} = {num * i}')

multiplication_table(get_number('Введите число: '))