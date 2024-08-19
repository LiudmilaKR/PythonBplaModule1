import unittest
# from .practice1_15 import Drone
from practice1_15 import Drone


class TestDrone(unittest.TestCase):
    
    # запуск кода перед тестированием
    def setUp(self):
        self.drone = Drone()
    
    # если нет self - временная переменная
    def test_takeoff(self):
        # проверяем заряд батареи
        # высокий уровень заряда
        self.drone.battery_level = 50
        result = self.drone.takeoff()
        self.assertTrue(self.drone.is_flying)
        self.assertEqual(result, 'Дрон взлетел')
        
        # низкий уровень заряда
        self.drone.battery_level = 10
        result = self.drone.takeoff()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Низкий заряд батареи для взлета')
        
    def test_land_not_flying(self):
        self.drone.is_flying = False
        result = self.drone.land()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Дрон уже на земле')
        
    def test_land_not_flying(self):
        self.drone.is_flying = True
        result = self.drone.land()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Дрон приземлился')
        
# если код запускаем из этого файла, то name содержит main 
if __name__ == '__main__':
    unittest.main()
    
# юниттест можно запустить через терминал python -m unittest ".\Module 1\test1_15.py"