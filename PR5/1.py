import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=1200


R=2


pt=np.arange(0,t,h)
vx0=0
pla1 = plt.Circle((0, 0), R,lw=1,alpha=0.4)
plt.gcf().gca().add_artist(pla1)

while(vx0<1):
    x=3
    y=4
    vx=vx0
    vy=0
    ax=0
    ay=0
    px=[x]
    py=[y]
   
    for t in pt:
        ax=-x/(x**2 + y**2)**(1.5)
        ay=-y/(x**2 + y**2)**(1.5)
        vx=vx+ax*h
        vy=vy+ay*h
        x=x+vx*h
        y=y+vy*h
        
        if x>=50:
            break
        
        if((x)**2 + (y)**2)<=R*R:
            break
        px.append(x)
        py.append(y)
    #pr.append(px,py)
    plt.plot(px,py)
    plt.grid(True)
    vx0+=0.05
'''
def chart(t):
    plt.gca().clear()
    plt.gca().add_patch(mp.Rectangle((-ancho, -largo), 2*ancho, 2*largo, fill=None,alpha=1,lw=2))
    plt.gca().add_artist(pla1)
    plt.gca().axis('equal')
    plt.plot(px[t],py[t])

ani= animation.FuncAnimation(plt.gcf(),chart,pt,interval=1)
'''
plt.show()


