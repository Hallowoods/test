# 开发时间：2023/3/2 8:49
# import daytime是一个函数包，写出来是申明以下代码调用了这个包
# 然后给now变量赋值，datetime.datetime.now()给出现在的时间，里面应该有年月日等所有时间信息，但是只想用“星期几“
# 所以用now.isoweekday()导出里面的”星期几“赋值给变量wday，其格式是一个整数如：1、2、3、4、5、6、7
# print出来的 %s一个引用格式，引用的内容就是后面的 %W3DAY[wday-1]
# WDAY是一个字符串，WDAY[i]就代表该字符串下标为i的字符，但是下标是从0开始，所以例如WDAY[1]给出的是”二“这个数字，所以星期X应该是WDAY[X-1]

# list='一二三四五六天'
# m=int(input('请输入今天是星期几(用阿拉伯数字表示)：'))
# print('今天是星期%s'%list[m-1])
# n=int(input('请问你想知道哪天之后是星期几（用阿拉伯数字表示）：'))
# if n < 0:
#     raise ValueError('n应该是整数')
# future_day=(m+n)%7
# print('结果是星期%s'%list[future_day-1])

# number =2
# # if number%2==0:
# #     even=True
# # else:
# #     even=False
#
# # even= True if number%2==0 else False
#
# even=number%2==0

#
# #第八题
# def double(x):
#     t=2*x
#     return t
#
# #第九题
# x=3
# x=double(double(x)+3)
# print(x)


# def almost_equal(x,y,sip=10E-10):
#     if abs(x-y)<sip:
#         return True
#     else:
#         return False
#
# print(almost_equal(1,0.99999999999999999))



# minutes = int(input("请输入时间间隔(分钟): "))
#
# # 转换为天数，小时和分钟数
# days = minutes // 1440
# hours = (minutes % 1440) // 60
# minutes = (minutes % 1440) % 60
#
# # 输出结果
# if days > 0:
#     print(f"{days}天", end="")
# if hours > 0:
#     print(f"{hours}小时", end="")
# if minutes > 0:
#     print(f"{minutes}分钟", end="")
# if days == 0 and hours == 0 and minutes == 0:
#     print("0分钟", end="")
# print("。")



# n=int(input('please input n ='))
# j=n%5
# i=n//5
#
# def f5():
#     for line in range(5):
#         t=2*line+1
#         s=''
#         for k in range(t):
#             s+=str(k+1)
#         print('{:{:s}{align}{width}}'.format(s,"-",align="^",width=11))
#
#
# def f():
#     for line in range(j):
#         t = 2 * line + 1
#         s = ''
#         for k in range(t):
#             s += str(k+1)
#         print('{:{:s}{align}{width}}'.format(s, "-", align="^", width=11))
#
# for t in range(i):
#     f5()
# if j!=0:
#     f()

import random
# def f():
#     number = random.randint(1,100)
#     guess=int(input('您猜的数是'))
#     for i in range(1,5):
#         if guess > number:
#             print('您猜的数太大了！')
#         elif guess < number:
#                 print('您猜的数太小了！')
#         elif guess == 'help':
#                 print('[作弊模式]您要猜的数是',number)
#         else:
#             print('您猜对了！')
#
#             print('您已经猜了四次，要猜的数是',number)
#             anwser=input(print('继续游戏(Y/N)...?')
# while True:
#     f()
#     if anwser == "Y" or "y":
#         False
# try:
#     f()
# except:
#     guess = input('请输入一个[1，100]范围的整数')
#     raise




import random
# def f():
#     number = random.randint(1,100)
#     istrue=True     #循环标记初始是True
#     tick=0    #用来标记询问的次数！
#     while istrue:
#         initial_input=input('您猜的数是')
#
#         if initial_input=='help' or initial_input=='8888':
#             print('[作弊模式]您要猜的数是',number)
#             break       #一旦输入的是‘help’或者‘8888’，直接不进行下面的步骤，直接推出循环！
#
#         else:
#             guess =int(initial_input)       #每一次循环询问一次guess的值！(注意，此时initial_input才只能是数字形式的字符串，才可以用int作用)
#         tick += 1       #由于初始值是0，tick为多少就表明猜了错少次
#         #接下来进行判断！
#         if guess > number:
#             print('您猜的数太大了！')
#         elif guess < number:
#             print('您猜的数太小了！')
#
#         else:       #表明猜对了
#             print('您猜对了！')
#             break        # 猜对了，退出循环！
#         print('你猜了',tick,'次哦！')
#         if tick == 4:       # 当tick=4且没有被上一行的break终止循环，表明没有猜对且次数已经达到了四次，推出循环
#             istrue=False
#
# #下面素主体部分
# print('你好李奕霖，吃了吗？')
# stilltrue=True      #stilltrue是循环标记,初始值是True
# while stilltrue:
#     f()
#     t=input('输了并不可耻,放弃才可耻,是否要进行新一局游戏？（输入y/Y继续，输入其他退出）')
#     if t != 'y' and t !='Y':
#         stilltrue=False
# print('想lyl了！,想ss')


# matrix=[[1,2,3],[4,5,6],[7,8,9]]
#
# def is_matrix(matrix):
#     istrue=True
#     i=0
#     while istrue:
#         sum_1=sum(matrix[i])
#         sum_2=sum(matrix[i+1])
#         i += 1
#         if sum_1!=sum_2:
#             istrue=False
#
#     j = 0
#     while istrue:
#         sum_3=sum([matrix[l][j] for l in range(len(matrix))])
#         sum_4 = sum([matrix[l][j+1] for l in range(len(matrix))])
#         j+=1
#         if sum_3!=sum_4:
#             istrue=False
#
#     if istrue==True:
#         sum_5=sum([matrix[k][k] for k in range(len(matrix))])
#         sum_6=sum([matrix[k][len(matrix-k-1)] for k in range(len(matrix))])
#         if sum_5!=sum_6:
#             istrue=False
#
#     return istrue



# def get_element(s,idx):
#     try:
#         return s[idx]
#     except:
#         return None
#         print('下标不合法')
#
#
# print(get_element([1,2,3],2))


# def odd_sum(*a,init=0):
#     b=list(a)
#     sum=init
#     for i in b:
#         if i % 2 != 0:
#             sum+=i
#     return sum
#
# print(odd_sum(1,2,6,4,5))
# print(odd_sum(1,2,6,4,5,init=4))



lst=[1,2,3]
lst2=lst
lst2[-1]=17
lst2='sss'
print(lst)












































