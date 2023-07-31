

import IsingGrid
import matplotlib as mpl

import matplotlib.pyplot as plt
from copy import deepcopy
import time

# Fundamental parameters

size = 100
size_list=[60,80,100]
temperature =2.28
temperature_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,25,27,29]
tlist=[(k-2.269/2.269)for k in temperature_list]        #无量纲温度
print(tlist)
dimensionless_list=[[],[],[],[],[]]
dimensionless_mag=[[],[],[],[],[]]
u_lsit= [[],[],[],[],[]] #存放各种温度下的binder cumulant
Jfactor = 1
interval=[[],[],[],[],[]]

# Generate grid
for i in range(3):
    dimensionless_list[i]=[k*(size_list[i]**1) for k in tlist]
    g = IsingGrid.Grid(size_list[i], Jfactor)  # 对每一个size都需要单独生成一个对象，因为canvas大小不同
    g.randomize()  # 随机生成一个canvas
    interval[i] = size_list[i] ** 2  # 为了便于处理，将动力学因子取成z=2
    steps = 20 * interval[i]  # 每一次蒙卡采样选择20个数据点
    # data = []       # 用于存放特定size特定温度下的采样所得canvas结果，每一个新尺寸循环重置为[]

    m = 0  # 磁化等物理量，每一次尺寸循环重置为0
    m_square = 0
    nm = 0
    m_quadr = 0

    for temperature in temperature_list:
        for step in range(steps):

            # Single/cluster Filp

            # clusterSize = g.singleFlip(temperature)
            clusterSize = g.clusterFlip(temperature)

            # if (step + 1) % interval == 0:
            #         data.append(deepcopy(g.canvas))

            if (step + 1) % interval[i] == 0:
                print("Step ", step + 1, "/", steps, ", Cluster size ", clusterSize, "/", size_list[i] * size_list[i])

            if step > 10 * interval[i] and (step + 1) % interval[i] == 0:    # 对达到平衡态的状态进行采样，间隔为interval
                nm += 1
                m += abs(g.avrM())
                m_square += (g.avrM())**2
                m_quadr += (g.avrM())**4
        t=(m_quadr/nm)/(3*(m_square/nm)**2)
        u=1.5*(1-t)
        mag=m/nm
        u_lsit[i].append(u)
        dimensionless_mag[i].append(mag*(size_list[i])**0)


    print("Simulation completes.")
    # Animation
    print("Animation begins.")

    # for frame in range(0, len(data)):
    #     ax.cla()
    #     ax.imshow(data[frame], cmap=mpl.cm.winter)
    #     ax.set_title("Step {}".format(frame * interval))
    #     plt.pause(0.01)

    print("Animation completes.")
    # print(m/nm)#磁化强度
    # print(m_square/nm)
    # print(m_quadr/nm)
    # t=(m_quadr/nm)/(3*(m_square/nm)**2)
    # u=1.5*(1-t)
    # print('u=',u)  # binder cummulant

print(u_lsit[0])
plt.scatter(dimensionless_list[0],u_lsit[0],s=20,color='red')
plt.scatter(dimensionless_list[1],u_lsit[1],s=20,color='orange')
plt.scatter(dimensionless_list[2],u_lsit[2],s=20,color='yellow')
# plt.scatter(dimensionless_list[3],u_lsit[3],s=20,color='blue')
# plt.scatter(dimensionless_list[4],u_lsit[4],s=20,color='purple')

# plt.scatter(dimensionless_list[0],dimensionless_mag[0],s=20,color='red')
# plt.scatter(dimensionless_list[1],dimensionless_mag[1],s=20,color='orange')
# plt.scatter(dimensionless_list[2],dimensionless_mag[2],s=20,color='yellow')
# plt.scatter(dimensionless_list[3],dimensionless_mag[3],s=20,color='blue')
# plt.scatter(dimensionless_list[4],dimensionless_mag[4],s=20,color='purple')

plt.title('dimensionless quantity curve')
plt.ylabel('dimensionless magnetic')
plt.xlabel('dimensionless')
plt.legend()
plt.show()



