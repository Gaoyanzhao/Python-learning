# 声明一个列表，在列表中保存6个学生的信息
students = [
    {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel': '15400022839'},
    {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel': '15400022838'},
    {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel': '15400022839'},
    {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel': '15400022428'},
    {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel': '15400022839'},
    {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel': '15400022839'}
]


# (1) 统计不及格学生的个数
# (2) 打印不及格学生的名字和对应的成绩
def score_count(ls):
    count = 0
    for stu in range(len(ls)):
        if ls[stu].get('score') >= 60:
            count += 1
        else:
            print(ls[stu].get('name'), ls[stu].get('score'))
    return count


print(score_count(students))


# (3) 统计未成年学生的个数
def age_count(ls):
    count = 0
    for stu in range(len(ls)):
        if ls[stu].get('age') < 18:
            count += 1
    return count


print(age_count(students))


# (4) 打印手机尾号是8的学生的名字
def tel_8(ls):
    names = []
    for stu in range(len(ls)):
        if ls[stu].get('tel').endswith('8'):
            names.append(ls[stu].get('name'))
    return names


print(tel_8(students))


# (5) 打印最高分和对应的学生的名字
s1 = max(students, key=lambda s: s.get('score'))
print(s1['name'])  # 只能输出其中第一个是最大值的数据，其他数据也是最大值但是并不能全部输出


# 函数封装改进，但是代码不简洁
def max_score(ls):
    score = ls[0].get('score')
    names = {}
    for stu in range(len(ls)):
        if score < ls[stu].get('score'):
            score = ls[stu].get('score')
    for stu in range(len(ls)):
        if score == ls[stu].get('score'):
            names.setdefault(ls[stu].get('name'), score)
    return names


print(max_score(students))


# (6) 删除性别不明的所有学生
def del_st(ls):
    stu = 0
    while stu < len(ls):
        if ls[stu].get('gender') == '不明':
            del ls[stu]
            stu -= 1
        stu += 1
    return ls


print(del_st(students))


# (7) 将列表按学生成绩从大到小排序
students.sort(key=lambda s: s.get('score'), reverse=True)
print(students)

# 名片管理系统
# 思路:
# 使用字典包括每张名片的信息, 例如
# {'name': '张三', 'tel': '123', 'qq': '321'}
# 使用列表包含所有名片的信息, 如:
# user_list = [
#     {'name': '张三', 'tel': '123', 'qq': '321'},
#     {'name': 'lisi', 'tel': '666', 'qq': '999'},
#     {'name': 'jack', 'tel': '888', 'qq': '233'}
# ]
user_list = [
    {'name': '张三', 'tel': '123', 'qq': '321'},
    {'name': 'lisi', 'tel': '666', 'qq': '999'},
    {'name': 'jack', 'tel': '888', 'qq': '233'}
]


# 系统包含的操作:
#               1.添加名片
# 信息由控制台输入即可, 包含信息有用户名, 手机号, QQ号
# 名片的用户名不能重复, 如果添加是重复了要提示
# 用户名已被占用
# 让其重新输入
def add_card(ls):
    while True:
        username = input('请输入用户名：')
        if username not in [ls[i].get('name') for i in range(len(ls))]:
            break
        else:
            print('用户名已被占用，请重新输入')
    tel = input('请输入手机号：')
    qq_number = input('请输入QQ号：')
    user_dict = {'name': username, 'tel': tel, 'qq': qq_number}
    ls.append(user_dict)
    return user_dict


#               2.删除名片
# 根据名称name删除名片, 并询问是否确定删除
# 判断是否名片在名片中
def del_card(ls, name):
    print([ls[i].get('name') for i in range(len(ls))])
    if name in [ls[i].get('name') for i in range(len(ls))]:
        k = 0
        while k < len(ls):
            if ls[k].get('name') == name:
                while True:
                    is_del = input(f'是否确认删除{name}(Y/N)')
                    if is_del not in ['Y', 'N', 'y', 'n']:
                        print('请注意输入规范然后重新输入！')
                    elif is_del == 'Y' or is_del == 'y':
                        del ls[k]
                        k -= 1
                        print('删除成功！')
                        break
                    else:
                        print('放弃删除，返回首页')
                        break
            k += 1
    else:
        return -1


#               3.修改名片
# 先根据名片在列表中的编号
# 让用户选择名片, 再提示输入要哪个键的值
# 再提示让其输入新值
# 进而完成修改、
def change_card(ls):
    print([[i, ls[i].get('name')] for i in range(len(ls))])
    while True:
        num = int(input('请输入想要修改用户的编号：'))
        if num not in range(len(ls)):
            print('这不是个合法的编号，请按提示输入！')
            continue
        else:
            print(ls[num])
            while True:
                key_num = input('请输入想要修改哪个键：')
                if key_num not in ls[num].keys():
                    print('输入的键不合法请重新输入！')
                    continue
                else:
                    new_value = input('请输入一个新的值：')
                    ls[num][key_num] = new_value
                    break
            while True:
                is_continue = input('是否继续进行修改（Y/N）')
                if is_continue not in ['Y', 'N', 'y', 'n']:
                    print('请注意输入规范然后重新输入！')
                else:
                    break
            if is_continue == 'Y' or is_continue == 'y':
                print('继续修改其他值！')
                continue
            else:
                print('放弃继续修改，返回首页！')
                break


#               4.根据名称查询名片
def find_card(ls, name):
    if name in [ls[i].get('name') for i in range(len(ls))]:
        number_list = [[i, ls[i].get('name')] for i in range(len(ls))]
        for i in range(len(number_list)):
            if number_list[i][1] == name:
                print(ls[i])
                # return ls[i]
    else:
        print('找不到你想要的名片，请确认名称是否正确之后重新操作！')


#               5.显示所有的名片信息
def display_cord(ls):
    print(ls)


#               6.退出系统
# 询问是否退出
# 确定的情况下才退出


# 程序启动 , 如下提示:
#
# =============欢迎进入名片管理系统============
#
# =============1.添加名片  2.删除名片============
#
# =============3.修改名片  4.查询名片============
#
# =============5.显示所有名片  6.退出============
#
# 请输入要进行的操作编号:

while True:
    print('欢迎进入名片管理系统'.center(40, '='))
    print()
    print('1.添加名片  2.删除名片'.center(40, '='))
    print()
    print('3.修改名片  4.查询名片'.center(40, '='))
    print()
    print('5.显示所有名片  6.退出'.center(40, '='))
    print()
    x = input('请输入要进行的操作编号：')
    if x == '6':
        break
    elif x == '1':
        print(add_card(user_list))
    elif x == '2':
        name1 = input('请输入要删除的名片的名称')
        print(del_card(user_list, name1))
    elif x == '3':
        print(change_card(user_list))
    elif x == '4':
        name2 = input('请输入要删除的名片的名称')
        find_card(user_list, name2)
    else:
        display_cord(user_list)



