
import IsingGrid
import matplotlib as mpl

import matplotlib.pyplot as plt
from copy import deepcopy
import time
size_list=[11,13,15,17,19]# temperature =2.28
temperature_list=[1,2.1,2.23,2.26,2.3,2.4,2.8,3,3.2,3.4,3.6,3.8,4,5,6,7,8,9,10,11,15]
interval=[[],[],[],[],[]] # 存放各种size对应的间隔
Jfactor = 1
m_lsit= [[],[],[],[],[]] # 存放各种温度下的磁化

for i in range(len(size_list)):
    interval[i]= int(size_list[i]**2)
    steps=interval[i]*20
    data = []
    print("Simulation begins.")

    g = IsingGrid.Grid(size_list[i], Jfactor) # 生成对应size的canvas
    g.randomize() # 随机初始化canvas
    for temperature in temperature_list:
        m = 0
        nm = 0
        for step in range(steps):
            clusterSize = g.clusterFlip(temperature)

            if (step + 1) % interval[i] == 0:
                data.append(deepcopy(g.canvas))

            if (step + 1) % (10 * interval[i]) == 0:
                print("Step ", step + 1, "/", steps, ", Cluster size ", clusterSize, "/", size_list[i] * size_list[i])

            if step >5*interval[i] and (step + 1) % interval[i] == 0:    #对达到平衡态的状态进行采样，间隔为interval
                nm += 1
                m += abs(g.avrM())
        m_lsit[i].append(m/nm)

print("Simulation completes.")

print("Animation begins.")

print("Animation completes.")

plt.plot(temperature_list,m_lsit[0],label='size=11')
plt.plot(temperature_list,m_lsit[1],label='size=13')
plt.plot(temperature_list,m_lsit[2],label='size=15')
plt.plot(temperature_list,m_lsit[3],label='size=17')
plt.plot(temperature_list,m_lsit[4],label='size=19')


plt.title('magnetic curve')
plt.ylabel('|M|')
plt.xlabel('Temperature')
plt.legend()
plt.show()


