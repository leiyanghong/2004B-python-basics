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
#     def __new__(cls):
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
class Test():

    def __init__(self, *args, **kwargs):
        self.name = args
        self.age = kwargs
        self.__instance = {}

    def __call__(self, cls):  # __call__()的本质是将一个类变成一个函数（使这个类的实例可以像函数一样调用）
        def new(cls):  # 定义new函数,将类定义为装饰器
            if not hasattr(cls, 'instance'):  # hasattr()判断类实例中是否含有某个属性 判断是否为空
                cls.instance = object.__new__(cls)  # 为空就创建一个对象,下次如果再次调用这个类__instance就不会创建对象了
            return cls.instance  # 返回给new函数
        cls.__new__ = new  # 将new的对象赋值给__new__,__new__方法是用来创建对象的
        return cls  # 返回给调用者,cls就是传入的A类地址,将new出来的对象返回给原来的A类,实现单例模式


@Test("leiyh","18")
class A:
    pass
a = A()
a1 = A()
print(id(a))
print(id(a1))

'''
3、使用元类实现
'''
