from tsp_lib.population import *


class GeneticAlgorithm:
    mutation_Rate = 0.015
    tourSize = 5
    elitism = True

    @classmethod
    def evolve_Population(cls, population: Population):
        new_population = Population(population.populationSize, False)
        offset = 0
        if cls.elitism:
            new_population.setRoute(0, population.getFittest())
            offset = 1

        for i in range(offset, new_population.populationSize):
            first_parent = cls.selection(population)
            second_parent = cls.selection(population)
            child = cls.crossover(first_parent, second_parent)
            new_population.setRoute(i, child)

        for i in range(offset, new_population.populationSize):
            cls.mutation(new_population.getRoute(i))
        return new_population

    @classmethod
    def crossover(cls, parent1: Route, parent2: Route):
        child = Route()
        startPos = 0
        endPos = 0
        while startPos == endPos:
            startPos = random.randint(0, parent1.routeSize() - 1)
            endPos = random.randint(0, parent2.routeSize() - 1)

        for i in range(child.routeSize()):
            if startPos < endPos and startPos < i < endPos:
                child.setCity(i, parent1.getCity(i))

            elif startPos > endPos:
                if not (startPos > i > endPos):
                    child.setCity(i, parent1.getCity(i))

        for i in range(parent2.routeSize()):
            if not (child.containsCity(parent2.getCity(i))):
                for j in range(child.routeSize()):
                    if child.getCity(j).checkNull():
                        child.setCity(j, parent2.getCity(i))
                        break
        return child

    @classmethod
    def mutation(cls, route):
        routePos1 = 0
        routePos2 = 0
        while routePos1 == routePos2:
            routePos2 = random.randint(0, route.routeSize() - 1)
            routePos2 = random.randint(0, route.routeSize() - 1)
        if random.randrange(1) < cls.mutation_Rate:
            first_city = route.getCity(routePos1)
            second_city = route.getCity(routePos2)

            route.setCity(routePos2, first_city)
            route.setCity(routePos1, second_city)

    @classmethod
    def selection(cls, population: Population):
        route = Population(cls.tourSize, False)
        for i in range(cls.tourSize):
            rand_index = random.randint(0, population.populationSize - 1)
            route.setRoute(i, population.getRoute(rand_index))

        fittest = route.getFittest()
        return fittest

    def toString(self):
        pass
