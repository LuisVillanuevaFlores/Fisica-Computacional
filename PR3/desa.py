import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import matplotlib.animation as animation
from matplotlib import rcParams


plt.xlim(0,40)
plt.ylim(0,40)
g=10
r=0.005
vol=4/3*np.pi**3
C=0.5
A=pi*r**2
d=1000
m=vol*d
p=1.2

h=0.005
k=C*A*p/(2*m)

v=50

x=0
y=16

x_sin=0
y_sin=16

ax=0
ay=-10

ax_sin=0
ay_sin=-10

px=[]
py=[]

px_sin=[]
py_sin=[]

pv=[]
pv_sin=[]
pa=[]
pa_sin=[]
vx=14
vy=0
vx_sin=14
vy_sin=0
redDot, =plt.plot([x_sin], [y_sin], 'ro')

t=0

def animate(i):
    global x,y,x_sin,y_sin,vx_sin,vy_sin,vx,vy,ax_sin,ay_sin,ax,ay,v
    
    if y_sin>=0:
        x_sin=x_sin+vx_sin*h
        y_sin=y_sin+vy_sin*h
        vx_sin=vx_sin+ax_sin*h
        vy_sin=vy_sin+ay_sin*h
        px_sin.append(x_sin)
        py_sin.append(y_sin)
        pv_sin.append([vx_sin,vy_sin])
            
            

    if y>=0:
        x=x+vx*h
        y=y+vy*h
        redDot.set_data(x,y)
        vx=vx+ax*h
        vy=vy+ay*h
        ax=-k*v*vx
        ay=-g-k*v*vy
        px.append(x)
        py.append(y)
        pv.append([vx,vy])
            
        pa.append([ax,ay])
        v=np.sqrt(vx**2+vy**2)

            
    return redDot,
        
        

myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0,1000,h),\
                                      interval=50, blit=True, repeat=True)

plt.show()

