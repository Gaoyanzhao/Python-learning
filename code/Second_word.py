# 假设今天的上课时间为15678秒，编程计算今天上课时间是对少小时，多少分钟，多少秒；
# 以'多少时多少分多少秒'的方式表示出来

Time = 15678
ts = Time % 60
tm = Time // 60 % 60
th = Time // 60 // 60
print('上课的时间是%d时%d分%d秒' % (th, tm, ts))


# 定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常！
# 公式: `体重(kg)/(身高(m)的平方值)` 在18.5 ~ 24.9之间属于正常, 小于18.5偏瘦，大于24.9偏胖

height = float(input('请输入你的身高(m)：'))
weight = float(input('请输入你的体重(kg)：'))
body = weight / height ** 2
if 18.5 <= body <= 24.9:
    print('你的身材正常！')
elif body < 18.5:
    print('你的身材偏瘦！')
else:
    print('你的身材偏胖！')


# 水仙花数校验器：输入一个三位数，判断其是不是水仙花数
# 水仙花数是一个三位数，特点是每位上数的立方和结果是其本身
# 例如 153 = 1**3 + 5 ** 3 + 3**3

flowers = int(input('请输入你认为的一个水仙花数（3位）：'))
if flowers == (flowers // 100) ** 3 + (flowers // 10 % 10) ** 3 + (flowers % 10) ** 3:
    print('这个数就是水仙花数！')
else:
    print('你输入的数并不是水仙花数！')

# 回文数校验器：输入一个五位数，判断其是不是回文数
# 回文数特点：万位与个位相同， 十位与千位相同 例如 12321

back_word = int(input('请输入一个五位数：'))
if (back_word // 10000) == (back_word % 10) and (back_word // 1000 % 10) == (back_word // 10 % 10):
    print('这个数是回文！')
else:
    print('这个数不是回文！')


# 三角形校验器：录入三角形的三个边长，判断三个数据能否构成三角形构成三角形的条件是任意两边之和大于第三边

a, b, c = int(input('请输入三角形的一个边长：')), int(input('另一个边长：')), int(input('最后一个边长:'))
if a+b < c or a+c < b or b+c < a or b-a > c or b-c > a or a-c > b:
    print('这构不成一个三角形！')
else:
    print('这是一个三角形！')
