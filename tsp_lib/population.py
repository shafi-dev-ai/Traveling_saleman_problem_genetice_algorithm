from tsp_lib.route import *


class Population:
    route = [Route()]

    def __init__(self, populationSize, init):
        self.populationSize = populationSize
        if init:
            for i in range(populationSize):
                newTour = Route()
                newTour.generate_Individual()
                self.route.append(newTour)

    def setRoute(self, key, route):
        try:
            self.route[key] = route
        except IndexError:
            print("cannot insert in the route ...!! index error population")

    def getRoute(self, key):
        try:
            return self.route[key]
        except IndexError:
            print("Index out of bound..!! population get")

    def population_size(self):
        return int(self.populationSize)

    def __eq__(self, other):
        return self.route == other.route

    def __setitem__(self, key, value):
        try:
            self.route[key] = value
        except IndexError:
            print("cannot insert in the route ...!! index error population")

    def __getitem__(self, key):
        try:
            return self.route[key]
        except IndexError:
            print("Index out of bound..!! population get")

    def getFittest(self):
        fittest = self.route[0]
        fitness_value = int(fittest.Fitness())
        for i in range(1, self.populationSize):
            i_th_fitness_value = int(self.getRoute(i).Fitness())
            if fitness_value <= i_th_fitness_value:
                fittest = self.getRoute(i)
        return fittest

    def sum_of_fitness(self):
        fitness_sum = 0
        for i in range(0, self.populationSize):
            fitness_sum += self.getRoute(i).Fitness()
        return fitness_sum

    def fitness_ratio(self, index):
        return int((self.getRoute(index).Fitness() / self.sum_of_fitness()) * 100)

    def toString(self):
        string = ''
        print("Route no \tF(x) \tFitness(x)\tFitness ratio\n")
        for i in range(0, self.populationSize):
            string += 'Route {}    {}      {}         {} \n'.format(i, self.route[i].getDistance(), self.route[i].Fitness(), self.fitness_ratio(i))
            '''
                'Route ' + str(i) + '\t\t\t' + str(self.route[i].getDistance()) + '\t\t\t' + str(
                self.route[i].Fitness()) + '\t\t\t' + str(self.fitness_ratio(i)) + ' % \n'
                            '''
        return string
