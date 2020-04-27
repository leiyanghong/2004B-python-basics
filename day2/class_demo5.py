''''
构造函数的继承
如果我们只是简单的在子类Chinese中定义一个构造函数，其实就是在重构。
这样子类就不能继承父类的属性了。
所以我们在定义子类的构造函数时，要先继承再构造，这样我们也能获取父类的属性了。
'''''
'''''
如果我们要给实例 c 传参，我们就要使用到构造函数，那么构造函数该如何继承，同时子类中又如何定义自己的属性？
继承类的构造方法：
1.经典类的写法： 父类名称.init(self,参数1，参数2，…)
2. 新式类的写法：super(子类，self).init(参数1，参数2，…)
'''


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = "weight"

    def talk(self):
        print("person is talking....")


class Chinese(Person):
    def __init__(self, name, age, language):  # # 先继承，再重构
        # 继承父类的构造方法，也可super(Chinese,self).__init__(name,age)
        # 调用第一个父类的同名方法，我们可以使用super()函数
        # super(Chinese,self).__init__(name,age)
        # 类名.同名方法(self)调用,调用其它父类同名方法 只能采用未绑定方式来调用
        Person.__init__(self, name, age)
        self.name = name
        self.age = age
        self.language = language

    def walk(self):
        print('is walking...')


c = Chinese('雷阳洪', "18岁", '会写python')
print(c.name, c.age, c.language)
