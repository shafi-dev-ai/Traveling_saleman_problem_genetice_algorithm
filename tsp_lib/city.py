import random
import math


class City:
    x = 0
    y = 0

    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)
        else:
            self.x = x
            self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        s = '(' + str(self.get_x()) + ',' + str(self.get_y()) + ')'
        return s

    def Distance_city(self, city):
        # euler distance
        dis_x = abs(self.get_x() - city.get_x())
        dis_y = abs(self.get_y() - city.get_y())
        distance = math.sqrt((math.pow(dis_x, 2)) + (math.pow(dis_y, 2)))
        return distance

    def checkNull(self):
        if self.x == -1 or self.x is None:
            return True
        else:
            return False


class RouteCityManager:
    destination_city = []

    @classmethod
    def appendCity(cls, city: City):
        cls.destination_city.append(city)

    @classmethod
    def getCity(cls, index):
        try:
            return cls.destination_city[index]
        except IndexError:
            print("Index out of bound..!!! route city manager")

    @classmethod
    def noOfCity(cls):
        return len(cls.destination_city)
