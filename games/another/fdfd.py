class Car:
    def __init__(self, maximum_speed, unit):
        try:
            self.maximum = int(maximum_speed)
        except:
            
            pass
        self.maximum = maximum_speed
        self.unit = unit
        self.string = f"Car with maximum speed of {self.maximum} {self.unit}"
       

class Boat:
    def __init__(self, maximum_speed):
        try:
            self.maximum = int(maximum_speed)
        except:
            # self.maximum = maximum_speed
            pass
        self.maximum = maximum_speed
        self.string = f"Boat with maximum speed of {self.maximum} knots"
        

if __name__ == '__main__':
    fptr = open('data.txt', 'w')
    q = int(input())
    queries = []
    for i in range(q):
        args = input().split(' ')
        vehicle_type, params = args[0], args[1:]
        if vehicle_type.lower() == "car":
            max_speed, speed_unit = params[0], params[1]
            vehicle = Car(max_speed, speed_unit)
            vehicle = vehicle.string
        elif vehicle_type.lower() == "boat":
            max_speed = params[0]
            vehicle = Boat(max_speed)
            vehicle = vehicle.string
            
        else:
            raise ValueError("invalid vehicle type")
        fptr.write(f"{vehicle}\n")
        
    fptr.close()