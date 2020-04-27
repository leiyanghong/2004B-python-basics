# 类的继承

# 继承的定义
class Person():  # 定义一个父类
    def talk(self):  # 定义一个类函数
        print("person is talking....")


class Chinese(Person):  # 定义一个子类,继承Person类
    def walk(self):  # 在子类定义一个类函数
        print('is walking...')


c = Chinese()  # 实例化对象
c.talk()  # 调用父类的方法
c.walk()  # 调用本身的方法
