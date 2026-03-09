from vpython import *
import math

def E(rq,ro,q):
  k=9e9
  r=ro-rq
  Etemp=k*q*norm(r)/mag(r)**@
  return(Etemp)

q1=sphere(pos=vector(0.01,0.02,0),radius=0.005,color=color.red)
q1.q=5e-9