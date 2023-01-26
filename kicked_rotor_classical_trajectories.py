from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
#

dpi=2.0*pi

I_min = 0
theta_min = 0
number_of_trajectories =50 
number_of_points =1000 
theta_max = dpi    
I_max = dpi

Ks = [0.5, 3.5, 8]
for K in Ks:
    Kprime = round(K, 2)
    plt.axis([theta_min,theta_max,I_min,I_max])
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\mathcal{I}$')
    plt.title(f"K = {Kprime:.2f}")

    for i_traj in range(number_of_trajectories):
        theta=random.uniform(0,dpi)
        tab_theta=[]
        tab_I=[]
        I=random.uniform(0,dpi)
        for i in range(number_of_points):
            tab_theta.append(theta)
            tab_I.append(I)
      
            I = (I+Kprime*np.sin(theta))%dpi
            theta = (theta + I)%dpi
        plt.plot(tab_theta, tab_I, linestyle = 'None', marker = '.', markersize = 1)
    plt.savefig(f"{K}.jpg")
    plt.clf()
    plt.subplot(1, 1, 1)
    
