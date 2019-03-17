# -*- coding: utf-8 -*-

from pair_correlation import pair_correlation


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#------------------uncorrelated data-------------------- #
p = 0, 0, 20, 20

# uncorrelated coordinates
x = np.random.uniform(low=0, high=20, size=2000)
y = np.random.uniform(low=0, high=20, size=2000)

Arr = np.column_stack((x,y))

rmax = 5
dr = 0.1

g_random, radius_1 = pair_correlation(Arr, Arr, p, rmax, dr)

fig = plt.figure(figsize=(9,9/1.618))

plt.title('RANDOM')

plt.plot(radius_1, g_random, 'r.--', label='uncorrelated')

plt.xlim(0, rmax * 1.1)
plt.ylim(0, max(g_random) * 1.1)

plt.xlabel('r')
plt.ylabel('g(r)')

plt.legend()

plt.savefig('uncorrelated example.png')

#------------------my data-------------------- #

# the largest radius to analyze
rmax = 400
dr = 20

# calculate the radius
edge = np.arange(0., rmax + 1.1 * dr, dr)
radius = (edge[:-1] + edge[1:]) / 2

g_r12 = np.zeros(len(radius))
g_r21 = np.zeros(len(radius))

p = x, y, w, h = 8832, 16080, 12528, 10656

df1 = pd.read_csv('./20180503_8b_cr cluster center.csv', sep = ',')
df2 = pd.read_csv('./20180503_8c_cr cluster center.csv', sep = ',')

Arr1= df1[['x_median','y_median']].values
Arr2= df2[['x_median','y_median']].values

# in reference to color 1
g_r12 = g_r12 + pair_correlation(Arr1, Arr2, p, rmax, dr)[0]

# in reference to color 2
g_r21 = g_r21 + pair_correlation(Arr2, Arr1, p, rmax, dr)[0]

fig = plt.figure(figsize=(9,9/1.618))

plt.title('MY DATA')

plt.plot(radius, g_r12, 'rx--', label='g12(r)')
plt.plot(radius, g_r21, 'kx--', label='g21(r)')

plt.xlim(0, rmax * 1.1)
plt.ylim(0, max(max(g_r12), max(g_r21)) * 1.1)

plt.xlabel('r / nm')
plt.ylabel('g(r)')

plt.legend()

plt.savefig('correlated example.png')

plt.show()
