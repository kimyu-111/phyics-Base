from vpython import *

g1 = graph(title="kinematics", xtitle="time[s]", ytitle="x[m]",width=500,height=250,fast=False)
f1 = gcurve(graph=g1, color=color.blue,markers=True)
x = 0     # m
v = 0.45  # m/s
t = 0     # s
dt = 0.01 

while t < 1.5:
    v = v + a * dt
    x = x + v * dt
    t = t + dt
    
    f1.plot(t, x)
    
# problem 
g1=graph(title="Kinematics",xtitle="time[s]",ytitle="x[m]",width=500,height=250,fast=False)
A1=gcurve(graph=g1, color=color.blue,markers=True)
B1=gcurve(graph=g1, color=color.red,markers=True)
t=0
dt=0.01
A_x=0.5
A_v=0.45
B_x=0
B_v=0
B_a=0.2
while (A_x>B_x): #이걸 만족할떄까지
  A_x=A_x+A_v*dt
  B_x=B_x+B_v*dt
  B_v=B_v+B_a*dt
  t=t+dt
  A1.plot(t,A_x)
  B1.plot(t,B_x)
print("B_x:",B_x)
print("t:",t)
