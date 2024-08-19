class GPS:
    def __init__(self) -> None:
        # координаты (широта, долгота)
        pass
    
    # метод обновления координат

class FlightContrloller:
    def __init__(self) -> None:
        # координаты (шарота, долгота)
        # высота
        # карта полёта (список из координат)
        # is_flying (летим ли сейчас?)
        pass
    
    # метод включить двигатель
    # метод армирование
    # метод пуск, взлет, ниже, выше, вправо, влево, на одни координаты и другие
    
class Camera :
    def __init__(self, resolution) -> None:
        # разрешение камеры
        # зум камеры
        # частота кадоров камеры
        pass
    
    # метод делать фото
    # метод захват изображения
    # метод запись, трансляция, ночная съемка и т.д.

# дрон наследуется от предыдущих классов 
class Drone(Camera, GPS, FlightContrloller):
    
    def __init__(self, id, model, resolution) -> None:
        # id
        # модель
        # заводская инфо
        # super().__init__()
        Camera.__init__(resolution)