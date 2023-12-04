import numpy as np

x_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y_values = np.array([0, 2.8, 2.03, -1.33, -2.99, -0.84, 2.38, 2.56, -0.52, -2.94], float)
x0 = float(input('Введите точку в которой хотите посчитать значение:'))

def divided_diff_coefficients(x_values, y_values):
    """
    Вычисляет коэффициенты разделённых разностей для построения полинома Ньютона.

    :param x_values: Значения x (точки, в которых известны значения функции).
    :param y_values: Значения функции в соответствующих точках x.
    :return: Список коэффициентов разделённых разностей.
    """
    n = len(x_values)
    coefficients = y_values.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x_values[i] - x_values[i - j])

    return coefficients


def newton_interpolation_polynomial(x_values, y_values):
    """
    Вычисляет интерполяционный полином Ньютона.

    :param x_values: Значения x (точки, в которых известны значения функции).
    :param y_values: Значения функции в соответствующих точках x.
    :return: Функция интерполяционного полинома.
    """
    coefficients = divided_diff_coefficients(x_values, y_values)

    def newton_polynomial(x):
        result = coefficients[0]
        product_term = 1.0

        for i in range(1, len(coefficients)):
            product_term *= (x - x_values[i - 1])
            result += coefficients[i] * product_term

        return result

    return newton_polynomial


from sympy import Symbol, diff


def interpolate_derivative_at_point(x_values, y_values, x0, interpolation_method):
    """
    Вычисляет производную интерполяционного полинома в заданной точке x0.

    :param x_values: Значения x (точки, в которых известны значения функции).
    :param y_values: Значения функции в соответствующих точках x.
    :param x0: Точка, в которой вычисляется производная.
    :param interpolation_method: Метод интерполяции ('lagrange' или 'newton').
    :return: Значение производной в точке x0.
    """

    # Находим производную полинома
    interpolation_poly = newton_interpolation_polynomial(x_values, y_values)
    x = Symbol('x')
    derivative_poly = diff(interpolation_poly(x), x)

    # Подставляем x0 в производную
    result = derivative_poly.subs(x, x0)
    return result

print()
result_newton = interpolate_derivative_at_point(x_values, y_values, x0, interpolation_method='newton')
print(f"Значение производной в точке x = {x0}: {result_newton}")
