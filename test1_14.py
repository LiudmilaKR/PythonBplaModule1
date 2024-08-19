import pdb
from practice1_14 import Drone

def test_takeoff():
# трассировка устанавливает точки останова
    pdb.set_trace()
    test_drone = Drone('testDrone')
    test_drone.takeoff()
    assert test_drone.altitude == 101, 'Успешно взлетели на 100 метров'
    # assert test_drone.altitude == 101, 'Тест не прошёл'
    
if __name__ == '__main__':
    test_takeoff() # запустили тест взлета