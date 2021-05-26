1. **递归算法**

   在函数的内部调用了函数
   
   
   
     **注：递归一定要有基例（出口 已知项），递归的层次不要太深，否则人会造成栈溢出**

2. **函数嵌套**

   在一个函数中声明另一个函数

   * 调用方法：

     * 直接调用

       在外部函数中调用，然后通过调用外部函数来实现内部函数的调用

       ```
       def out1():
           print('外层函数')
           def inner():
               print('内层函数')
           inner()
       
       
       out1()
       ```

       

     * 间接调用

       把内部函数当做外部函数的返回值

       ```
       def out2():
           print('外层函数')
           def inner():
               print('内层函数')
       
           return inner
       
       print(out2())
       ```

       

   * 内层函数中修改外层函数的变量

     `nonlocal`  ----   告诉解释器 变量不是内部函数声明的需要向外找，找到外部函数的这个变量再进行修改

   **闭包**

   ​	内部函数对外部函数作用域里变量的引用

   ​	闭包内的变量为闭包私有，不会因为外部函数的结束而消失。

   ```
   def outer1():
       num = 10
       def inner():
           # 告诉解释器 num不是inner自身内部声明的  向外找  找到外部函数的num
           nonlocal num
           num += 20 # 修改的外层的num的变量
           print('内层函数中num的值是', num)
   
       return inner
   
   func = outer1() # func获取的是inner的地址
   
   func() # num为30  # 此时num的值已被修改了
   
   func() # num是多少50 # 这里调用的时候 获取的是修改之后的
   ```

   

3. **装饰器**

   在不修改原有功能的基础上，对功能增加额外的内容

   装饰器就是闭包结构

   ```
   def check_login(func): # func这个形参是来记录被装饰的函数
       # 额外的功能写在内层函数中
       def inner():
           username = input('用户名:')
           password = input('密码：')
           if username == 'admin' and password == '123456':
               # 执行被装饰功能
               func()
           else:
               print('登录失败')
       return inner
   
   
   @check_login
   def collection():
       print('收藏')
   
   
   @check_login
   def like():
       print('点赞')
   
   
   # collection()
   # like()
   
   ```

   装饰器添加的本质：

   当执行到@语法的时候

   其实装饰器的外层函数就被调用了， 并且把被装饰的功能赋值给了外层函数的形参`@check_login`

    `def like():`

   解释器做的事情是：
   `like = check_login(func=like)`
   把外层函数调用完成之后 会把内层函数当做返回值 返回到调用的位置
   由于这个动作是解释器来完成的， 接受返回值的变量名 是怎么定义的？？？？

   被修饰的函数名是什么 就使用对应的名来接受的

   换句话说 当装饰完成之后  原有的功能名对应的地址发生了变化 指向了装饰器的内层函数

   ```
   def func1(func):
   	def func2():
   		print('a')
   		return func()
   	retrun func2
   
   
   @func1  
   def myprint():
   	print('hello, print')
   	
   	
   myprint()  # 等价于 func2() + func()
   ```

   执行逻辑：

   `@func1`实际上是`func1(myprint)() -->func2()  `接收被装饰的函数作为参数， 而且还要再调用一次

   `func2()  `的执行过程`func2()  --> print('a') --> return func() --> myprint() --> print('hello, print')`