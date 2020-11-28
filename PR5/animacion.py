import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

#DATOS INICIALES

l_line=300
        
h=0.01
t=2000

R=2
d=20
b=20
pt=np.arange(0,t,h)
##DIBUJO DE PLANETAS##
pla1 = plt.Circle((-d, 0), R,lw=1,alpha=0.4)
pla2 = plt.Circle((d, 0),R,lw=1,alpha=0.4)
pla3 = plt.Circle((0, b), R,lw=1,alpha=0.4)

#LIMITES
plt.xlim([-70,70])
plt.ylim([-70,70])

#ALGORITMO EN SI DE GRAVITACION

def gravi(x,y,velocidad):
        ##MASA1
        x=x
        y=y
        vx=velocidad[0]
        vy=velocidad[1]
        px=[x]
        py=[y]

        for t in pt:
            ##MASA1
            x1=x+d
            x2=x-d
            x3=x
            y2=y-b
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
            
        return [px,py]
        
'''
plt.gcf().gca().add_artist(pla1)
plt.gcf().gca().add_artist(pla2)
plt.gcf().gca().add_artist(pla3)
'''


class punto():
    def __init__(self,x,y,velocidad):
        self.velocidad=velocidad
        self.pe=gravi(x,y,velocidad)
    
    def dibujar(t):
        t=int(t)
        if(t<len(self.pe[0])):
            plt.plot(self.pe[t][0],self.pe[t][1],'ro',alpha=0.5)

    

def init():
    global puntos
    puntos= [punto(20,30,[i,0])for i in np.arange(0,1,0.1)]


def graf(t):
    plt.gca().clear()
    plt.gcf().gca().add_artist(pla1)
    plt.gcf().gca().add_artist(pla2)
    plt.gcf().gca().add_artist(pla3)
    plt.gca().axis('equal')
    for i in puntos:
        i.dibujar(t)


ani= animation.FuncAnimation(plt.gcf(),graf,pt,init_func=init,interval=1)


try:
    plt.show()
except :
    print("TERMINO")



