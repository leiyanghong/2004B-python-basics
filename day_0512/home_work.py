''''''
'''
首先分清init new call 方法的含义
init:创建完对象后调用，对当前对象的实例的一些初始化，无返回值,即在调用__new__之后，根据返回的实例初始化；
new:创建对象时调用，返回当前对象的一个实例;
call:如果类实现了这个方法，相当于把这个类型的对象当作函数来使用
很显然,如果是要修改类中的属性必须要在new方法里面去重新定义元类,获取类的属性以及方法,最后再将方法修改成大写
'''


class Mymeta(type):
    def __new__(cls, class_name, class_bases, class_dict):
        # print(class_name)  # 获取生成的类名
        # print(class_bases)  # 获取该属性返回所有直接父类组成的元组
        print('类字典:', class_dict)  # 获取类的字典,里面寸的是类
        # 将class_dict的key value 取出,再将所有的属性和方法转成大写
        class_dict1 = {}
        for key, value in class_dict.items():  # 获取class_dict的key value
            if not key.startswith('__'):  # 判断key的值不能为'__',才执行下面的代码
                class_dict1[key.upper()] = value  # 赋值操作,将满足的value赋值给class_dict1字典中,以key存储,将key转换成大写
            else:
                class_dict1[key] = value  # 反之,不做转换大写操作,只做赋值操作
        return super().__new__(cls, class_name, class_bases, class_dict1)  # 返回实例化出来的实例


class Chinese(object, metaclass=Mymeta):
    country = 'China'
    tag = '123'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


print(Chinese.__dict__)
