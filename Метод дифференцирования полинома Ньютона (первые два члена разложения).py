import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)
y = np.array([0, 2.8, 2.03, -1.33, -2.99, -0.84, 2.38, 2.56, -0.52, -2.94], float)
z = float(input('Введите точку в которой хотите посчитать значение:'))

def numerical_diff(z):
    for i in range(len(x)):
        if x[i] >= z:
            return (y[i] - y[i-1]) / (x[i] - x[i-1]) + (2*z-x[i-1]-x[i]) * ((y[i+1] - y[i])/(x[i+1] - x[i]) - (y[i] - y[i-1]) / (x[i] - x[i-1])) / (x[i+1] - x[i-1])

print()
print(f"Значение производной в точке x = {z}: {numerical_diff(z)}")
