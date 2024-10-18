from tsp_lib.genetic_algo import *
from tsp_lib.population import *
from tsp_lib.city import RouteCityManager
import csv


def init_tourManager(Manager: RouteCityManager, pop: Population):
    for k in range(0, pop.populationSize):
        for j in range(0, 20):
            Manager.appendCity(pop.route[k].getCity(j))


if __name__ == '__main__':
    tour_manager = RouteCityManager()
    p = Population(6, True)
    init_tourManager(tour_manager, p)
    print(p.toString())
    print('Initial distance:-> ' + str(p.getFittest().getDistance()))
    fittest = 0
    for i in range(p.populationSize):
        p = GeneticAlgorithm.evolve_Population(p)
        fittest = p.getFittest().getDistance()
    print('Final Distance:->' + str(fittest))
    print('Final Route: ' + p.getFittest().toString())
    with open('distance_data.csv', 'w', newline='')as file:
        writer = csv.writer(file)
        for i in range(0, 20):
            dist = float(tour_manager.getCity(i).Distance_city(tour_manager.getCity(i+1)))
            file.write('Distance from %s:' % i)
            file.write(" to %s " % str(i+1))
            file.write(' = %s\n' % dist)
