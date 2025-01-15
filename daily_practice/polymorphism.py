class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        print('hon honk!')
class SportsCar(Car):
    def honk(self):
        print('beep beep!')
class Truck(Car):
    def honk(slef):
        print('poo poo!')
        