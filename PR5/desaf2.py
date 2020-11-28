import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=1800

R=2
d=10
pt=np.arange(0,t,h)
vx0=0
pla1 = plt.Circle((-d, 0), R,lw=1,alpha=0.5)
pla2 = plt.Circle((d, 0),R,lw=1,alpha=0.5)
plt.gcf().gca().add_artist(pla1)
plt.gcf().gca().add_artist(pla2)

plt.xlim([-50,50])
plt.ylim([-50,50])
while(vx0<1):
    ##MASA1
    x=10
    y=10
    vx=vx0
    vy=0
    px=[x]
    py=[y]

    #MASA2
    x_2=10
    y_2=15
    vx2=vx0
    vy2=0
    px2=[x_2]
    py2=[y_2]

    for t in pt:
        ##MASA1
        x1=x+d
        x2=x-d
        ax=-(x1)/((x1)**2+y**2)**(1.5)-(x2)/((x2)**2+y**2)**(1.5)
        ay=-y/((x1)**2+y**2)**(1.5)-(y/((x2)**2+y**2)**(1.5))
        vx = vx + ax*h;
        x = x + vx*h
        vy= vy + ay*h 
        y = y + vy*h

        ##MASA 2
        x11=x_2+d
        x22=x_2-d
        ax2=-(x11)/((x11)**2+y_2**2)**(1.5)-(x22)/((x22)**2+y_2**2)**(1.5)
        ay2=-y_2/((x11)**2+y_2**2)**(1.5)-(y_2/((x22)**2+y_2**2)**(1.5))
        vx2 = vx2 + ax2*h;
        x_2 = x_2 + vx2*h
        vy2= vy2 + ay2*h 
        y_2= y_2 + vy2*h
        
        if x>=50 or x_2>=50:
            break
        if y>=50 or y_2>=50:
            break
        if (((x1)**2 + (y)**2) <=R*R) or (((x11)**2 + (y_2)**2) <=R*R) :
            break
        if (((x2)**2 + (y)**2) <=R*R) or (((x22)**2 + (y_2)**2) <=R*R):
            break
        px.append(x)
        py.append(y)
        px2.append(x_2)
        py2.append(y_2)
    
    
        #pv.append([vx,vy])
        #pa.append([ax,ay])
    plt.plot(px,py,px2,py2)
    plt.grid(True)
    vx0+=0.05

plt.show()


