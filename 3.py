import numpy as np

# Создание массива случайных чисел нормального распределения размера 10x4
data = np.random.randn(10, 4)

# Нахождение статистик
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)
mean_values = np.mean(data, axis=0)
std_deviation = np.std(data, axis=0)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = data[:5]

print("Минимальные значения по столбцам:", min_values)
print("Максимальные значения по столбцам:", max_values)
print("Средние значения по столбцам:", mean_values)
print("Стандартное отклонение по столбцам:", std_deviation)
print("Первые 5 строк:")
print(first_five_rows)
