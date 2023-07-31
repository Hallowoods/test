

import IsingGrid
import matplotlib as mpl

import matplotlib.pyplot as plt
from copy import deepcopy
import time

# Fundamental parameters
u_lsit= [[],[],[],[]] # 存放各种温度下的binder cumulant
m_squarelist=[[],[],[],[]]
m_list=[[],[],[],[]]
size_list=[11,13,15,17]
temperature_list=[i*0.2 for i in range(1,20)]
Jfactor = 1
interval=[[],[],[],[]]    #3ee 存放各种size下的自关联时间interval=size**2

# Generate grid
for i in range(4):      # 对不同的size进行遍历
    g = IsingGrid.Grid(size_list[i], Jfactor)     # 对每一个size都需要单独生成一个对象，因为canvas大小不同
    g.randomize()       # 随机生成一个canvas
    interval[i]=int(size_list[i]**0.35)    # 为了便于处理，将动力学因子取成z=0.35
    steps=7000*interval[i]        # 每一次蒙卡采样选择60个数据点
    # data = []       # 用于存放特定size特定温度下的采样所得canvas结果，每一个新尺寸循环重置为[]


    for temperature in temperature_list:
        m = 0  # 磁化等物理量，每一次采样后重置为0
        m_square = 0
        nm = 0
        m_quadr = 0
        for step in range(steps):
            clusterSize = g.clusterFlip(temperature)        # 每个step做一个翻转并返回clustersie

            if (step + 1) % interval[i] == 0:
                print("Step ", step + 1, "/", steps, ", Cluster size ", clusterSize, "/", size_list[i] * size_list[i])

            if step >30*interval[i] and (step + 1) % interval[i] == 0:    # 对达到平衡态的状态进行采样，间隔为interval(热化时间和尺寸的关系?)
                nm += 1
                m += abs(g.avrM())
                m_square+=(g.avrM())**2
                m_quadr+=(g.avrM())**4
        t=(m_quadr/nm)/(3*(m_square/nm)**2)
        u=1.5*(1-t)
        u_lsit[i].append(u)
        m_list[i].append(m/nm)


    print("Simulation completes.")

    print("Animation begins.")

    print("Animation completes.")



plt.plot(temperature_list,u_lsit[0],label='size=30',linestyle='-',linewidth=1.2)
plt.plot(temperature_list,u_lsit[1],label='size=50',linestyle='--',linewidth=1.8)
plt.plot(temperature_list,u_lsit[2],label='size=100',linestyle='-.',linewidth=1.8)
plt.plot(temperature_list,u_lsit[3],label='size=150',linestyle=':',linewidth=1.8)


plt.title('Binder cumulant curve')
plt.ylabel('Binder cummulant')
plt.xlabel('Temperature')
plt.legend()
plt.show()



