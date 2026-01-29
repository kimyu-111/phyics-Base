from vpython import *
g1=graph(xtitle="r [m]",ytitle="E [J]", width=500, height=250)
fk=gcurve(color=color.red,label="KE",dot=True)
FU=gcurve(color=color.green,label="U",dot=True)
FE=gcurve(color=color.blue,label="E",dot=True)
G=6.67e-11
ME=5.97e24
RE=6.37e6


earth=sphere(pos=vector(0,0,0),radius=RE,texture=textures.earth)
craft=sphere(pos=vector(2*RE,0,0),radius=RE/30,color=color.yellow,make_trail=True)

craft.m=1000
craft.p=vector(0,5500,0)*craft.m

t=0
dt=11

while t<30000:
  rate(1000)
  r=craft.pos-earth.pos
  F=-G*ME*craft.m*norm(r)/mag(r)**2
  craft.p=craft.p+F*dt
  craft.pos=craft.pos + craft.p*dt/craft.m 
  t=t + dt
  K=mag(craft.p)**2/(2*craft.m)
  U=-G*ME*craft.m/mag(r)
  E=K+U
  fk.plot(mag(r),K)
  FU.plot(mag(r),U)
  FE.plot(mag(r),E)