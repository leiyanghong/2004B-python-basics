'''
类属性&实例属性&局部属性
'''

class Test():
    # 类变量
    name = "雷阳洪"

    # 实例变量
    def __init__(self, sex):
        self.sex = sex
        print("__init__函数的high变量为:",sex)

    def demo(self):
        # 局部变量
        high = 180
        print('雷阳洪身高为:',high)

    def sex(self):
        # 局部变量
        sex = "男生"
        print('雷阳洪是{}'.format(sex))
    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def class_method(cls):  # cls : 表示没用被实例化的类本身,可以随意命名,只是业内规定这样命名
        class_method = "class_method"
        return class_method

    # 静态方法
    @staticmethod
    def static_method():
        static_method = "static_method"
        print('实例方法调用:',static_method)


# 使用类调用类变量
print(Test.name,"超级无敌帅气")
# 使用对象调用类变量 此种方法不推荐
print(Test("男").name)
# 使用对象调用实例变量
print(Test("男").sex)
# 使用对象调用类实例方法
tes = Test("男")
print("demo函数返回的值为:",tes.demo())


