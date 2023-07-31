# 开发时间：2023/3/6 20:24
import math

#四极杆质谱仪标定函数
# import math
#
# a=0.9504
# b=-0.01213
# def f(x):
#     return a*x+b
#
# list=[15.7,27.7,28.4,29.4,30.4,32.4,45.5,47.3,48.4]
#
# for i in range(len(list)):
#     print(round(f(list[i])))

#计算平均值和不确定度
# lst=[2.58E-05,2.79E-05,2.64E-05,2.59E-05,2.73E-05,2.61E-05]       # 列表数据
# ave=sum(lst)/len(lst)           # 求平均值
# t=0
# for x in lst:
#     t += (x-ave)**2
# u_a=math.sqrt(t/(len(lst)*(len(lst)-1)))        # 求A类不确定度
# print('ave:',ave)
# print('u_a:',u_a)


#光泵磁共振
lst=[0.051]
output=[]
N=100
r=0.153

for t in lst:
    B=32*math.pi/(5**(3/2))*(N/r)*t
    output.append(B)
print(output)




