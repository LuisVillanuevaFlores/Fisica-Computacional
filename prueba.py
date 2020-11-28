import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

v = 10

h = 0.001
pos = [[0],[0]]
k = 0
angulo = np.deg2rad(60)
print(angulo)
velocidad = [[v*np.cos(angulo)], [v*np.sin(angulo)]]
a = [0, -10]

pos2 = [[0],[0]]
angulo = np.deg2rad(30)
print(angulo)
velocidad2 = [[v*np.cos(angulo)], [v*np.sin(angulo)]]
a2 = [0, -10]

while True:

    if(pos[1][-1] < 0):
        break
    
    if(pos2[1][-1] >= 0):
        pos2[0].append(pos2[0][-1] + velocidad2[0][-1]*h)
        pos2[1].append(pos2[1][-1] + velocidad2[1][-1]*h)

        velocidad2[0].append(velocidad2[0][-1] + a2[0]*h)
        velocidad2[1].append(velocidad2[1][-1] + a2[1]*h)

    if(pos[1][-1] >= 0):
        pos[0].append(pos[0][-1] + velocidad[0][-1]*h)
        pos[1].append(pos[1][-1] + velocidad[1][-1]*h)

        velocidad[0].append(velocidad[0][-1] + a[0]*h)
        velocidad[1].append(velocidad[1][-1] + a[1]*h)

    

print(pos[0][-1])

plt.plot(pos[0],pos[1])
plt.plot(pos2[0],pos2[1])
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()
