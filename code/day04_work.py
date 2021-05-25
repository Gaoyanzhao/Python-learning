# 1.石头剪刀布游戏
# ​		0 表示石头 1表示剪刀 2表示布
# ​		系统随机生成0-2之间的任意一个数
# ​		用户输入0-2中的任意一个数
# ​		验证输赢
# ​			当用户赢了之后 
# ​			问用户是否继续玩 输入 yes 为继续 no 为退出 其他时要求重新输入 yes 或者 no
# 【注意： 石头 > 剪刀  剪刀 > 布 布 > 石头】

import random

rock, scissors, paper = 0, 1, 2  # 定义石头剪刀布分别用0,1,2表示
while True:
    user_num = int(input('请输入一个0-2之内的数：'))
    sys_num = random.randint(0, 2)
    if user_num not in [0, 1, 2]:
        print('请按照提示输入！')
        continue
    if user_num < sys_num or (user_num == 2 and sys_num == 0):
        print('恭喜获得胜利！')
        while True:
            choice = input('输入yes为继续，no退出')
            if choice == 'no' or choice == 'yes':
                break
            else:
                print('输入不规范，请重新输入！')
        if choice == 'no':
            print('退出成功！')
            break
        else:
            print('欢迎继续游戏！')
    else:
        print('很遗憾，你输了！')
        break


# 2.有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少

#  方法一，时间复杂度感觉会低一点，但是没找到while的终止条件，借助算出来的个数勉强跳出循环

import random

num_list = [1, 2, 3, 4]
number_l = []
count = 0
while True:
    num = random.sample(num_list, 3)
    number = num[0] * 100 + num[1] * 10 + num[2]
    if number not in number_l:
        print(number)
        count += 1
        number_l.append(number)
    if len(number_l) == 24:
        break
print(number_l, count)


#  方法二，这个就是for循环

count = 0
number_l = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j != k and i != k:
                count += 1
                num = i*100 + j * 10 + k
                number_l.append(num)
print('能组成%d个不同的三位数，且组成3位数的每个数字不同' % count )
print('所有3位数由列表显示为', number_l)


# 3.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

molecular1, molecular2 = 2, 3  # 第一个和第二个分子
Denominator1, Denominator2 = 1, 2  # 第一个和第二个分母
value = molecular1 / Denominator1 + molecular2 / Denominator2  # 前两项的和
for i in range(3, 21):
    molecular = molecular1 + molecular2
    molecular1, molecular2 = molecular2, molecular
    Denominator = Denominator1 + Denominator2
    Denominator1, Denominator2 = Denominator2, Denominator
    value += molecular / Denominator
print('这20项数列的和为：%0.2f' % value)


# 4.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？

peach = 1  # 第七天桃子的数量
for i in range(6):
    peach = (peach + 1) * 2
print('公园刚开始有%d只桃子' % peach)


# 6.利用循环，实现下面数据的输出结果
# `1-3+5-7+....-99+101`


count, value = 0, 0  # 奇偶计数器, 求和结果
for i in range(1, 102, 2):
    count += 1
    if count % 2 == 0:
        i = i * (-1)
    value += i
print('输出结果为', value)


# 7.统计1到200中的质数以及质数的个数

count = 0  # 计数器
number_l = []  # 用来存放质数的列表
for num in range(2, 201):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1
        number_l.append(num)
print('1-200中有%d个质数为：' % count, number_l)