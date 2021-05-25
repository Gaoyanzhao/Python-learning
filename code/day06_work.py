# 1. 封装一个函数，函数的功能是生成指定长度的验证码
# 要求：由数字和大小写英文字母构成的随机字符串

import random


def cos_ver(n):
    str_all = 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP0123456789'
    str1 = ''
    for i in range(n):
        str1 += random.choice(str_all)
    return str1


print(cos_ver(20))


# 2. 封装一个函数，函数的功能是对密码加密，默认密码中只有小写字母和空格
# 加密规则是 a变d, b变e, c变f, ...., u变x, v变y, w变z,  x变a, y变b,  z变c. 空格保持不变

def encryption(password):
    word_change = ''
    for i in password:
        if 96 < ord(i) < 120:
            i = chr(ord(i) + 3)
            word_change += i
        elif 120 <= ord(i) < 123:
            i = chr(ord(i) - 22)
            word_change += i
        elif i == ' ':
            word_change += i
        else:
            print('密码格式错误！')
            return False
    return word_change


print(encryption('dhd   ds   dj af  l'))
# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘


def num_factorial(number=10):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact


print(num_factorial(6))
# 写一个函数，获取在指定列表中与指定数据相同的所有索引


def num_index(num_list, value):
    count = -1
    list_in = []
    if value not in num_list:
        print('无法查找下标，数据不在列表中')
        return False
    for i in num_list:
        count += 1
        if i == value:
            list_in.append(count)
    return list_in


print(num_index([1, 11, 2, 733, 327, 23, 733], 733))
# 写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在


def cos_in(num_list, value):
    for i in num_list:
        if i == value:
            return True
    else:
        return False


print(cos_in([1, 11, 2, 733, 327, 23, 733], 23))
# 封装一个函数：统计多个数中以5结尾的数据


def statistics(*num):
    list_num = []
    count_1 = 0
    for num_1 in num:
        if type(num_1) == str:
            if num_1[len(num_1) - 1] == '5':
                count_1 += 1
                list_num.append(num_1)
        else:
            num_2 = str(num_1)
            if num_2[len(num_2) - 1] == '5':
                count_1 += 1
                list_num.append(eval(num_2))
    print(count_1)
    return list_num


print(statistics(325, 25525, 'nu5', 'abc', 'df4', 222))
# 有一下数字：77、39、26、531、426 根据首位进行比较获取最大值


def first_max_number(*num_list):
    number_n = '0'
    for number in num_list:
        number_s = str(number)
        if number_s[0] > number_n[0]:
            number_n = number_s
    return eval(number_n)


print(first_max_number(77, 39, 26, 531, 426))

