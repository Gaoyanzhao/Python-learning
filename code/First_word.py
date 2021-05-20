# 使用print打印出来横向排放的三颗星***,注意需要一颗一颗的打印

print('*', end='')
print('*', end='')
print('*')


# 使用print打印等腰三角形， 一行一行的打印

a = '*'
b = ' '
for i in range(7):
    c = 3
    if(i <= c):
        print(b * (c - i), end='')
        print(a * ((2 * i)+1))


# 录入一个数值， 输出这个数的平方

value = input('请输入一个数(注：只能输入小数或者整数)：')
print("这个数的平方为：", float(value) * float(value))


# 录入一个二进制数据，将其转化为十进制的整数数据

value1 = int(input('请输入一个二进制类型的数据：(注：只能输入二进制类型的数据)'), base=2)
print("对应的十进制数据为：", value1)
