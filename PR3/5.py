import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
h=0.001
r=10
a=5

x=10*np.cos((np.pi)*2/3)
y=10*np.sin((np.pi)*2/4)
vx=-6*np.cos((np.pi)*2/3)
vy=6*np.sin((np.pi)*2/3)
print(vx,vy)
px=[]
py=[]
pv=[]
pa=[]
pt = np.arange(0,20,h)

for t in pt:
    ax=-(a*x/r)
    ay=-(a*y/r)
    x=x+vx*h
    y=y+vy*h
    vx=vx+ax*h
    vy=vy+ay*h
    px.append(x)
    py.append(y)
    pv.append([vx,vy])
    pa.append([ax,ay])

plt.subplot(2,2,1)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(pt,pv)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(pt,pa)    
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,py)    
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)

plt.show()


plt.plot(px,py)
plt.xlabel('x')
plt.ylabel('y')
plt.title('X-Y')
plt.grid(True)

plt.show()
