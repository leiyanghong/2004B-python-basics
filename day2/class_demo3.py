'''
类方法&实例方法&静态方法
'''


class A():
    bar = 1
    num = "类变量"

    # 实例方法
    def func1(self):
        print("func1")

    @classmethod
    def func2(cls):
        print("func2")
        print(cls)
        print(cls.bar)
        cls().func1()  # 调用 foo 方法
    # 静态方法
    @staticmethod
    def func3():
        print("func3")

# 类调用类方法
A.func2()

# 类调用静态方法
A.func3()
# 对象调用静态方法
a = A()
a.func3()

