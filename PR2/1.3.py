import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
h=0.01
x=10
y=10
z=10
vx=0
vy=0
vz=4
ax=0
ay=-10
az=0
t=0
px=[]
py=[]
pz=[]
pv=[]
pa=[]
ante=0
while(True):
    t=t+h
    ante=y
    px.append(x)
    py.append(y)
    pz.append(z)
    pa.append([ax,ay,az])
    pv.append([vx,vy,vz])
    x=x+vx*h
    y=y+vy*h
    z=z+vz*h
    vx=vx+ax*h
    vy=vy+ay*h
    vz=vz+az*h
    if(y<0):
        break

print("tiempo: ",t)
print("coordenadas: ", px[len(px)-1],py[len(py)-1],pz[len(pz)-1])
pt=np.arange(0,t-h,h)
ax=plt.axes(projection='3d')
ax.set_xlabel('Espacio x')
ax.set_ylabel('Espacio y')
ax.set_zlabel('Espacio z')

ax.scatter3D(px,py,pz,c=pt)
plt.show()
