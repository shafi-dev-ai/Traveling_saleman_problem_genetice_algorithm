from tsp_lib.city import *


class Route:

    def __init__(self, route=None):
        self.route = []
        self.fitness = 0
        self.distance = 0
        if route is None:
            for i in range(0, 20):
                self.route.append(City(random.randint(0, 100), random.randint(0, 100)))
        else:
            self.route = route

    def generate_Individual(self):
        # for disindex in range(RouteCityManager.noOfCity()):
        # self.setCity(disindex, RouteCityManager.getCity(disindex))
        random.shuffle(self.route)

    def getCity(self, key):
        try:
            return self.route[key]
        except IndexError:
            print("index out of bound....! route ger city")

    def setCity(self, key, city):
        try:
            self.route[key] = city
        except IndexError:
            print("cannot insert at this index route set city")
        self.fitness = 0
        self.distance = 0

    def toString(self):
        geneString = "|"
        for i in range(0, self.routeSize()):
            geneString += str(self.getCity(i)) + "| --> |"
        geneString += "Finish!|"
        return geneString

    def routeSize(self):
        return len(self.route)

    def __len__(self):
        return len(self.route)

    def __getitem__(self, index):
        try:
            return self.route[index]
        except IndexError:
            print("index out of bound....!route ger city")

    def __setitem__(self, key, value):
        try:
            self.route[key] = value
        except IndexError:
            print("cannot insert at this index route set cit")

    def containsCity(self, city: City):
        if city in self.route:
            return True
        else:
            return False

    def getDistance(self):
        if self.distance == 0:
            route_dis = 0
            for dixindex in range(self.routeSize()):
                from_city = self.getCity(dixindex)
                if dixindex + 1 < self.routeSize():
                    des_city = self.getCity(dixindex + 1)
                else:
                    des_city = self.getCity(0)
                route_dis += from_city.Distance_city(des_city)
            return int(route_dis)

    def Fitness(self):
        if self.fitness == 0:
            fit = 100 - self.getDistance()
            return fit * -1
