# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник
import time
text = str(input('О чем вам напомнить? '))
local_time_hours = float(input('Через сколько часов?'))
local_time_min = float(input('Через сколько минут?'))
local_time_sec = float(input('Через сколько секунд?'))
local_time_total = (local_time_hours * 60 * 60) + (local_time_min * 60) + local_time_sec
time.sleep(local_time_total)
print(text)