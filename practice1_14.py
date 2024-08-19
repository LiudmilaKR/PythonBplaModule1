class Drone:
    
    def __init__(self, id, altitude=0) -> None:
        self.id = id
        self.altitude = altitude
        
    def takeoff(self):
        self.altitude = 100
        print(f'{self.id} взлетел на высоту {self.altitude}')

def main():
    my_drone = Drone('IDtest')
    my_drone.takeoff()
    
    
if __name__ == '__main__':
    main()