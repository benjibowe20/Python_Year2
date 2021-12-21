"""
    Prevents a user from creating an object of that class.
    Compels a user to override abstract methods in a child class.

    Abstract Class -> A class which contains one or more abstract methods.
    Abstract Method -> A method that has a declaration but does not have an implementation.

"""

#Always include following line when using abstarct classes
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is moving.")

class Motorbike(Vehicle):
    def go(self):
        print("The motorbike is moving")

car = Car()
motorbike = Motorbike()

car.go()
motorbike.go()


