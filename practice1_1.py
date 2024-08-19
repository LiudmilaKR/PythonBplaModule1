altitude = 0 # Высота в метрах
speed = 0 # Скорость в метрах в секунду
weight = 1.5 # Вес БПЛА в килограммах
# fuel = 100 # Топливо в процентах

# тангаж - один из углов летательного аппарата относительно абциссы (горизонтали)
pitch = 0 # Тангаж в градусах
roll = 0 # Крен в градусах
yaw = 0 # Рысканье в градусах

battery_capacity = 100 # Ёмкось батареи в процентах
# Против часовой стрелки (CCW)
# По часовой стрелке (CW)
# (1)       (2)
#  CCW      CW
#   \        /
#    \      /
#     ------
#    /      \
#   /        \
#  CW       CCW
# (3)       (4)
propeller_speed1 = 0 # Скорость вращения 1-ого пропеллера в об\мин
propeller_speed2 = 0 # Скорость вращения 2-ого пропеллера в об\мин
propeller_speed3 = 0 # Скорость вращения 3-ого пропеллера в об\мин
propeller_speed4 = 0 # Скорость вращения 4-ого пропеллера в об\мин

direction = 0 # Направление в градусах (по сути - азимут для БПЛА)
payload = 500 # Грузоподъёмность в граммах

is_flying = False # Летит ли БПЛА
is_connected = False # Подключен ли БПЛА (связь с БПЛА)