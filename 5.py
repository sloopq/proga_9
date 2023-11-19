import numpy as np
from scipy.stats import multivariate_normal

def log_density(X, m, C):
    D = m.shape[0]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    constant_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    
    diff = X - m
    exponent_term = -0.5 * np.sum(np.dot(diff, inv_C) * diff, axis=1)
    
    return constant_term + exponent_term

# Пример использования
mean = np.array([0, 0])
covariance = np.array([[1, 0.5], [0.5, 1]])
points = np.random.randn(100, 2)  # Пример случайных точек
log_density_values = log_density(points, mean, covariance)
scipy_log_density = multivariate_normal(mean=mean, cov=covariance).logpdf(points)

# Сравнение результатов
print("Разница между результатами log_density и scipy.stats.multivariate_normal.logpdf:")
print(np.max(np.abs(log_density_values - scipy_log_density)))
