import matplotlib.pyplot as plt
import numpy as np

h=0.01
x=0
y=0
vx=1
vy=3
ax=0
ay=-10
t=0
px=[]
py=[]
pv=[]
pa=[]

while(True):
    t=t+h
    px.append(x)
    py.append(y)
    pa.append([ax,ay])
    pv.append([vx,vy])
    x=x+vx*h
    y=y+vy*h
    vx=vx+ax*h
    vy=vy+ay*h
    if(y<0):
        break
    

pt=np.arange(0,t-h,h)

plt.plot(px,py)    
plt.xlabel('espacio x ')
plt.ylabel('espacio y')
plt.title('x-y')
plt.grid(True)

plt.show()

