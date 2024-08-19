import numpy as np

# ID БПЛА | Время полета (минуты) | Расстояние (километры) | Средняя скорость (км/ч) | Высота полета (метры)
drones_data = np.array([
    [1, 30, 10, 20, 500],
    [2, 45, 15, 20, 600],
    [3, 25, 8, 19.2, 550],
    [4, 60, 25, 25, 700],
    [5, 35, 12, 20.6, 580]
])
# print("Данные о полетах БПЛА:")
# print(drones_data)

# altitudes = drones_data[:, -1]
altitudes = drones_data[:, 4]
# max_altitude = np.max(altitudes)
# print(f'Максимальная высота полета: {max_altitude}')

# long_flight_drones1 = drones_data[:, 1]
# print(f'Этап 1\n{long_flight_drones1}')

# long_flight_drones2 = drones_data[:, 1] > 30
# print(f"Этап 2\n{long_flight_drones2}")

# long_flight_drones3 = drones_data[drones_data[:, 1] > 30]
# print('Этап 3')
# print(f'Дроны летающие долше 30 минут\n{long_flight_drones3}')

# total_dist = np.sum(drones_data[:, 2])
# print(f"Всего пройдено расстояние: {total_dist} км")


import matplotlib.pyplot as plt

drone_ids = drones_data[:, 0]
flight_times = drones_data[:, 1]
# altitudes = drones_data[:, 4]

# т.к. не через пандас - должны построить полотно!
plt.figure(figsize=(10, 5))

# строим подграфик 1 строка, 2 графика, и это - 1-ый график
# plt.subplot(1, 2, 1)
# plt.bar(drone_ids, flight_times, color="blue")
# plt.xlabel('ID БПЛА')
# plt.ylabel('Время полета (минуты)')
# plt.title('Время полета БПЛА')

# plt.subplot(1, 2, 2)
# plt.bar(drone_ids, altitudes, color="green")
# plt.xlabel('ID БПЛА')
# plt.ylabel('Высота полета (метры)')
# plt.title('Высота полета БПЛА')

# plt.show()

convertation_matrix = np.array([
    [1, 0],
    [0, 0.277778]
])

speed_kmh = drones_data[:, 3]
speed_ms = speed_kmh * convertation_matrix[1, 1]

# print(convertation_matrix[1, 1]) # 0.277778
print(f'speed_kmh: {speed_kmh}')
print(f'speed_ms: {speed_ms}')

print(speed_kmh * 0.277778)
