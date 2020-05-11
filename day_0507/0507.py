# # 递归函数
# def jie_func(n):
#     # 判断n是否等于1,如果等于则返回1,
#     if n == 1:
#
#         return n
#     else:
#         # 不等于则继续调用自身函数进行判断
#
#         return n * jie_func(n - 1)
#
#
# res = jie_func(5)
# print(res)
# # zip()函数的作用
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = zip(a, b)
# print(list(c))


# # 纯函数
# # 函数func1返回的结果为两个参数相加的结果
# def func1(a, b):
#     return a + b
#
#
# var1 = 100
#
#
# # 函数func2返回的结果为参数a和外部变量var1相加的结果
# def func2(a):
#     return var1 + a
#
#
# print(func2(2))
# 在上面的两个案例中func1返回的结果只受传入的参数的影响，而func2不仅受传入参数的影响而且还会受外部变量var1的影响，像func1这样的返回值只跟传入参数有关的函数我们把它叫做纯函数。

# # 内置函数
# # lambda 匿名函数 传入参数:参数的表达式
# # map()根据提供的函数对指定序列做映射。
# m = map(lambda x: x ** 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 根据提供的函数对指定序列做映射。
# print(list(m))
# # filter()函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# f = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 将余0的数值过滤出来
# print(list(f))
# # zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# z = zip(["name", "age", "sex"], ["xuepl", 18, '男'])
# print(dict(z))

# # 偏函数作用
# # 原始方案
# def filter1(l):  # 定义一个过滤出列表中偶数的方法
#     return list(filter(lambda x: x % 2 == 0, l))
# # 调用函数对列表进行过滤
# print(filter1([1, 2, 3, 4, 5, 6, 7, 8]))
# # 使用偏函数解决
# from functools import partial # 导入partial模块
# # 通过偏函数创建一个新函数，提前传入原函数所需要的参数，让我们在调用的时候更加简单。
# filter2 = partial(filter,lambda x: x % 2 == 0)
# # 使用偏函数过滤列表数据
# print(list(filter2([1,2,3,4,5,6,7])))
# # 偏函数传递关键字参数
# def info(age,name):  # 准备一个原函数
#     print("我叫{},我{}岁了".format(name,age))
# info2 = partial(info,age=18)  # 定义偏函数时设置默认值
# info2(name = "雷阳洪")  # 使用偏函数的时候，注意要使用关键字的方式传参,要符合关键字传参的顺序

# # 闭包函数作用
# #闭包函数，其中 exponent 称为自由变量
# def a(exponent):
#     def b(base):
#         return exponent  ** base
#     return b
# square = a(2)  # 计算一个数的平方 拿到b函数的返回值,此时square=b(base) return 2 ** base
# print(square(3)) # 计算2的立方  此时square=b(base) return 2  ** 2
# def test(name):
#     def test_in(str):
#         print(name+str)
#     return test_in
# name1 = test("leiyh")
# name1("是帅哥")


# # 装饰器-语法糖
# def fun_a(func):
#     return 'hello'
#
#
# @fun_a  # 这种写法，等价于  fun_b=fun_a(fun_b)
# def fun_b():
#     pass
# print(fun_b)

# # 装饰器的原型
# import time
# def showtime(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print('spend is {}'.format(end_time - start_time))
#
#     return wrapper
#
# def foo():
#     print('foo..')
#     time.sleep(3)
#
# foo1 = showtime(foo)
# # foo1()就是调用wrapper()函数
# foo1()

# # 不带参数的装饰器
# import time
# def showtime(func):
#     def wrapper():
#         start_time =  time.time()
#         func()  # 该函数就是传入进来的too()函数,执行foo里面的代码
#         end_time = time.time()
#         print("spend is {}".format(end_time-start_time))
#     return wrapper
#
# @showtime
# def foo():
#     print("foo..")
#     time.sleep(3)
#
# @showtime
# def doo():
#     print("doo...")
#     time.sleep(2)
# # 调用打了装饰器的函数会先执行装饰器,然后再执行原函数
# foo()
# doo()


# * 给装饰器传参
import copy
import time

# # * 给装饰器传参
# def fun_a(arg_a):
#     def swap(func):
#         def function(*args,**kwargs):
#             print("接收到了装饰器传过来的参数",arg_a)
#             print("函数执行前的操作")
#             res = func(*args,**kwargs)
#             print('函数执行后的操作')
#             return res
#         return function
#     return swap
#
# @fun_a('arg_a')
# def fun_b(arg_b):
#     print(arg_b)
# a = fun_b('执行fun_b函数')

# def main(arg_a):
#     print('是main方法')
#     def swap(func):
#         def child(*args,**kwargs):
#             print("它打印前执行函数…",arg_a)
#             res = func(*args,**kwargs)
#             print("它打印后执行函数…")
#             return res
#         return child
#     return swap
#
# @main("arg_a")
# def alone(alone_a):
#     print("我是alone方法...",alone_a)
#
# alone("传入alone参数,*args,**kwargs")

# import time
# from functools import wraps  # wraps能保留原有函数的名称和docstring
#
# def log_level(level="DEBUG"): # 该参数是装饰器里面的原函数的装饰器传入的参数,这里是写死的
#     def log_format(func): # 该参数是原函数名
#         @wraps(func)
#         def format(*args,**kwargs): # 该参数对应的是原函数传入的参数
#             logtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # 取得本地时间
#             print("[{}]{}: ".format(level, logtime), end='') # 输出打印时间
#             return func(*args,**kwargs) # 返回原函数的参数
#         return format
#     return log_format
#
#
# @log_level()
# def log_1(time):
#     print("你好,欢迎来到雷阳洪python3装饰器学习课堂,现在本地时间是{}".format(time))
#
# log_1(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))



# 给类加装饰器
import time
from functools import wraps
# class Logger:
#     def __init__(self,level='DEBUG'):
#         self.level = level
#     def __call__(self, func):
#         @wraps(func)
#         def log_format(*args, **kwargs):
#             log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#             print("[{}]{}: ".format(self.level, log_time), end='')
#             return func(*args, **kwargs)
#         return log_format
#
# @Logger()
# def log1(name):
#     print("Hello,Welcome to Python...{}".format(name))
#
# @Logger('Error')
# def log2():
#     print("Python ...")
#
# log1("leiyanghong")
# time.sleep(1)
# log2()

# # 装饰器装饰类
# def f2(f_value):
#     def f1(func):
#         def function(*args, **kwargs):
#             print(f_value)
#             print('-----执行装饰器实现的功能-------')
#             return func(*args, **kwargs)
#         return function
#     return f1
# @f2("这是往装饰器里面传参的值")
# class Hero(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print('正在初始化')
#     def move(self):
#         print('%s在快速移动'%self.name)
#
# laoli=Hero('老李',19)
# print(laoli.name)


# # 装饰器嵌套
# def fun_a(func):
#     print("装饰器fun_a")
#     def function():
#         res=func()
#         return res
#     return function
# def fun_b(func):
#     print("装饰器fun_b")
#     def function():
#         res=func()
#         return res
#     return function
# def fun_c(func):
#     print("装饰器fun_c")
#     def function():
#         res=func()
#         return res
#     return function
#
# @fun_a
# @fun_b
# @fun_c
# def fun():
#     print("执行fun函数")
# fun()

# property setter deleter   首先要定义(property)  然后才能setter deleter操作




'''
1、定义一个用户类，包含用户名，密码，手机号三个属性，无方法
要求：使用@property装饰器实现对上述三个属性的修改检查（提示数据检查用正则表达式实现，正则表达式可以百度）
用户名：长度6-8位的数字、字母
密码：长度4-10位，必须包含字母和数字
手机号：11位数字
'''
import re

class User():
    @property
    def username(self):
        return self.username
    @username.setter  # 修改
    def username(self,value):
        if re.match("^[a-zA-Z0-9]{6,8}$", value):
            print("用户名合法:{}".format(value))
        else:
            print("用户名不合法,错误用户名：长度6-8位的数字、字母")
    @property
    def pwd(self):
        return self.pwd
    @pwd.setter  # 修改
    def pwd(self, value):
        if re.match("^[a-zA-Z0-9]{4,10}$", value):
            print("密码合法:{}".format(value))
        else:
            print("密码不合法,错误密码：长度4-10位，必须包含字母和数字,错误的密码为:{}".format(value))
    @property
    def phone(self):
        return self.phone
    @phone.setter  # 修改
    def phone(self, value):
        if re.match("1\d{10}", value):
            print("手机号合法:{}".format(value))
        else:
            print("手机号不合法,必须满足11位数字,且首位为1的手机号.错误的手机号为:{}".format(value))
user = User()
user.username = "asA111"
user.pwd = "asA111"
user.phone = "13264673267"



# 课堂作业
# '''
# 1、使用递归函数求100以内数的和
# '''
# def sum(max):
#     if max ==1:
#         return 1
#     else:
#         return max + sum(max-1)
# print(sum(100))
#
# '''
# 2、使用实现一个统计函数运行时间的装饰器
# '''
# import time
#
# def wrapper(func):
#     def count_time(*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         end_time = time.time()
#         time1 = end_time-start_time
#         return time1
#     return count_time
#
# @wrapper
# def wsaaccept():
#     time.sleep(2)
#
# print(wsaaccept())


