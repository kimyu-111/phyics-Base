from vpython import *
import math

M=0.05
L=0.1

x=0
dx=0.0001

I=0

while x<L:
  dI=M*(x**2)*dx/L
  I=I+dI
  x=x+dx
print("I =",I,"kg*m^2")
It=(1/3)*M*L**2
print("It =",It,"kg/m^2")

x=0
A=0
while x<1:
  dA=math.sin(math.pi*x)**2
  A=A+dA
  x=x+dx
print("A=",A)