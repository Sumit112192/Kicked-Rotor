import numpy as np
import random
import matplotlib.pyplot as plt
from math import *

dpi = 2*pi

K =5
no_of_points = 1000
no_of_trajectories = 1000





totalTrajectory = []
for trajectory in range(no_of_trajectories):
    theta_i = random.uniform(0, dpi)
    L_i = random.uniform(0, dpi)
    #L_0 = L_i
    DeltaL2 = []
    for i in range(no_of_points):
        L_f = L_i + K*np.sin(theta_i)
        theta_f = (theta_i + L_f)%(dpi)
        deltaL2 = (L_f )**2
        DeltaL2.append(deltaL2)
        L_i = L_f
        theta_i = theta_f
    totalTrajectory.append(DeltaL2)
meanL2 = np.zeros(1000)
for i in range(no_of_trajectories):
    for j in range(no_of_points):
        meanL2[j] += totalTrajectory[i][j]

for i in range(1000):
    meanL2[i] = meanL2[i]/no_of_trajectories

        

plt.xlabel("Number of kicks(N)")
plt.ylabel(r"$<L^2>$")
plt.title("Classical Kicked Rotor")
plt.plot(range(1, 1001), meanL2)
plt.savefig("MeanL2.jpg")
plt.show()
