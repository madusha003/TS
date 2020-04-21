import numpy as np

type = input('1- ellipse, 2- hyperbola, 3- parabola:\n')
x = [0] * 3
y = [0] * 3
for i in range(3):
    print('Input coordinate #', i + 1)
    x[i], y[i] = [float(co) for co in input().split()]

if type == '3':
    if x[0] != 0 and y[0] != 0:
        print('x^2 = 2 *', y[0] * 2 / (2 ** x[0]), '* y')
    else:
        print('x^2 = 2 *', y[1] * 2 / (2 ** x[1]), '* y')

if type == '2':
    a = (y[0] ** 2 * x[1] ** 2 - x[0] ** 2 * y[1] ** 2) / (y[0] ** 2 - y[1] ** 2)
    b = (y[0] ** 2 * x[1] ** 2 - x[0] ** 2 * y[1] ** 2) / (x[0] ** 2 - x[1] ** 2)
    print('x^2/', a, ' - ', 'y^2/', b, ' = 1')

if type == '1':
    a = (x[0] ** 2 * y[1] ** 2 - x[1] ** 2 * y[0] ** 2) / (y[1] ** 2 - y[0] ** 2)
    b = (x[0] ** 2 * y[1] ** 2 - x[1] ** 2 * y[0] ** 2) / (x[0] ** 2 - x[1] ** 2)
    print('x^2/', a, ' + ', 'y^2/', b, ' = 1')
