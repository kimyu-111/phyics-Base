from vpython import *
import math

def E(rq,ro,q):
  K=9e9
  r=ro-rq
  Etemp=K*q*norm(r)/mag(r)**2
  return(Etemp)

q=3e-9
s=0.001
q1=sphere(pos=vector(s/2,0,0),radius=s/2,color=color.red)
q2=sphere(pos=vector(-s/2,0,0),radius=s/2,color=color.cyan)

N=16
theta=0
dtheta=2*math.pi/N
R=0.005
Escale=2e-8
Emax=5e5
while theta<2*math.pi :
  ro=R*vector(cos(theta),sin(theta),0)
  Ed=E(q1.pos,ro,q)+E(q2.pos,ro,-q)
  E_mag = mag(Ed)
  intensity = min(E_mag / Emax, 1.0) 
  arrow_color = vector(intensity, 0, 1 - intensity)
  arrow(pos=ro,axis=Escale*Ed,color=arrow_color)
  theta=theta+dtheta

theta=0
while theta<2*math.pi :
  ro=R*vector(cos(theta),0,sin(theta))
  Ed=E(q1.pos,ro,q)+E(q2.pos,ro,-q)
  E_mag = mag(Ed)
  intensity = min(E_mag / Emax, 1.0) 
  arrow_color = vector(intensity, 0, 1 - intensity)
  arrow(pos=ro,axis=Escale*Ed,color=arrow_color)
  theta=theta+dtheta

while True:
  rate(10)