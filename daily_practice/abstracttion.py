from abc import ABC, abstractmethod
#abstract class is a class that cannot be instantiated directly and is meant to serve as a blueprint for other classes,
#it can have both abstract method and concrete method
#Abstract classess are typically used to define common behaviours that subclasses must implement

class Vehicle(ABC):
    #abstract method - methods declared but not implemented they do not have a body.
    @abstractmethod
    def start_engine(self):
        pass
    def apply_break(self):   #concrete method - methods that are fully implemented and can be inherited by child classes.
        print('Applying Break')
    
class Car(Vehicle):
    def start_engine(self):
        print('starting the car engine')
class Truck(Vehicle):
    def start_engine(self):
        print('starting the truck engine')

my_car = Car()
my_car.start_engine()

#key notes: Abstract classes focus on providing a common interface and shared behaviour use an abstact class when multiple subclasses share common behaviour but also require unique implementations for specific methods.
