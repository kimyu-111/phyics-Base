from vpython import *
import math
g1=graph(xtitle="t [s]",ytitle="px [kg*m/s]",width=450,height=200)
f1=gcurve(color=color.blue)
f2=gcurve(color=color.red)
f3=gcurve(color=color.yellow)
ft=gcurve(color=color.green)
m1 = sphere(pos=vector(0,0,0), radius=0.01, color=color.yellow, make_trail=True)
m2 = sphere(pos=vector(0.15,0,0), radius=0.02, color=color.cyan, make_trail=True)

m1.m = 0.05
m2.m = 0.078

m1.p = m1.m * vector(0,0.5,0)
m2.p = m2.m * vector(0,0,0)


rcom = (m1.pos * m1.m + m2.pos * m2.m) / (m1.m + m2.m)
com = sphere(pos=rcom, radius=0.005, color=color.red)

k = 10
L0 = 0.12
spring = helix(pos=m1.pos, axis=m2.pos-m1.pos, radius=0.005, thickness=0.005,make_trail=True)

t = 0
dt = 0.001

while t < 5:
    rate(100)
    

    L = m2.pos - m1.pos
    F = k * (mag(L) - L0) * norm(L)
    
    m1.p = m1.p + F * dt
    m2.p = m2.p - F * dt
    
    m1.pos = m1.pos + m1.p * dt / m1.m 
    m2.pos = m2.pos + m2.p * dt / m2.m
    

    rcom = (m1.pos * m1.m + m2.pos * m2.m) / (m1.m + m2.m)
    com.pos = rcom
    
    spring.pos = m1.pos
    spring.axis = L
    f1.plot(t,m1.p.x)
    f2.plot(t,m2.p.x)
    f3.plot(t,m1.p.x+m2.p.x)
    t = t + dt