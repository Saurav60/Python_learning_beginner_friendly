# encapsulation helps to bundle data and methods inside class 
# here we restricts direct access to certain attributes and methods 
class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year
        self.__speed = 0 
    def increase_speed(self, speed):
        return self.__accelerate(speed)
    def get_speed(self):
        return self.__speed
    def __accelerate(self, speed):
        if self.__speed + speed <= 100:
            self.__speed += speed
        else:
            self.__speed = 100
        return self.__speed
my_car = Car('tesla','Model s', 2022)
#print(my_car.get_speed())
print(my_car.increase_speed(40))
print(my_car.get_speed())
