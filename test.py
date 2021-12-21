from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def Rectangle_Area(self, x, y):
        pass

    @abstractmethod
    def Square_Area(self, x):
        pass

    @abstractmethod
    def Circle_Area(self, x):
        pass


