# impport libriries
import numpy as np
import matplotlib.pyplot as plt

# initialize constants
a, b, c = 5, 10, -30

limit = 5
step = 0.001

# range of x-values
x = np.arange(-limit, limit, step)

# main function
def func(x):
    return a * x**2 + b*x + c

# function roots
def take_roots(a, b, c) -> tuple:
    discr = (b**2 - 4*a*c)
    
    if discr > 0:
        x1 = (-b + discr**0.5) / (2*a)
        x2 = (-b - discr**0.5) / (2*a)
        return (round(x1, 2), round(x2, 2))

    elif discr == 0:
        x = -b / (2*a)
        return (round(x, 2),)

    else:
        return (None,)

# min x- and y- coordinates
min_y = min(func(x))
min_x = take_roots(a, b, c - min_y)[0]

# roots of the function
roots = take_roots(a, b, c)

# devide the graph into four partitions
x_down_pos = np.arange(-limit, min(roots), step)
x_down_neg = np.arange(min(roots), min_x, step)
x_up_neg = np.arange(min_x, max(roots), step)
x_up_pos = np.arange(max(roots), limit, step)

# plot the graph
plt.plot(x_down_pos, func(x_down_pos), 'b', 
         label='Descending values > 0')

plt.plot(x_up_pos, func(x_up_pos), 'r', 
         label='Ascending values > 0')

plt.plot(x_down_neg, func(x_down_neg), 'b', linestyle = 'dashed', 
         label='Descending values < 0')

plt.plot(x_up_neg, func(x_up_neg), 'r', linestyle = 'dashed', 
         label='Ascending values < 0')

if len(roots) == 2:
    plt.plot(roots[0], 0, 'yo', label=f'Roots ({roots[0]}, {roots[1]})')
    plt.plot(roots[1], 0, 'yo')
else:
    if roots[0] != None:
        plt.plot(roots[0], 0, 'ro')

plt.plot(min_x, min_y, 'gx', label=f'Extremum ({min_x}, {min_y})')

plt.legend()
plt.grid()
plt.show()