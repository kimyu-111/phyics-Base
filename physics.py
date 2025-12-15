from vpython import * #opip  install vpython , INCITING TRICKET
import math # sqrt 함수호출법 항상 생각
A= vector(1,-2,1)
B= vector(0.3,4,0)
C=A+B
print("|C|=",mag(C)) # math.sqrt(C.x**2+C.y**2+C.z**2)
print("C hat=",norm(C)) #unit vector C/mag(C)
C=3*A
print("3C=",C)
print(A*B)# CANT INTERPRET
print(dot(A,B)) # DOT PRODOCT
print(cross(A,B))# 벡터사이는 항상 콤마로 찍힌다. CROSS PRODOCT


# A Phyics Problem
# v=v0+at, in acceralation motion with steady speed, a=delta(v1-v0/delta t)
v=0+0.45*1.5
print(v)
# program 
x=0
y=0
t=0
dt=0.25
while(t<1.5):
    print("t=",t)
    t=t+dt
    