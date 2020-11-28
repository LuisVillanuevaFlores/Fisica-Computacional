import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=2000

R=5
d=20
d2=20
pt=np.arange(0,t,h)
vx0=0
pla1 = plt.Circle((-d, 0), R,lw=1,alpha=0.4)
pla2 = plt.Circle((d, 0),R,lw=1,alpha=0.4)
pla3 = plt.Circle((0, d2), R,lw=1,alpha=0.4)
plt.gcf().gca().add_artist(pla1)
plt.gcf().gca().add_artist(pla2)
plt.gcf().gca().add_artist(pla3)

plt.xlim([-70,70])
plt.ylim([-70,70])
while(vx0<1):
    ##MASA1
    x=20
    y=30
    vx=vx0
    vy=0
    px=[x]
    py=[y]

    for t in pt:
        ##MASA1
        x1=x+d
        x2=x-d
        x3=x
        y2=y-d2
        ax=-(x1)/((x1)**2+y**2)**(1.5)-(x2)/((x2)**2+y**2)**(1.5)-x3/(x3**2+y2**2)**(1.5)
        ay=-y/((x1)**2+y**2)**(1.5)-(y/((x2)**2+y**2)**(1.5))-y2/(x3**2+y2**2)**(1.5)
        vx = vx + ax*h;
        x = x + vx*h
        vy= vy + ay*h 
        y = y + vy*h
        
        if x>=70:
            break
        if y>=70:
            break
        if (((x1)**2 + (y)**2) <=R*R):
            break
        if (((x2)**2 + (y)**2) <=R*R):
            break
        if(((x3)**2+(y2)**2) <=R*R):
            break
        px.append(x)
        py.append(y)
    
    
        #pv.append([vx,vy])
        #pa.append([ax,ay])
    plt.plot(px,py)
    plt.grid(True)
    vx0+=0.05

plt.show()




