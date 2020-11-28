import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import rcParams

fig, ax = plt.subplots()
k=0.1
m=0.2
f0=0.01
f1=0
c=0.05
w=0.3

h=0.01
t=100
ax=0
ax1=0
x=-1
x1=-1
vx=1
vx1=1
px=[]
px1=[]

pv=[]
pv1=[]
pa=[]
pa1=[]


pt=np.arange(0,t,h)
ax=-k*x/m-c*vx/m+f0*np.cos(w*t)/m
vx=vx+ax*h/2

ax1=-k*x1/m-c*vx1/m+f1*np.cos(w*t)/m
vx1=vx1+ax1*h/2
j=0

for t in pt:
    ax=-k*x/m-c*vx/m+f0*np.cos(w*t)/m
    vx=vx+ax*h
    x=x+vx*h
    
    ax1=-k*x1/m-c*vx1/m+f1*np.cos(w*t)/m
    vx1=vx1+ax1*h
    x1=x1+vx1*h
    
  
    px.append(x)
    pv.append(vx)
    pa.append(ax)

    px1.append(x1)
    pv1.append(vx1)
    pa1.append(ax1)







  
plt.subplot(2,2,1)
plt.plot(pt,px,pt,px1)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('X-T')
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(pt,pv,pt,pv1)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('V-T')
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(pt,pa,pt,pa1)
plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.title('A-T')
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(px,pv,px,pv1)
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)

'''
plt.subplot(2,3,5)
plt.plot(px,pu,px,pk,px,pe)
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)

plt.show()
'''
'''
fig = plt.figure()
ax=plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter3D(px,pv,pt,c=pt)

plt.show()


fig1 = plt.figure()
ax1=plt.axes(projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.scatter3D(px1,pv1,pt,c=pt)

plt.show()
'''
fig = plt.figure()
#plt.gcf().suptitle(exercise+": v - x - t", fontsize=16)
ax = fig.gca(projection='3d')
ax.plot(pv,px,pt)
ax.plot(pv1,px1,pt)
plt.xlabel('velocidad')
plt.ylabel('espacio')
ax.set_zlabel('tiempo')
plt.grid(True)
plt.show()

