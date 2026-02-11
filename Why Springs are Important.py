from vpython import *
import math
g1=graph(xtitle='t[s]',ytitle='x[m]',width=500,height=250)
f1=gcurve(color=color.blue)
m=0.1
k=1000.5
g=vector(0,-9.8,0)
L0=0.15
theta=10*math.pi/180
top=sphere(pos=vector(0,L0,0),radius=0.004)
mass=sphere(pos=top.pos+L0*vector(-sin(theta),-cos(theta),0),radius=0.01,color=color.yellow,make_trail=True)
spring=helix(pos=top.pos,axis=mass.pos-top.pos,radius=0.005,thickness=0.002,color=color.cyan)

mass.p=m*vector(0.5,0,0.07)
t=0
dt=0.01


while t<1.5:
  rate(100)
  L = mass.pos-top.pos
  F=-k*(mag(L)-L0)*norm(L) +m*g
  mass.p=mass.p+F*dt
  mass.pos=mass.pos+mass.p*dt/m
  t=t+dt
  f1.plot(t,mass.pos.x)
  spring.axis=L
Tt=2*math.pi*sqrt(L0/mag(g))
print("T theory=",Tt,"s")
