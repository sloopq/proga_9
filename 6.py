import numpy as np

a = np.arange(16).reshape(4, 4)
print("Исходный массив:")
print(a)

# Поменять местами строки 1 и 3
a[[1, 3]] = a[[3, 1]]

print("Массив после замены строк:")
print(a)
