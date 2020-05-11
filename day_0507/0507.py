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
# 给类加装饰器
# 语法糖执行逻辑 从里到外执行  调用函数执行逻辑 从外到里执行   分开理解语法糖 和 调用逻辑
# property setter deleter   首先要定义(property)  然后才能setter deleter操作


copy