
import IsingGrid
import matplotlib as mpl

import matplotlib.pyplot as plt
from copy import deepcopy
import time
# Fundamental parameters

size_list=[11,13,15,17,19]
temperature_list=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4]
tlist=[(k-2.269)/2.269 for k in temperature_list]        #无量纲温度
print(tlist)
dimensionless_list=[[],[],[],[],[]]
dimensionless_mag=[[],[],[],[],[]]
u_lsit= [[],[],[],[],[]] #存放各种温度下的binder cumulant
Jfactor = 1
interval=[[],[],[],[],[]]

# Generate grid
for i in range(5):
    dimensionless_list[i]=[k*(size_list[i]**1) for k in tlist]
    g = IsingGrid.Grid(size_list[i], Jfactor)  # 对每一个size都需要单独生成一个对象，因为canvas大小不同
    g.randomize()  # 随机生成一个canvas
    interval[i] = int(size_list[i] **0.35)  # 为了便于处理，将动力学因子取成z=2
    steps = 2000 * interval[i]  # 每一次蒙卡采样选择20个数据点
    # data = []       # 用于存放特定size特定温度下的采样所得canvas结果，每一个新尺寸循环重置为[]



    for temperature in temperature_list:
        m = 0  # 磁化等物理量，每一次温度遍历重置为0
        m_square = 0
        nm = 0
        m_quadr = 0
        for step in range(steps):
            clusterSize = g.clusterFlip(temperature)
            if (step + 1) % interval[i] == 0:
                print("Step ", step + 1, "/", steps, ", Cluster size ", clusterSize, "/", size_list[i] * size_list[i])

            if step > 20 * interval[i] and (step + 1) % interval[i] == 0:    # 对达到平衡态的状态进行采样，间隔为interval
                nm += 1
                m += abs(g.avrM())
                m_square += (g.avrM())**2
                m_quadr += (g.avrM())**4
        t=(m_quadr/nm)/(3*(m_square/nm)**2)
        u=1.5*(1-t)
        mag=m/nm
        u_lsit[i].append(u)
        dimensionless_mag[i].append(mag*(size_list[i])**0.125)


    print("Simulation completes.")
    # Animation
    print("Animation begins.")


    print("Animation completes.")


print(u_lsit[0])
print(dimensionless_list)
# p1=plt.scatter(dimensionless_list[0],u_lsit[0],s=10,color='red')
# p2=plt.scatter(dimensionless_list[1],u_lsit[1],s=10,color='orange')
# p3=plt.scatter(dimensionless_list[2],u_lsit[2],s=10,color='yellow')
# p4=plt.scatter(dimensionless_list[3],u_lsit[3],s=10,color='blue')
# p5=plt.scatter(dimensionless_list[4],u_lsit[4],s=10,color='purple')

p1=plt.scatter(dimensionless_list[0],dimensionless_mag[0],s=10,color='red')
p2=plt.scatter(dimensionless_list[1],dimensionless_mag[1],s=10,color='orange')
p3=plt.scatter(dimensionless_list[2],dimensionless_mag[2],s=10,color='yellow')
p4=plt.scatter(dimensionless_list[3],dimensionless_mag[3],s=10,color='blue')
p5=plt.scatter(dimensionless_list[4],dimensionless_mag[4],s=10,color='purple')


# p1=plt.scatter(u_lsit[0],dimensionless_mag[0],s=10,color='red')
# p2=plt.scatter(u_lsit[1],dimensionless_mag[1],s=10,color='orange')
# p3=plt.scatter(u_lsit[2],dimensionless_mag[2],s=10,color='yellow')
# p4=plt.scatter(u_lsit[3],dimensionless_mag[3],s=10,color='blue')
# p5=plt.scatter(u_lsit[4],dimensionless_mag[4],s=10,color='purple')


plt.title('dimensionless quantity curve')
plt.xlabel('dimensionless temperature')
# plt.xlabel('Binder cumulant')
plt.ylabel('dimensionless magnetic')
# plt.ylabel('Binder cumulant')

plt.legend((p1,p2,p3,p4,p5),('size=11','size=13','size=15','size=17','size=19'))
plt.show()



