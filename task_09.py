import song
# # 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# # Ставим таймер - часы, минуты, секунды.
# # После отсчета срабатывает будильник
# import time
# def total_time_and_message():
#     time_hours = int(input('In how many hours? '))
#     time_min = int(input('In how many minutes? '))
#     time_sec = int(input('In how meny seconds? '))
#     sum_time = time_sec + (time_min * 60) + (time_hours * 60 * 60)
#     return sum_time
#
# def timer(massage, times):  #3621
#     while times > 0:
#         print(f'Осталось {times // 3600} часов, {(times - (times // 3600)* 3600) // 60} минут, {times % 60} секунд')
#         times -= 1
#         time.sleep(1)
#     print(massage)
#
#
# # def timer(text, times):
# #     hours = times // 3600
# #     min = times // 60
# #     while times > 0:
# #         if times > 3600:
# #             count_min = 60
# #             hours -= 1
# #             while count_min > 0:
# #                 count_sec = 60
# #                 count_min -= 1
# #                 while count_sec > 0:
# #                     count_sec -=1
# #                     print(f'Осталось {hours} - часов, {count_min} - минут, {count_sec} - секунд!')
# #                     time.sleep(1)
# #                     times -= 1
# #         elif times > 60 and times < 3600:
# #                 count_sec = 60
# #                 min -= 1
# #                 while count_sec > 0:
# #                     count_sec -= 1
# #                     print(f'Осталось {hours} - часов, {min} - минут, {count_sec} - секунд!')
# #                     time.sleep(1)
# #                     times -= 1
# #
# #
# #         elif times < 60:
# #             while times > 0:
# #                 times -= 1
# #                 print(f'Осталось {hours} - часов, {min} - минут, {times} - секунд!')
# #                 time.sleep(1)
# #     print(text)
# #
#
# timer('privet',total_time_and_message())
#
#
#
#
#
#
#
#         # if times < 60:
#         #     print(f'{times} - seconds, {times // 60} - minutes, {times // (60 * 60)} - hours left!')
#         #     time.sleep(1)
#         #     times -= 1
#         #
#         # elif times < 3600:
#         #     print(f'{times} - seconds, {times // 60} - minutes, {times // (60*60)} - hours left!')
#         #     time.sleep(1)
#         #     times -= 1
#         # elif times > 3600:
#         #     print(f'{times // 3600 } - seconds, {times // 60} - minutes, {times // (60 * 60)} - hours left!')
#         #     time.sleep(1)
#         #     times -= 1
#
#
import time
import click

event = input('Задайте напоминание: \n')
print()

print('Задайте время, через которое должно сработать напоминание!')
hours = int(input('Часов: '))
minutes = int(input('Минут: '))
seconds = int(input('Секунд: ')) + minutes * 60 + hours * 3600
click.clear()

for value in range(seconds, 0, -1):
    hour = value // 3600
    minute = (value % 3600) // 60
    second = value - hour * 3600 - minute * 60
    print("Таймер запущен!\n")
    print('{}:{}:{}'.format(hour, minute, second))
    time.sleep(1)
    click.clear()
else: print(event)