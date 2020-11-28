import matplotlib.pyplot as plt
import numpy as np
from numpy import pi


h=0.001
v=10
x=0
y=0
k=0
vx=v*np.cos((pi/6))
vy=v*np.sin((pi/6))
px=[]
py=[]
pv1=[]
ax=0
ay=-10

x2=0
y2=0
vx2=v*np.cos((pi/3))
vy2=v*np.sin((pi/3))
px2=[]
py2=[]
pv2=[]
ax2=0
ay2=-10

while(True):

    if y2<0:
        break

    if y2>=0:
        x2=x2+vx2*h
        y2=y2+vy2*h
        px2.append(x2)
        py2.append(y2)
        vx2=vx2+ax2*h
        vy2=vy2+ay2*h
        pv2.append([vx2,vy2])

    if y>=0:
        x=x+vx*h
        y=y+vy*h
        px.append(x)
        py.append(y)
        vx=vx+ax*h
        vy=vy+ay*h
        pv1.append([vx,vy])
        

    

    
print(px[len(px)-1],py[len(py)-1])
print(px2[len(px2)-1],py2[len(py2)-1])


plt.plot(px,py,px2,py2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')

plt.show()
