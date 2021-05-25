# 笔记

### 函数

**作用：简化代码，提高代码的复用性**

1. **系统函数**

   `print, ord, chr, type, id, input`

   `abs()` ---    获取数据的绝对值

   `pow(x, y)` ---  获取x的y次幂

   `round(x, k = 0)`   ---   保留k位小数的情况下进行4舍五入

   `max()`  ----    获取序列或者多个数据最大值

   `min()`  ----    获取序列或者多个数据最小值

   `sun()`  ----    求序列中元素的数据和

   `eval()`   ----    解析字符串，将数据的最外层引号去掉

   `str()`    ----   将数据转化为字符串，只是在外层加一个引号

   `bin()`   ---   将数据转化为二进制数据

   `int()`   ---   将数据转化为十进制数据

   `oct()`   ---   将数据转化为八进制数据

   `hex()`   ---   将数据转化为十六进制数据

2. **自定义函数**

   ```
   def 函数名（形式参数1， 形式参数2，……，形式参数n)：
   	功能体
   	return 返回值
   ```

   * 函数名符合标识符规范

   * 形式参数  ---  形参，参与功能的未知项， 他是变量

   * 实际参数 ---  实参， 调用功能时给形参赋予的值

   * `return`   ---- 结束函数， 并且把结果返回到调用函数的位置，如果功能没有返回值，那么隐式返回 `return None`

3. **方法压栈**

   内存是分为不同区域的

   * 方法区：

     程序加载的时候把那些声明类函数都放在这个区域

     生命周期是和程序等长的

   * 栈区：

     存放的是运行的函数【将方法区的函数拷贝一份放入栈区】

     特点：函数运行完，内存被立即释放

     存储的结构特点：先进后出 【类似于向上开口的容器】

   * 堆区：

     存储的是列表、元组、字典、集合等对象的区域

     特点：对于对象才用的是引用计数的原则 【数据的地址被几个变量使用着，计数器就记录几】

     当计数器为0的时候，对象才在内存中被释放

   * 常量池：

     -5到256的数值

     字符串的数据

     特点：

     ​		第一次设置数据的时候，在此区域开辟一块空间进行存储，之后再使用的数据的时候，先检测这个数据在这个区域中是否存在，如果存在的话直接使用数据的地址了，如果不存在才在内存中存储一份

   * 静态区：

     存储全局变量和类属性

4. **全局变量和局部变量**

   * 函数有自己独立的作用域，在此作用域中声明的内容只能在此作用域中使用，出了作用域就不能使用了，在作用域中声明的变量就是局部变量

   * 全局变量 --- 作用范围是整个应用程序，直接在`.py`中声明的变量就是全局的，可以在任意位置使用

   * `global`   ----   在函数中声明全局的或者修改全局变量的值

     在函数内部可通过`global`修饰来使得变量由局部变量变成全部变量，进而修改全局变量的值

5. **位置参数**

   * 位置参数

     调用函数必须给位置参数传值，实参和形参必须是一一对应的

   * 关键字参数

     形参的个数比较多， 如果记不清形参的顺序， 可以使用关键字传值， 这个时候无所谓顺序`函数名（形参名=实参）`

   * 默认参数

     声明函数的时候 某个形参带有默认值， 这就是对应的默认参数

     使用场景：封装的功能是有未知项的，在大部分场景下，某个未知项的值是一样的，声明功能的时候只需要把这个未知项的对应的形参赋予默认值，调用函数的时候，可以不用给这个形参赋值，这时候就是用的是默认值，如果赋值，那么使用的是新值

   * 可变参数（不定长参数）

     使用场景：当声明功能的时候，不知道未知项的个数具体是多少就用可变参数

     ```
     *args --- 未命名形式的可变参数
     	传值的时候直接传递数据，每个数据之间使用逗号隔开
     	args可以接受多个数据，它是容器型的数据 --- 元组类型的数据
     	
     **kwargs --- 命名形式的可变参数又称为命名式关键字可变参数
     	传值的时候需要给数据设置一个标记名   格式：标记名=数据
     ```

     **注意事项**

     - 位置参数在默认参数后边
     - 如果位置参数在未命名式可变参数后边，调用函数的时候位置参数传值时要以关键字形式赋值
     - 位置参数必须在命名式关键字可变参数之前，默认参数也需要在命名式关键字可变参数之前

   * 匿名函数
     - 函数也是`function`类型的数据值
     - 函数名可以表示函数，函数()表示调用函数，结果的类型是函数功能返回值的类型
     - 匿名函数  ---  对简单功能的函数的简化
     - 格式`lambda 形参 …:函数返回值`
     - 经常被当做回调函数使用 eg:`key=lambda a, b :(a>b)-(a<b)`
     - 回调函数:被当做实参传递的函数