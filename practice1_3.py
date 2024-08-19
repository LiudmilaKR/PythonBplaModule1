import random
import time

altitude = 0 # Высота в метрах
speed = 0 # Скорость в метрах в секунду
weight = 1.5 # Вес БПЛА в килограммах
# fuel = 100 # Топливо в процентах

# тангаж - один из углов летательного аппарата относительно абциссы (горизонтали)
pitch = 0 # Тангаж в градусах
# Тангаж в градусах (Поворот вокруг поперечной оси (наклон вперед или назад))
roll = 0 # Крен в градусах
# Крен в градусах (Поворот вокруг продольной оси (наклон влево или вправо))
yaw = 0 # Рысканье в градусах
# рысканье - поворот вокруг оси z (вокруг вертикальной оси, куда направлен нос аппарата)
# Рысканье в градусах (Поворот вокруг вертикальной оси)

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

propellers_speed = [0, 0, 0, 0] # Скорости вращения пропеллеров в об\мин
propellers_direction = ['CCW', 'CW', 'CW', 'CCW'] # Направление вращения пропеллеров
direction = 0 # Направление в градусах (по сути - азимут для БПЛА)
payload = 500 # Грузоподъёмность в граммах

is_flying = False # Летит ли БПЛА
is_connected = False # Подключен ли БПЛА (связь с БПЛА)
# армирование двигателя - подготовка двигателя к работе (проверка безопасности, того, что двигатель готов к работе, предотвращает случайное включение двгителя)
is_armed = False # Арминг (состояние) двигателя
# телеметрия - наши все показали: высота, скорости и пр., передается всегда с помощью словаря
speed_k = 1000  # коэффициент скорости, 1 м/с = 1000 об/мин

coordinates = (50.1231, 30.5231) # начальные координаты
target_coord = (30.2344, 42.5332) # координаты цели (куда должны прилететь)

way_coords = []  # где был дрон, его координаты

def get_info():
    info = f"""
--------Квадрокоптер---------
Высота: {altitude} м, Скорость: {speed} м/сек.
Вес БПЛА: {weight} кг, Грузоподъемность: {speed} грамм
Тангаж: {pitch} градусов, Крен: {roll} градусов, Рысканье: {yaw} градусов
Скорость вращения пропеллеров: {propellers_speed}
({propellers_speed[0]})       ({propellers_speed[1]})
CCW        CW
 \\        /
  \\      /
   ------
  /      \\
 /        \\
CW        CCW
({propellers_speed[2]})       ({propellers_speed[3]})
    """
    print(info)

# Функция подключения к дрону
def drone_connect():
    global is_connected
    print('Подключение к БПЛА...')
    time.sleep(1)
    is_connected = True
    print('Подключение установлено')

# Функция проверки (армирование) дрона (после подключения к нему)
def arm_drone():
    global is_armed, propellers_speed
    if is_connected:
        print('Армирование двигателя')
        # Симулируем проверку безопасности
        time.sleep(3)
        print('Проверка безопасности завершена!')
        is_armed = True
        start = 100
        propellers_speed = [start, start, start, start]
        way_coords.append(coordinates)
        print('Двигатель армирован.')
        print(f'Скорость вращения пропеллера {start} об/мин')
        print(f'Направление движения пропеллерров {propellers_direction}')
    else:
        print('Не удалось армировать двигатель. БПЛА не подключён.')

def set_propellers_speed(speed):
    global propellers_speed
    if is_armed:
        propellers_speed = [speed * speed_k, speed * speed_k, speed * speed_k, speed * speed_k]
        print(f'Установлена скорость вращения пропеллера: {propellers_speed} об\мин')
    else:
        print(f'Не удалось установить скорость вращения пропеллеров. Двигатель не армирован.')

# функция перемещения к координате
def move_to_coord(target):
    global coordinates, altitude, speed, direction
    if is_armed and is_flying:
        print(f'Перемещаемся к координатам: {target}...')
        coordinates = target
        altitude = 10
        speed = 6
        direction = 200
        time.sleep(3)
        print('Достигли цели!')
        way_coords.append(coordinates)

get_info()
drone_connect()
arm_drone()
get_info()

if is_armed and is_connected:
    set_propellers_speed(1000)
    print('Взлет!')
    speed = 5
    altitude = 10
    pitch = 15
    roll = 5
    yaw = 10
    direction = 90
    is_flying = True
    battery_capacity -= 5
    coordinates = (50.1231, 30.5231)
    telemetry = {
        "speed": speed,
        "altitude": altitude,
        "pitch": pitch,
        "roll": roll,
        "yaw": yaw,
        "direction": direction,
        "propellers_speed": propellers_speed,
        "propellers_direction": propellers_direction,
        "coordinates": coordinates,
        "battery_capacity": battery_capacity
    }
    print(f"Телеметрия: {telemetry}")
else:
    print('Взлететь не удалось')

if is_flying:
    move_to_coord(target_coord)
    
get_info()

# Выводим весь путь дрона
print(way_coords)
# Подменяем начальные координаты на случайные вещественные числа c помощью функции uniform
# функция round позволяет округлить числа до 4 знаков после запятой
# чтобы число было похоже на реальную координату
way_coords[0] = (round(random.uniform(1, 50), 4), round(random.uniform(1, 50), 4))
print(way_coords)
