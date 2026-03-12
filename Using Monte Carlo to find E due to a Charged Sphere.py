from vpython import *
import math

def E(rq,ro,q):
  k=9e9
  r=ro-rq
  Etemp=k*q*norm(r)/mag(r)**2
  return (Etemp)

Q=3e-6
R=0.01
N=1000
n=0
dQ=Q/N
k=9e9
ro=vector(2*R,0,0)
Es=vector(0,0,0)
dr=R/20
while n<N:
  rate(30)
  rt=R*vector(1-2*random(),1-2*random(),1-2*random())
  if mag(rt)<=R and mag(rt)>(R-dr):
    sphere(pos=rt,radius=R/50)
    Es=Es+E(rt,ro,dQ)
    n=n+1
print("E due ro sphere=",Es,"N/C")
Et=k*Q/mag(ro)