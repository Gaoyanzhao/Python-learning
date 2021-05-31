## 排序

#### 冒泡排序

##### 1.冒泡排序

```
规律:
	从头开始将相邻的元素两两进行比较， 如果前者大于后者 交换两者的位置
	
# 冒泡排序
num = [1, 43, 32, 56, 76, 243, 654]
for i in range(1, len(num)):
    for j in range(len(num) - i):
        if num[j] < num[j+1]:
            num[j+1], num[j] = num[j], num[j+1]
print(num)
```



##### 2.选择排序

```
第一次遍历的时候
	将第一个位置的元素与之后每一个位置的元素进行比较 如果前者大于后者 两者交换位置  得到最小值
第二次遍历的时候
	将第二个位置的元素与之后每一个位置的元素进行比较 如果前者大于后者 两者交换位置  得到次小值
...

直到排序完成

# 选择排序
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

print(num)
```



##### 3.插入排序

```
第一次遍历的时候
	将下标为1的元素 与 下标为0的元素进行比较  如果前者小于后者 两者交换位置
第二次遍历的时候
	从下标为2的位置开始  向左对相邻的元素两两进行比较  
...

排序完成

# 插入排序
for i in range(1, len(num)):
    for j in range(i, 0, -1):
        if num[j] > num[j-1]:
            num[j], num[j-1] = num[j-1], num[j]
        else:
            break

print(num)
```



##### 4.快速排序

```
分治法：
在列表中找一个数据作为基准值， 然后遍历列表， 比基准值大的向右走， 比基准值小的 向左走

同样的操作 再去对大的一方与小的一方进行相同的操作 来完成排序效果

一般情况下是把列表中的中间值当做基准值

# 快速排序
def quick_sort(st):
    if len(st) >= 2:
        mid = st[len(st) // 2]
        st.remove(mid)
        big, small = [], []
        for ele in st:
            if ele >= mid:
                big.append(ele)
            else:
                small.append(ele)
        return quick_sort(small) + [mid] + quick_sort(big)
    else:
        return st


print(quick_sort(num))
```