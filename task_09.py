# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник
import time
text = str(input('О чем вам напомнить? '))
local_time_hours = int(input('Через сколько часов?'))
local_time_min = int(input('Через сколько минут?'))
local_time_sec = int(input('Через сколько секунд?'))
local_time_total = (local_time_hours * 60 * 60) + (local_time_min * 60) + local_time_sec
def timer(time):
    while time > 0:
        hour = 0
        min = 0
        sec = 0
        if time > 60 * 60:
            hour = time // 3600
            time = time % 3600
        if time > 60:
            min = time // 60
            time = time % 60
        if time > 0:
            print(f'осталось {time}  секунд!!!!')
            time.sleep(1)
            time -= 1
    print(text)

timer(local_time_total)