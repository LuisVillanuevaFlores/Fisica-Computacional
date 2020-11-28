import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
plt.xlim(0,20)
plt.ylim(0,10)
h=0.005
redDot, = plt.plot([0], [0], 'ro')
x=0
y=0
vx=1
vy=4

def animate(i):
    global x,y,vx,vy

    x=x+vx*h
    y=y+vy*h
    redDot.set_data(x, y)
    if(y>=10 or y<=0):
        vy=vy*-1
    if(x>=20 or x<=0):
        vx=vx*-1

    
    return redDot,


myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0,100,h),\
                                      interval=5, blit=True, repeat=False)


plt.show()
