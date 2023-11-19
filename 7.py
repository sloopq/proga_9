import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Получение столбца species
species_column = iris[:, -1]

# Нахождение уникальных значений и их количества
unique_species, counts = np.unique(species_column, return_counts=True)

print("Уникальные значения в столбце species:", unique_species)
print("Количество каждого значения:", counts)
