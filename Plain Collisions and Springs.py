from vpython import *
import math
g1=graph(xtitle="t[s]",ytitle="px",width=450,height=200)
fA=gcurve(color=color.blue)
fB=gcurve(color=color.red)
fT=gcurve()
ballA=sphere(pos=vector(-.4,.01,0),radius=0.02,color=color.yellow,make_trail=True)
ballB=sphere(pos=vector(0,0,0),radius=0.017,color=color.cyan,make_trail=True)
ballA.m=0.1
ballB.m=.1
ballA.p=ballA.m*vector(0.4,0,0)
ballB.p=ballB.m*vector(0.0,0,0)

k1=500
k2=50
RA=ballA.radius
RB=ballB.radius

t=0
dt=0.001

rold=ballB.pos-ballA.pos
while t<.6:
  rate(1000)
  FA=vector(0,0,0)
  FB=vector(0,0,0)
  r=ballB.pos-ballA.pos
  if mag(r)<(RA+RB):
    if mag(r)<=mag(rold):
      FA=k1*(mag(r)-RA-RB)*norm(r)
    else :
      FA=k2*(mag(r)-RA-RB)*norm(r)
    FB=-FA

    #FA=-.1*norm(r)
    #FB=-FA
  ballA.p= ballA.p+FA*dt
  ballB.p=ballB.p+FB*dt
  ballA.pos=ballA.pos +ballA.p*dt/ballA.m 
  ballB.pos=ballB.pos+ballB.p*dt/ballB.m
  rold=r
  t=t+dt
  KA=mag(ballA.p)**2/(2*ballA.m)
  KB=mag(ballB.p)**2/(2*ballB.m)
  if contact:
    E=KA+KB+.5*k*(mag(r)-RA-RB)**2
  else :
    E=KA+KB
  fA.plot(t,ballA.p.x)
  fB.plot(t,ballB.p.x)
  fT.plot(t,ballA.p.x+ballB.p.x)