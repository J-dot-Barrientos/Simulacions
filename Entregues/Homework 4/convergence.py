# -*- coding: utf-8 -*-
"""Convergence.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14Gxy-XcuCcTPO3wB-MpUJ8WRRiijs2Eg

# **Calculation of $\frac{4}{3}\,\pi$ using Markov chain Monte Carlo**

The algorithm is a modification of the Markov Chain example to aproximate the volume of a unite sphere instead of the area of a unite circle.
"""

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# Create output file with data
f = open('MCVolume.dat','w')

# initial and maximum number of random points
max_random_points = 100000
min_random_points = 100

#step for iteration
step = 100

# input total number of random points
delta = float(input("\nEnter size of jump (example 0.3): \n>"))

#Loop over number of random points
total_random_points=min_random_points
while (total_random_points <= max_random_points):

    # Init counter of number of points inside unit sphere and inside unit cube
    inside_sphere = 0
    inside_cube = 0
    outside = 0

    #Create list to save x,y of points inside sphere to be shown in the graph
    xs = []
    ys = []
    zs = []

    #Create list to save x,y of points inside cube but outside sphere to be shown in the graph
    xc = []
    yc = []
    zc = []

    #---------------------------------------------------
    #Calculation

    #Initial position
    x=1.0
    y=1.0
    z=1.0

    while (inside_cube<total_random_points):

        #generate a random jump
        del_x = np.random.uniform(-delta, delta)
        del_y = np.random.uniform(-delta, delta)
        del_z = np.random.uniform(-delta, delta)

        #check new positions and if they are outside the sphere make zero jump
        if abs(x+del_x) > 1.0 or abs(y+del_y) > 1.0 or abs(z+del_z) > 1.0:
            outside = outside +1
            del_x = 0.0
            del_y = 0.0
            del_z = 0.0

        #Update number of points inside cube and update the new starting position
        inside_cube = inside_cube +1
        x = x + del_x
        y = y + del_y
        z = z + del_z

        #check whether it is inside sphere (count and save for representation)
        if x**2 + y**2 + z**2 <= 1.0:
            inside_sphere = inside_sphere +1
            xs.append(x)
            ys.append(y)
            zs.append(z)
        else:
            xc.append(x)
            yc.append(y)
            zc.append(z)

    #---------------------------------------------------

    # Statistics

    # Number of points inside sphere as compared with total
    sphere_ratio = inside_sphere /  inside_cube

    #Number of points inside sphere as compared with those inside the total cube with volume 8.0
    fourthirdspi_approx = 8.0*sphere_ratio

    #save data to a file
    print(f'{total_random_points} {fourthirdspi_approx}\n')
    f.write(f'{total_random_points} {fourthirdspi_approx}\n')

    #update
    total_random_points=total_random_points + step
