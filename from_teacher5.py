import random


class GPS:

    def __init__(self, init_coordinates=(0.0, 0.0)):
        self.coordinates = init_coordinates

    def update_coordinates(self):
        """
        Симулирует обновление координат GPS
        """
        # lat = round(random.uniform(1, 50), 4) # широта
        # lon = round(random.uniform(1, 50), 4) # долгота
        lat_variation = random.uniform(-0.0001, 0.0001)  # изменение широты
        lon_variation = random.uniform(-0.0001, 0.0001)  # изменение долготы
        lat = round(self.coordinates[0] + lat_variation, 4)
        lon = round(self.coordinates[1] + lon_variation, 4)
        self.coordinates = (lat, lon)
        # print(f"Обновленные коодинат: {self.coordinates}")
        return self.coordinates


if __name__ == "__main__":
    gps_module = GPS((55.7558, 37.6176))
    print(gps_module.coordinates)
    # for i in (0, 1, 2, 3):
    for i in range(100):
        gps_module.update_coordinates()
    print(gps_module.coordinates)
