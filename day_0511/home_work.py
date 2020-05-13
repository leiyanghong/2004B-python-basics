#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
使用至少三种方案实现单例模式：
'''
'''
1、重写类中的new方法
'''

# class Test(object):
#     __instance = None  # 私有变量,权限只针对类本身调用
#
#     def __init__(self):
#         print("init方法")
#
#     def __new__(cls):  # __new__方法是用来创建对象的
#         print('------new方法--------')
#         if not cls.__instance:  # 判断__instance是否为空
#             cls.__instance = object.__new__(cls)  # 为空就创建一个对象,下次如果再次调用__instance就不会创建对象了
#         return cls.__instance  # 将object类new的类返回给调用者
#
#
# t = Test()
# t2 = Test()
# print(id(t))
# print(id(t2))

'''
2、使用装饰器实现（用类装饰器）
'''
# class Test():
#
#     def __init__(self, *args, **kwargs):
#         self.name = args
#         self.age = kwargs
#         # self.__instance = {}
#
#     def __call__(self, cls):  # __call__()的本质是将一个类变成一个函数（使这个类的实例可以像函数一样调用）
#         def new(cls):  # 定义new函数,将类定义为装饰器
#             if not hasattr(cls, 'instance'):  # hasattr()判断类实例中是否含有某个属性 判断是否为空
#                 cls.instance = object.__new__(cls)  # 为空就创建一个对象,并且赋值给原类下次如果再次调用这个类__instance就不会创建对象了
#             return cls.instance  # 返回给new函数
#         cls.__new__ = new  # 将new的对象赋值给__new__,__new__方法是用来创建对象的
#         return cls  # 返回给调用者,cls就是传入的A类地址,将new出来的对象返回给原来的A类
#
#
# @Test("leiyh","18")
# class A:
#     pass
# a = A()
# a1 = A()
# print(id(a))
# print(id(a1))

# '''
# 使用函数装饰器实现单例模式
# '''
# def fun_a(cls):  # cls代表的是传入的类实例本身
#     instance = {}
#     def function(*args,**kwargs):  # 接收类传入的参数
#         if not instance:  # 判断instance是不是为空字典
#             instance[cls] = cls(*args,**kwargs)  # 赋值操作,将实例化的A类赋值存到instance字典中,下次如果再进行实例化操作,会去判断该字典是否为空的情况
#         return instance[cls]  # 返回A类的地址
#     return function  # 返回生成的类实例
#
# @fun_a
# class A():
#     pass
# a = A()  # 当实例化就去调用function函数
# a1 = A()
# print(id(a))
# print(id(a1))

'''
3、使用元类实现单例模式
'''


# def move(self):
#     print('---move----方法')
#
#
# # 元类type创建类需要三个参数，
# # 第一个为类名（str类型）,即类的_name_属性
# # 第二个为继承的父类（tuple类型）,
# # 第三个是属性和方法{dict类型}
# Use = type('User', (object,), {'name': '小明', 'move': move})
# u = Use()
# u.move()

# # 自定义元类
# class MyMeta(type):  # 继承type元类,自定义元类
#     def __init__(cls,name,bases=None,dict=None):  # __init__方法是用来初始化类对象
#         print("init函数已经执行")
#         # super() 函数是用于调用父类(超类)的一个方法。
#         super().__init__(name,bases,dict)  # 重写type父类__init__
#
#     # __new__方法是用来创建对象,__new__方法的会先于__init__方法执行
#     def __new__(cls, *args, **kwargs):
#         print("new函数已经执行")
#         # 如果要得到当前类的实例，应当在当前类中的__new__()方法语句中调用当前类的父类 (type)的__new__()方法。
#         return super().__new__(cls,*args, **kwargs)
#
#     # __call__()方法是将一个类变成一个函数（使这个类的实例可以像函数一样调用）
#     def __call__(self, *args, **kwargs):
#         print('call函数已经执行')
#         return super().__call__(self,*args, **kwargs)
#
#
# class Test(metaclass=MyMeta,):
#     attr = "我是attr"


class SingLeton(type):  # 自定义元类
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)  # 重写type父类__init__
        self.__instanc = {}  # 定义一个为空的__instanc的私有属性
    def __call__(self, *args, **kwargs):
        #判断__instanc属性是否为空
        if not self.__instanc:
            # 重写type父类__call__ 赋值给__instanc属性
            self.__instanc = super().__call__(*args, **kwargs)
        return self.__instanc

class TestSingLeton1(metaclass=SingLeton):
    def __init__(self,arg):
        self.arg = arg

class TestSingLeton2(metaclass=SingLeton):
    def __init__(self, arg):
        self.arg = arg

t = TestSingLeton1("你好,雷阳洪")
print(id(t))
t2 = TestSingLeton1("你好,马化腾")
print(id(t2))



