# 开发时间：2022/11/21 18:49
import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
N = 50      # 晶格大小
J = 1.0     # 交换耦合常数
T_list = np.linspace(0.1, 5.0, 50)   # 温度范围
n_mc = 1000     # 蒙特卡洛步数

# 产生随机初始状态
theta = 2 * np.pi * np.random.random((N, N))
x = np.cos(theta)
y = np.sin(theta)

# 计算每个格点周围的四个邻居
left = np.roll(x, -1, axis=1)
right = np.roll(x, 1, axis=1)
up = np.roll(y, -1, axis=0)
down = np.roll(y, 1, axis=0)

# 计算总能量
def energy(x, y):
    E = -J * np.sum(x * (left + right) + y * (up + down))
    return E

# 计算内能和热容
def calculate(T):
    E_list = []
    C_list = []
    beta = 1 / T
    for i in range(n_mc):
        # 随机选取一个格点
        ix, iy = np.random.randint(0, N, size=2)
        # 计算其周围四个邻居的总自旋
        s = x[ix, iy] * (left[ix, iy] + right[ix, iy]) + y[ix, iy] * (up[ix, iy] + down[ix, iy])
        # 计算更新后的自旋
        theta_new = theta[ix, iy] + np.random.uniform(-np.pi, np.pi) + beta * J * s
        x_new = np.cos(theta_new)
        y_new = np.sin(theta_new)
        # 计算能量变化
        delta_E = energy(x_new, y_new) - energy(x, y)
        # 判断是否接受新状态
        if delta_E < 0 or np.random.uniform() < np.exp(-beta * delta_E):
            x[ix, iy] = x_new
            y[ix, iy] = y_new
            theta[ix, iy] = theta_new
        # 计算当前总能量
        E = energy(x, y)
        E_list.append(E)
        # 计算当前内能和热容
        if i > n_mc // 2:
            E_avg = np.mean(E_list)
            E2_avg = np.mean([E**2 for E in E_list])
            C = (E2_avg - E_avg**2) / T**2
            C_list.append(C)
    return np.mean(E_list), np.mean(C_list)

# 计算内能和热容随温度的变化关系
E_list = []
C_list = []
for T in T_list:
    E, C = calculate(T)
    E_list.append(E)
    C_list.append(C)

# 绘制内能和热容随温度的变化关系图像
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(T_list, E_list, 'b-')
plt.show()
