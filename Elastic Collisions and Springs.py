from vpython import *
import math
g1=graph(xtitle="t[s]",ytitle="K [J]")
fA=gcurve(color=color.blue)
fB=gcurve(color=color.red)
fT=gcurve()
ballA=sphere(pos=vector(-.1,.01,0),radius=0.02,color=color.yellow,make_trail=True)
ballB=sphere(pos=vector(0,0,0),radius=0.017,color=color.cyan,make_trail=True)
ballA.m=0.1
ballB.m=0.07
ballA.p=ballA.m*vector(0.4,0,0)
ballB.p=ballB.m*vector(0.04,0,0)

k=500
RA=ballA.radius
RB=ballB.radius

t=0
dt=0.001

while t<1.6:
  rate(1000)
  FA=vector(0,0,0)
  FB=vector(0,0,0)
  r=ballB.pos-ballA.pos
  if mag(r)<(RA+RB):
    FA=k*(mag(r)-RA-RB)*norm(r)
    FB=-FA

    #FA=-.1*norm(r)
    #FB=-FA
  ballA.p= ballA.p+FA*dt
  ballB.p=ballB.p+FB*dt
  ballA.pos=ballA.pos +ballA.p*dt/ballA.m 
  ballB.pos=ballB.pos+ballB.p*dt/ballB.m
  t=t+dt
  KA=mag(ballA.p)**2/(2*ballA.m)
  KB=mag(ballB.p)**2/(2*ballB.m)
  fA.plot(t,KA)
  fB.plot(t,KB)
  fT.plot(t,KA+KB)