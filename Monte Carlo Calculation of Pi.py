from vpython import *
import math

g1= graph(width=400,height=380,ymax=1.1,xmax=1.1)
fq=gdots(color=color.red)
fo=gdots(color=color.blue)

N=10000
n=0
cin=0

while n<N:
  rate(5000)
  r=vector(random(),random(),0)
  if mag(r)<1:
    cin=cin+1
    fq.plot(r.x,r.y)
  else:
    fo.plot(r.x,r.y)

n=n+1

tpi=cin*4/n
print("pi = ",tpi)