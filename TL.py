from tlbofitnessfunctions import pressure_vessel, fitness_function_1, fitness_function_3
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import check_random_state
from swarmlib import FUNCTIONS

class TeachingLearning(object):

    def __init__(self, func, lower_bound, upper_bound,n_population=50,random_state=None):

        self.function = func # function to minimize
        self.lower_bound = lower_bound # lower bound
        self.upper_bound = upper_bound # upper bound
        self.index = list(range(n_population)) # population indexes
        self.dimension = lower_bound.shape[0]  # columns basicalyy our dimensions
        self.random_state = check_random_state(random_state) # random state
        self.population = self.random_state.rand(n_population, self.dimension) * (upper_bound - lower_bound) + lower_bound
        self.fitness = np.apply_along_axis(self.function, 1, self.population)
        self.fit_index = np.argmin(self.fitness)

    def best(self, num=1):
        bestidxs = np.argmin(self.fitness)
        return self.population[bestidxs], self.fitness[bestidxs]

    def classroom(self):
        mean = np.nanmean(self.population, axis=0)  # column mean.
        rs = self.random_state
        teacher = np.argmin(self.fitness)  # select teacher index from the fitness arrayy using argmin

        # teaching phase
        for i in self.index:
            T_F = 1+rs.randint(0,2)  # teaching factor is randomly 1 or 2.
            r_i = rs.rand(self.dimension)  # multiplier also random. 1 row * 13 columns

            new_solution = self.population[i] + (r_i * (teacher - (T_F * mean))) # new solution 1 row * 13 columns
            new_solution = np.minimum(np.maximum(new_solution, self.lower_bound), self.upper_bound)

            new_fitness = self.function(new_solution)

            if new_fitness < self.fitness[i]:
                self.population[i] = new_solution
                self.fitness[i] = new_fitness

        # Until Here we find a fitness from teacher
        # learning phase
        for i in self.index:

            j = rs.choice(self.index[:i] + self.index[(i + 1):], 1)  # pick another random i!=j 
            r_i = rs.rand(self.dimension)

            if self.fitness[i] < self.fitness[j]:
                new_solution = self.population[i] + r_i * (self.population[i] - self.population[j]).flatten()
            else:
                new_solution = self.population[i] + r_i * (self.population[j] - self.population[i]).flatten()

            new_solution = np.minimum(np.maximum(new_solution, self.lower_bound), self.upper_bound)
            new_fitness = self.function(new_solution)

            if new_fitness < self.fitness[i]:
                self.population[i] = new_solution
                self.fitness[i] = new_fitness

if __name__ == "__main__":

    """First Fitness Function"""
    lower= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
    upper= np.array([1,1,1,1,1,1,1,1,1,100,100,100,1])
    population = 50
    max_iter = 500

    X = TeachingLearning(fitness_function_1, lower,upper, n_population=population, random_state=40)
    data1 = []
    for i in range(max_iter):
        X.classroom()
        solution, fitness = X.best()
        data1.append(fitness)
    print("TLBO solution ",solution," fitness ",fitness)
    plt.plot(data1,label='Fitness Function 1')
    plt.title("Function 1")
    plt.xlabel("Iterations")
    plt.ylabel("Min function(x)")   
    # plt.show()
    plt.close()

    """Third Fitness Function"""
    lower = np.array([-10,-10,-10,-10,-10,-10,-10])
    upper = np.array([10,10,10,10,10,10,10])
    population = 50
    max_iter = 200
    X = TeachingLearning(fitness_function_3, lower,upper, n_population=population, random_state=10)
    data2 = []
    for i in range(max_iter):
        X.classroom()
        solution, fitness = X.best()
        data2.append(fitness)
    print("TLBO solution ",solution," fitness ",fitness)
    plt.plot(data2)
    plt.title("Function 3")
    plt.xlabel("Iterations")
    plt.ylabel("Min function(x)")   
    # plt.show() 
    plt.close()

    """Pressue Vessel Design"""
    lower = np.array([0,0,10,10])
    upper = np.array([99,99,200,200])
    population = 50
    max_iter = 200

    X = TeachingLearning(pressure_vessel, lower,upper, n_population=population, random_state=50)
    data3 = []
    for i in range(max_iter):
        X.classroom()
        solution, fitness = X.best()
        
        data3.append(fitness)
    print("TLBO solution ",solution," fitness ",fitness)
    plt.plot(data3,label='Pressure Vessel Function')
    plt.title("Pressure Vessel Design")
    plt.xlabel("Iterations")
    plt.ylabel("Min f(x)")   
    plt.show()