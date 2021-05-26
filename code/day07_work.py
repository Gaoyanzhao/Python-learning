# 封装函数 验证字符串的内容是否是纯数字
def is_all_number(src_str):
    for i in src_str:
        if not('0' <= i <= '9'):
            return False
    return True


print(is_all_number('546kd'))
# 封装一个函数 对字符串中的内容去重


def del_repeat(src_str):
    no_repeat_list = src_str[0]
    for i in src_str:
        if i not in no_repeat_list:
            no_repeat_list += i
    return no_repeat_list


print(del_repeat('djfskahfkue548ed4'))
# 声明一个装饰器：校验功能接到的参数是不是整型数据
# 不是整型的话 抛出错误 `raise TypeError()`
# 是的话 执行对应的功能


def is_int(func):
    def new_func(*args, **kwargs):
        if type(func(*args, **kwargs)) != int:
            raise TypeError()
        else:
            return func(*args, **kwargs)
    return new_func


@is_int
def add(a, b):
    return a+b


print(add(4, 5))
# 使用递归完成操作
# 有5个孩子， 问第五个人多少岁，他说比第四个人大3岁， 问第四个人多少岁，他说比第三个人大3岁， 问第三个人多少岁，他说比第二个人大3岁,
# 问第二个人多少岁，他说比第1个人大3岁，问第1个人多少岁，他说13岁，使用递归求第五个人的年龄


def old_year(n):
    if n == 1:
        return 13
    else:
        return old_year(n-1) + 3


print(old_year(5))