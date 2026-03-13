from vpython import *
import math

k=9e9
L=0.1
Q=6e-6

N=50
dQ=Q/N
dL=L/N
n=0
rq0=vector(0,-L/2+dL/2,0)
rstart=0.01
ro=vector(rstart,rstart,0)
while n<N:
  rq=rq0+n*vector(0,dL,0)
  r=ro-rq
  dE=k*dQ*norm(rq)/mag(rq)**2
  E=E+dE
  sphere(pos=rq,radius=L/20,color=color.yellow)
  n=n+1
Escale=2e-9
Earrow=arrow(pos=ro,axis=E*Escale,color=color.cyan)
print("E numerical =",E,"V/m")
Ec1=k*Q/(rstart*sqrt(rstart**2+(L/2)**2))
Ec2=k*2*Q/(L*rstart)
print("Ec1 =",)