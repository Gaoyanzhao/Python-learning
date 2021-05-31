# 1. `There is no denying that successful business lies in a healthy body and mind`
# 提取这句话中包含`i`的单词

src_str = 'There is no denying that successful business lies in a healthy body and mind'
n_str = [n_str for n_str in src_str.split() if 'i' in n_str]
print(n_str)


# 校验手机号是否合法
# 要求:
# 	 1.长度是11位的数字
# 	 2.以186	185	179	177	135	133	156	155	139开头

def is_phone_number(number):
    start_number = ['186', '185', '179', '177', '135', '133', '156', '155', '139']
    if len(number) == 11 and number[:3] in start_number:
        return True
    else:
        return False


num = input('请输入一个手机号码：')
print(is_phone_number(num))


# 双色球
# 在1-33中随机选择6个不重复的数据 作为红球
# random.sample(range(1, 34), 6)
# 在1-16中随机选择一个数据 作为蓝球
# 把最后球的信息拼接为：
# 	例如 03 09 11 33 29 18 + 15
# 注意 不足两位的按照两位格式化 还要保证红球是从小到大的顺序

import random


def dubble_ball_number():
    red_ball = random.sample(range(1, 34), 6)
    blue_ball = random.sample(range(1, 17), 1)
    ls = [str(f'{i:02d}') for i in red_ball+blue_ball]
    print(' '.join(ls[:6]) + ' + ' + ls[-1])


dubble_ball_number()


# 创建一个空列表，命名为names,往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素

# a.往names列表里末尾追加一个alex
# b.把shanshan的名字改成中文，姗姗
# c.返回peiqi的索引值
# d.对列表中的元素进行升序排序
# e.删除jack这个元素
# f.通过下标删除第一个元素
# g.创建新列表[1,2,3,4,2,5,6,2],合并入names列表
# h.取出names列表中索引4-7的元素
# i.取出names列表中索引2-10的元素，步长为2
# j.取出names列表中最后3个元素
# k.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1

names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
names.append('alex')
print(names)
names[3] = '姗姗'
print(names)
print(names.index('jack'))
names.sort()
print(names)
names.remove('jack')
print(names)
names.pop(0)
print(names)
ls = [1, 2, 3, 4, 2, 5, 6, 2]
names += ls
print(names)
print(names[4:8])
print(names[2:11:2])
print(names[-3:])
for index, value in enumerate(names):
    print(index, value)
    if index % 2 == 0:
        value = -1


# 已知一个数字列表， 编写程序将列表中所有元素乘以2

nums = [12, 34, 5, 6, 19, 23]
new_nums = [i*2 for i in nums]
print(new_nums)


# 列表中存储学生的成绩，去除掉不及格的成绩

scores = [77, 65, 42, 58, 89, 75]
qua_scores = [sco for sco in scores if sco >= 60]
print(qua_scores)


# 列表中存储学生的姓名， 按照学生姓名的首字母降序排序【练练算法与列表的系统方法】
new_names = ['driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl', 'rose']
# 冒泡算法
for i in range(1, len(new_names)):
    for j in range(0, len(new_names) - i):
        if new_names[j] < new_names[j+1]:
            new_names[j], new_names[j+1] = new_names[j+1], new_names[j]
print(new_names)

# 选择排序
for i in range(len(new_names) - 1):
    for j in range(i+1, len(new_names)):
        if new_names[i] < new_names[j]:
            new_names[i], new_names[j] = new_names[j], new_names[i]
print(new_names)
# 插入排序
for i in range(1, len(new_names)):
    for j in range(i, 0, -1):
        if new_names[j] > new_names[j-1]:
            new_names[j], new_names[j-1] = new_names[j-1], new_names[j]
print(new_names)
# 快速排序


def quick_sort(names):
    if len(names) >= 2:
        mid = names[len(names)//2]
        big, small = [], []
        names.remove(mid)
        for ele in names:
            if ele < mid:
                small.append(ele)
            else:
                big.append(ele)
        return quick_sort(big) + [mid] + quick_sort(small)
    else:
        return names


print(quick_sort(new_names))
