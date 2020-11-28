import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
h=0.01
r=8
a=2

x=8*np.cos(pi/4)
y=8*np.sin(pi/4)

vx=-4*np.cos(pi/4)
vy=4*np.sin(pi/4)
print(vx,vy)
ax=0
ay=0
px=[]
py=[]
pv=[]
pa=[]
p_sim=[]
pt = np.arange(0,15,h)

for t in pt:
    ax=-(a*x/r)
    ay=-(a*y/r)
    x=x+vx*h
    y=y+vy*h
    vx=vx+ax*h
    vy=vy+ay*h
    v_resu=np.sqrt(vx**2+vy**2)
    px.append(x)
    py.append(y)
    pv.append([vx,vy])
    pa.append([ax,ay])
    p_sim.append(v_resu)


for i in p_sim:
    print(i)

print(pv)
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
plt.plot(pt,p_sim)    
plt.xlabel('Tiempo')
plt.ylabel('V')
plt.title('x-y')
plt.grid(True)


plt.show()

plt.plot(px,py)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.show()
