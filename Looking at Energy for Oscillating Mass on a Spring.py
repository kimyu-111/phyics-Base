from vpython import *
import math

# 1. 그래프 설정 (막대 그래프용)
g1 = graph(xtitle='Energy Type', ytitle='E [J]', width=400, height=300)

# 막대 너비(delta)를 설정해주면 보기에 더 좋습니다.
fK = gvbars(color=color.red, label='Kinetic (K)', delta=0.5)
fUg = gvbars(color=color.green, label='Potential (Ug)', delta=0.5)
fUk = gvbars(color=color.blue, label='Elastic (Uk)', delta=0.5)
fE = gvbars(color=color.black, label="Total (E)", delta=0.5) # 점(dot) 대신 막대로 통일했습니다

m = 0.1
k = 100.5
g = vector(0, -9.8, 0)
L0 = 0.15
C = 0 # 1.5*0 이라 그냥 0으로 씀
theta = 10 * math.pi / 180

top = sphere(pos=vector(0, L0, 0), radius=0.004)
mass = sphere(pos=top.pos + L0 * vector(-sin(theta), -cos(theta), 0), radius=0.01, color=color.yellow, make_trail=True)
spring = helix(pos=top.pos, axis=mass.pos-top.pos, radius=0.005, thickness=0.002, color=color.cyan)

mass.p = m * vector(0.5, 0, 0.07)
t = 0
dt = 0.001 # 0.01은 물리적으로 불안정할 수 있어 조금 줄였습니다

while t < 5:
    rate(100)
    
    # 1. 물리 계산
    L = mass.pos - top.pos
    F = -k * (mag(L) - L0) * norm(L) + m * g - C * mass.p
    mass.p = mass.p + F * dt
    mass.pos = mass.pos + mass.p * dt / m
    t = t + dt
    
    # 2. 에너지 계산
    K = mag(mass.p)**2 / (2 * m)
    Ug = m * 9.8 * mass.pos.y  # 위치 에너지 (높이에 따라 -값이 나올 수 있음)
    Uk = 0.5 * k * (mag(L) - L0)**2
    E = K + Ug + Uk
    
    # 3. [핵심 수정] 그래프 데이터 업데이트
    # plot()을 쓰지 않고 data 속성을 통째로 바꿔야 잔상이 안 남고 움직입니다.
    # 형식은 반드시 [[x, y]] 리스트 안의 리스트여야 합니다.
    fK.data = [[1, K]]
    fUg.data = [[2, Ug]]
    fUk.data = [[3, Uk]]   # [수정] 아까 K로 잘못 적으신 부분 수정 (Uk)
    fE.data = [[4, E]]
    
    spring.axis = L

Tt = 2 * math.pi * sqrt(L0 / 9.8)
print("T theory =", Tt, "s")kiomyo