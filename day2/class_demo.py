# 类



class TheFistDemo:
    # 构造方法
    # init() 方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        print("这是一个构造方法")
        print("我的名字叫{},我是{},我{}岁了".format(name, sex, age))

    # 定义一个类变量
    url = 'https://www.stu.guoyasoft.com/'

    # 定义一个say方法
    def say(self, content):
        print(content)

    # del()析构方法一般不要自己定义，使用对象默认的即可
    def __del__(self):
        print("对象已经被删除")


'''
实例化对象,新增,调用,删除变量
'''
# 创建一个名为 demo 的 TheFirstDemo 类对象
# 创建对象时会调用类的构造方法，如果构造函数有多个参数时，需要手动传递参数
demo = TheFistDemo("雷阳洪", "男生", 18)
# 访问类中的属性
print("果芽学生端的url:",demo.url)
# 调用类方法
demo.say("雷阳洪,你好")
# 为上例中的demo对象增加一个money的实例变量
demo.high = 170
print("新增一个实例变量,雷阳洪身高:",demo.high,"cm")
# 删除high变量 关键字:"del"
del demo.high
# print(demo.high)



'''
给对象动态添加方法
'''
# 定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对clanguage的foo方法赋值（动态绑定方法）
demo.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
demo.foo(demo)
# 使用lambda表达式对clanguage的bar方法赋值
demo.bar = lambda self : print("lanmbda表达式",self)
demo.bar(demo)

# 使用MethodType动态绑定方法
# 先定义一个info2函数
def info2(self):
    print("---info2函数---", self)
# 导入MethodType
from types import MethodType

# MethodType() 两个参数:第一个参数填写需要定义的函数名 第二个参数填写需要添加的对象名
demo.info2 = MethodType(info2,demo)
demo.info2()