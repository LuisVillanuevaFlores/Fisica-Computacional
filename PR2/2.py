import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=0
y=0
vx=2
vy=3
ax=-10
ay=0
pt = np.arange(0,900,h)
px=[]
py=[]
pv=[]
pa=[]
for t in pt:
    x=x+vx*h
    y=y+vy*h
    vx=vx+ax*h
    vy=vy+ay*h
    px.append(x)
    py.append(y)
    pv.append([vx,vy])
    pa.append([ax,ay])


plt.subplot(2,2,1)
plt.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(pt,pv)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)



plt.subplot(2,2,3)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)



plt.subplot(2,2,4)
plt.plot(px,py)    
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('v-x')
plt.grid(True)

plt.show()
