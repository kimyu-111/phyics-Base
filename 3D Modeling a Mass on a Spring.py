from vpython import *
m=0.1
k=10.5
g=vector(0,-9.8,0)
L0=0.07
top=sphere(pos=vector(0,L0,0),radius=0.004)
mass=sphere(pos=top.pos-vector(.3*L0,L0,0),radius=0.01,color=color.yellow,make_trail=True)
spring=helix(pos=top.pos,axis=mass.pos-top.pos,radius=0.005,thickness=0.002,color=color.cyan)

mass.p=m*vector(0.5,0,0.07)
t=0
dt=0.01


while t<10:
  rate(100)
  L = mass.pos-top.pos
  F=-k*(mag(L)-L0)*norm(L) +m*g
  mass.p=mass.p+F*dt
  mass.pos=mass.pos+mass.p*dt/m
  t=t+dt
  spring.axis=L
