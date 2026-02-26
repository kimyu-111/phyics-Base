from vpython import *

# 1. 환경 설정
N = 10000
n = 0
dr = 0.2
I = 0
R = 1
M = 7
dm = M / N
rp = []


scene.width = 600
scene.height = 600

print("시뮬레이션 시작 (점 1만 개 생성 중...)")


while n < N:
    
    if n % 100 == 0:
        rate(1000) 
        
    rr = R * (1 + dr) * vector((1 - 2*random()), (1 - 2*random()), (1 - 2*random()))
    
   
    if (1 - dr) < mag(rr) < (1 + dr):
       
        sphere(pos=rr, radius=0.02, color=color.cyan, opacity=0.5)
        
        
        rp.append(rr) 
        n = n + 1


for rt in rp:
   
    dI = dm * (rt.x**2 + rt.y**2)
    I = I + dI

print("\n--- 결과 ---")
print(f"시뮬레이션 I = {I:.4f} kg*m^2")


R_in = R * (1 - dr)   # 0.8
R_out = R * (1 + dr)  # 1.2
It_thick = (2/5) * M * (R_out**5 - R_in**5) / (R_out**3 - R_in**3)

print(f"이론값 (두꺼운 껍질) It = {It_thick:.4f} kg*m^2")

It_thin = (2/3) * M * R**2
print(f"이론값 (얇은 껍질)   = {It_thin:.4f} kg*m^2")

# 오차율 계산
error_rate = abs(I - It_thick) / It_thick * 100
print(f"오차율 = {error_rate:.2f}%")