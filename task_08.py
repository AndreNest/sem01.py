# 3) Решить следующую задачу, проверки знания таблицы умножения.
# Программа выводит 10 примеров и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три.
# Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
# В итоге выводим количество верных ответов и оценку
import random
def get_number(input_string):
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число.')
        return get_number(input_string)
def exam():
    correctly = 0
    wrong = 0
    evaluation = None
    for i in range(1,11):
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        print(f'Решите пример №{i}: {num_1} x {num_2}')
        answer = get_number('Введите ответ: ')
        if answer == num_1 * num_2:
            correctly +=1
            print('Отлично! Это правильный ответ!')

        elif answer != num_1 * num_2:
            wrong += 1
            print('Ошибка! Ответ не верен!')
    if correctly == 10:
        evaluation = 'пять'
    elif correctly == 9 or correctly == 8:
        evaluation = 'четыре'
    elif correctly < 8:
        evaluation = 'три'

    print(f'Правильных ответов: { correctly}, не првильных {wrong}. Оценка - {evaluation}')


exam()