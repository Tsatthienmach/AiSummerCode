import random

n = 20  # size of individual
m = 10	# size of population
n_generations = 40 # number of generations

# for drawing chart to show the effective method
fitness = []

def generate_random_value():
	return random.randint(0,1)

def create_individual():
	return [generate_random_value() for _ in range(n)]

def compute_fitness(individual):
	return sum(individual)

def crossover(individual1 , individual2 , crossover_rate = 0.9):
	"Lai tao"
	individual1_new = individual1.copy()
	individual2_new = individual2.copy()
	for i in range(n):
		if random.random() < crossover_rate:
			individual1_new[i] = individual2[i]
			individual2_new[i] = individual1[i]

	return individual1_new, individual2_new

def mutate (individual, mutation_rate = 0.05):
	"dot bien gen"
	individual_n = individual.copy()
	for i in range(n):
		if random.random() < mutation_rate:
			individual_n[i] = generate_random_value()
	return individual_n	

def selection(sorted_old_population):
	"Chon loc"
	index1 = random.randint(0,m-1)
	while True:
		index2 = random.randint(0,m-1)
		if (index2 != index1):
			break
	individual_s = sorted_old_population[index1]
	if index2 > index1:
		individual_s = sorted_old_population[index2]
	return individual_s

def create_new_population(old_population , elitism= 2 , gen = 1):
	sorted_population = sorted(old_population, key = compute_fitness)
	# print(len(sorted_population))
	if gen %1 == 0:
		a = sorted_population[m-1]
		fitness.append(compute_fitness(a))
		print('BEST: ',compute_fitness(sorted_population[m-1]))

	# print('Xong')def create_individual():
	new_population = []
	while len(new_population) < m-elitism:
		# selection
		individual_s1 = selection(sorted_population)
		individual_s2 = selection(sorted_population)
		# crossover
		individual_c1 , individual_c2 = crossover(individual_s1,individual_s2)
		#mutate
		individual_m1 = mutate(individual_c1)
		individual_m2 = mutate(individual_c2)

		new_population.append(individual_m1)
		new_population.append(individual_m2)
	# print('ind', end = '\n')
	new_population.append(sorted_population[m-elitism].copy())
	# print(new_population)
	return new_population

population = [create_individual() for _ in range (m)]


for i in range(n_generations):
	# print('popu: ', end = '\n')
	m = len(population)
	print(m)
	population = create_new_population(population,2, i)

import matplotlib.pyplot as plt 

# print(fitness)
plt.plot([i for i in range(n_generations)],fitness)
plt.show()