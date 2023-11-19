import numpy as np

# Чтение матрицы из файла
matrix = np.genfromtxt('matrix.txt', delimiter=',')
print("Исходная матрица:")
print(matrix)

# Нахождение суммы всех элементов, максимального и минимального элементов
sum_all = np.sum(matrix)
max_value = np.max(matrix)
min_value = np.min(matrix)

print(f"Сумма всех элементов: {sum_all}")
print(f"Максимальный элемент: {max_value}")
print(f"Минимальный элемент: {min_value}")
