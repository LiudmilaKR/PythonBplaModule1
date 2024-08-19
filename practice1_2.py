import random

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
# propeller_speed1 = 0 # Скорость вращения 1-ого пропеллера в об\мин
# propeller_speed2 = 0 # Скорость вращения 2-ого пропеллера в об\мин
# propeller_speed3 = 0 # Скорость вращения 3-ого пропеллера в об\мин
# propeller_speed4 = 0 # Скорость вращения 4-ого пропеллера в об\мин

propellers_speed = [0, 0, 0, 0] # Скорости вращения пропеллеров в об\мин

direction = 0 # Направление в градусах (по сути - азимут для БПЛА)
payload = 500 # Грузоподъёмность в граммах

is_flying = False # Летит ли БПЛА
is_connected = False # Подключен ли БПЛА (связь с БПЛА)
# армирование двигателя - подготовка двигателя к работе (проверка безопасности, того, что двигатель готов к работе, 
# предотвращает случайное включение двгителя)
is_armed = False # Арминг (состояние) двигателя
# телеметрия - наши все показали: высота, скорости и пр., передается всегда с помощью словаря

info = f"""
--------Квадрокоптер---------
Высота: {altitude} м, Скорость: {speed} м/сек.
Вес БПЛА: {weight} кг, Грузоподъемность: {speed} грамм
Тангаж: {pitch} градусов, Крен: {roll} градусов, Рысканье: {yaw} градусов
Скорость вращения пропеллеров: {propellers_speed}
({propellers_speed[0]})       ({propellers_speed[1]})
 CCW      CW
  \\        /
   \\      /
    ------
   /      \\
  /        \\
 CW       CCW
({propellers_speed[2]})       ({propellers_speed[3]})
"""
# print(info)
# print(f'Высота: {altitude}, Скорость: {speed}')

# Функция подключения к дрону
def drone_connect():
    global is_connected
    print('Подключение к БПЛА...')
    is_connected = True
    print('Подключение установлено')

# Функция проверки дрона (после подключения к нему)
def arm_drone():
    global is_armed, propellers_speed
    if is_connected:
        print('Армирование двигателя')
        # Симулируем проверку безопасности
        print('Проверка безопасности...')
        is_armed = True
        propellers_speed = [random.randint(0, 100),
                    random.randint(0, 100),
                    random.randint(0, 100),
                    random.randint(0, 100)]

print(info)
drone_connect()
arm_drone()
info = f"""
--------Квадрокоптер---------
Высота: {altitude} м, Скорость: {speed} м/сек.
Вес БПЛА: {weight} кг, Грузоподъемность: {speed} грамм
Тангаж: {pitch} градусов, Крен: {roll} градусов, Рысканье: {yaw} градусов
Скорость вращения пропеллеров: {propellers_speed}
({propellers_speed[0]})       ({propellers_speed[1]})
 CCW      CW
  \\        /
   \\      /
    ------
   /      \\
  /        \\
 CW       CCW
({propellers_speed[2]})       ({propellers_speed[3]})
"""
print(info)