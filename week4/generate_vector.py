import random
def generate_vectors( n = 10 , m = 8):
	vector = [[0]*n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			if random.random() >= 0.5:
				vector[i][j] = 1
	return vector

def random_search(data):
	result = []
	for i in data:
		result.append( sum(i))
	return result
print(len(generate_vectors()))
print(random_search(generate_vectors()))