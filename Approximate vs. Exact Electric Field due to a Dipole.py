from vpython import *
import math

def E(rq,ro,q):
  k=9e9
  r=ro-rq
  Etemp=k*q*norm(r)/mag(r)**2
  return(Etemp)

q = 3e-9
s = 0.001
rqn=vector(-s/2,0,0)
rqp=vector(s/2,0,0)
g1=graph(xtitle="r [m]",ytitle="E [N/C]",width=500,height=200)
fe=gcurve(color=color.blue,label="Exact")
fa=gcurve(color=color.red,label="Far Field")

ro= vector(2*s,0,0)
dr=vector(s/10,0,0)
k=9e9
while ro.x < 3*s:
  #rn=ro-rqn
  #rp=ro-rqp
  Ee=E(rqn,ro,-q) + E(rqp,ro,q)
  Ea= k*2*q*s/mag(ro)**3
  fe.plot(ro.x,mag(Ee))
  fa.plot(ro.x,Ea)
  ro=ro+dr
  rate(30)