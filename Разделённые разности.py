import numpy as np
xval = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)
yval = np.array([0, 2.8, 2.03, -1.33, -2.99, -0.84, 2.38, 2.56, -0.52, -2.94], float)
z = float(input('Введите точку в которой хотите посчитать значение:'))

def numerical_diff(z):
    for i in range(len(xval)):
        if xval[i] > z:
            return (yval[i] - yval[i-1]) / (xval[i] - xval[i-1])
        if xval[i] == z:
            return (yval[i+1] - yval[i-1]) / (xval[i+1] - xval[i-1])
print()
print(f"Значение производной в точке x = {z}: {numerical_diff(z)}")
