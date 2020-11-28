import matplotlib.pyplot as plt
import numpy as np

k=0.1
m=0.2
f0=0
c=0
w=0

h=0.001
t=20
ax=0
ay=0
x=2
y=0
vx=0
vy=0
px=[]
py=[]
pv=[]
pa=[]


pt=np.arange(0,t,h)

ax=-k*x/m-c*vx/m+f0*np.cos(w*t)/m
vx=vx+ax*h/2
for t in pt:
    ax=-k*x/m-c*vx/m+f0*np.cos(w*t)/m
    ay=-k*y/m-c*vy/m+f0*np.cos(w*t)/m
    vx=vx+ax*h
    #vy=vy+ay*h
    x=x+vx*h
    #y=y+vy*h
    px.append(x)
    #py.append(y)
    pv.append(vx)
    pa.append(ax)

plt.subplot(2,2,1)
plt.plot(pt,px)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('X-T')
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(pt,pv)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('V-T')
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.title('A-T')
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(px,pv)
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)

plt.show()
