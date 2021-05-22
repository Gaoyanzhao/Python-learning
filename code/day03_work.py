# 输入x坐标与y坐标，输出这个坐标所在的象限

x, y = int(input('请输入横坐标')), int(input('请输入纵坐标'))  # 输入一个坐标
if x > 0 and y > 0:
    print('这个坐标在第一象限！')
elif x > 0 and y < 0:
    print('这个坐标在第二象限！')
elif x < 0 and y < 0:
    print('这个坐标在第三象限！')
elif x < 0 and y > 0:
    print('这个坐标在第四象限！')
else:
    print('这不是个合法坐标，或者这个坐标在坐标轴上！')


# 某超市为了促销，规定：购物不足50元的按原价付款，超过50不足100的按九折付款，超过100元的，超过部分按八折付款。编一程序完成超市的自动计费的工作

pay = float(input('请录入消费金额（￥）：'))  # 获取用户消费金额
if pay < 50:
    print('您消费%0.2f元，没有超过50元请原价支付！' % pay)
elif pay > 100:
    print('您消费%0.2f元，已超过100元可以享受八折优惠！实际付款金额为%0.2f' % (pay, pay * 0.8))
else:
    print('您消费%0.2f元，超过50不足100元可以享受九折优惠！实际付款金额为%0.2f' % (pay, pay * 0.9))


# 有一个棋盘，有64个方格，在第一个方格里面放1粒芝麻重量是0.00001kg，第二个里面放2粒，第三个里面放4粒，下一个方格是上一个方格的2倍，求棋盘上放的所有芝麻的重量

weight0 = 0.00001  # 一个芝麻的重量
weight = 0  # 棋盘上所有芝麻的总重量
for i in range(64):
    weight += weight0 * 2 ** i
    # print(weight)
print(weight)


# 录入一个整数，求这个数的阶乘

num = int(input('请输入一个整数：'))  # 录入一个整数
for i in range(1, num):
    num *= i
print('这个数的阶乘为：%d' % num)


# 公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？

peach = 1  # 第七天桃子的数量
for i in range(6):
    peach = (peach + 1) * 2
    # print(peach)
print('公园里刚开始有%d个桃子' % peach)


# 求1到100以内能被7或者3整除，但是不能同时被3和7整除的数的个数

count = 0  # 计数器
for i in range(1, 101):
    if (i % 3 == 0 or i % 7 == 0) and not(i % 3 == 0 and i % 7 == 0):
        # print(i)
        count += 1
print(count)


# 输入年、月分别赋值为year与month，输出year年的month月的天数

year, month = int(input('请输入一个年份：')), int(input('请输入一个月份：'))  # 录入一个年份和一个月份
day = 0  # 设置一个天数
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    if month == 2:
        print('%d年的%d月有29天' % (year, month))
    elif month < 8:
        if month % 2 == 0:
            print('%d年的%d月有30天' % (year, month))
        else:
            print('%d年的%d月有31天' % (year, month))
    else:
        if month % 2 == 0:
            print('%d年的%d月有31天' % (year, month))
        else:
            print('%d年的%d月有30天' % (year, month))
else:
    if month == 2:
        print('%d年的%d月有28天' % (year, month))
    elif month < 8:
        if month % 2 == 0:
            print('%d年的%d月有30天' % (year, month))
        else:
            print('%d年的%d月有31天' % (year, month))
    else:
        if month % 2 == 0:
            print('%d年的%d月有31天' % (year, month))
        else:
            print('%d年的%d月有30天' % (year, month))


# 改进上边的代码

year, month = int(input('请输入一个年份：')), int(input('请输入一个月份：'))  # 录入一个年份和一个月份
l_month = [1, 3, 5, 7, 8, 10, 12]  # 将31天的月份划分成一个列表
if month > 12 or month < 1:
    print('输入的月份不合理!')
elif month in l_month:
    print('%d年%d月的天数是31天！' % (year, month))
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print('%d年%d月的天数是29天！' % (year, month))
    else:
        print('%d年%d月的天数是28天！' % (year, month))
else:
    print('%d年%d月的天数是30天！' % (year, month))


# 打印所有的水仙花数。

count = 0  # 设置一个计数器
for i in range(100, 1000):
    if i == (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3:
        print(i)
        count += 1
print('水仙花的个数为：%d' % count)


# 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）

height = 0.00008  # 设置纸的厚度
count = 0  # 设置一个计数器
while height <= 8848.13:
    height *= 2
    count += 1
print('对折%d次之后能达到珠穆朗玛峰的高度' % count)


# 键盘录入年月日，获取这个日期是这一年中的第几天

days = 0  # 定义一个初始的天数
l_month = [1, 3, 5, 7, 8, 10, 12]  # 将31天的月份划分到一个列表
# s_month = [4, 6, 9, 11]  # 将30天的月份划分到一个列表
count1, count2 = 0, 0  # 设置两个初始的计数器
year, month, day = int(input('请输入一个年份：')), int(input('请输入一个月份：')), int(input('请输入某一天：'))
for i in range(1, 12):
    if month - i <= 0:
        break
    if month - i in l_month:
        count1 += 1
    else:
        count2 += 1
days = 31 * count1 + 30 * count2 + day
if month > 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days -= 1
    else:
        days -= 2
print(days)


# 求斐波那契数列中第n个数的值，n是正整数。n值由控制台输入
# 说明：斐波那契数列是这样的一个数列：1、1、2、3、5、8、13、21、34、.... ，第一个数和第二个数是1，从第三个数开始每个元素是前两个元素相加的和。

n = int(input('请输入一个正整数：'))
n1, n2, i = 1, 1, 0  # 初始当n = 1, n = 2, 计数器
n_value = 0
if n <= 0:
    print('请输入一个正整数！')
elif n == 1 or n == 2:
    print(n1)
else:
    while n-2 > i:
        n_value = n1 + n2
        n1 = n2
        n2 = n_value
        i += 1
    print(n_value)



