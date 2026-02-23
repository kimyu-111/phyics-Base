import numpy as np
import matplotlib.pyplot as plt

def is_inside(p, a, b, c):
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    cp1 = cross_product(a, b, p)
    cp2 = cross_product(b, c, p)
    cp3 = cross_product(c, a, p)

   
    return (cp1 >= 0 and cp2 >= 0 and cp3 >= 0) or (cp1 <= 0 and cp2 <= 0 and cp3 <= 0)


grid_size = 50

num_samples = 10000 



triangle = np.random.uniform(0, grid_size, (3, 2))


points = np.random.uniform(0, grid_size, (num_samples, 2))


inside_points = []
outside_points = []


inside_count = 0
for point in points:
    if is_inside(point, triangle[0], triangle[1], triangle[2]):
        inside_points.append(point)
        inside_count += 1
    else:
        outside_points.append(point)


inside_points = np.array(inside_points)
outside_points = np.array(outside_points)

rectangle_area = grid_size * grid_size
estimated_area = (inside_count / num_samples) * rectangle_area

def true_area(t):
    return 0.5 * abs(t[0,0]*t[1,1] + t[1,0]*t[2,1] + t[2,0]*t[0,1] - (t[1,0]*t[0,1] + t[2,0]*t[1,1] + t[0,0]*t[2,1]))

t_area = true_area(triangle)

print(f"시뮬레이션 추정 넓이: {estimated_area:.2f}")
print(f"수학적 실제 넓이: {t_area:.2f}")
print(f"오차율: {abs(estimated_area - t_area) / t_area * 100:.2f}%")


plt.figure(figsize=(8, 8)) 


if len(outside_points) > 0:
    plt.scatter(outside_points[:, 0], outside_points[:, 1], color='blue', s=2, alpha=0.5, label='Outside (Blue)')
if len(inside_points) > 0:
    plt.scatter(inside_points[:, 0], inside_points[:, 1], color='red', s=2, alpha=0.5, label='Inside (Red)')


t_plot = np.vstack((triangle, triangle[0]))
plt.plot(t_plot[:, 0], t_plot[:, 1], color='black', linewidth=2, label='Triangle Edge')


plt.xlim(0, grid_size)
plt.ylim(0, grid_size)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Monte Carlo: Estimated Area = {estimated_area:.2f} (True = {t_area:.2f})')
plt.legend(loc='upper right')


plt.show()