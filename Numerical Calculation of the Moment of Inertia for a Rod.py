from vpython import *
import math

M= 0.06
L=0.15
N=4
dL=L/N
dM=M/N
rstart=vector(dL/2,0,0)
n=0
mass=[]
while n<N:
  rp=rstart+n*vector(dL,0,0)
  rps=rps+[rp]
  n=n+1

r0=vector(0,0,0)

for rt in rps:
  r=rt-r0
  I=I+dM*mag(r)**2

print("I =",I,"kg*m^2")
Itheory=(1/3)*M*L**2
print("I theory =",Itheory,"kg*m^2")