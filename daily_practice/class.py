class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        print('Honk honk')
my_car = Car('Tesla','Model S',2022)
print(my_car.make)
print(my_car.year)
my_car.honk()