# 命名元组 collections模块中的namedtuple函数

# namedtuple:接收两个参数，第一个创建的类型名称，第二个列表
from collections import namedtuple

student = namedtuple("studen",["name","age","sex"])
# 传入value
s = student("leiyh",18,"sex")
# 根据指定key获取value
print(s.name)

# 三目运算符
a = 12
b = '成功'
c = '失败'
print(c if a>11 else b)

# 推导式
'''
列表推导式
'''
list3=[i for i in range(100)]
print('list3的值为：',list3)
'''
列表推导式中添加 if 条件语句
'''
# 添加if判断条件,将满足的条件i存到列表中
if_list = [i for i in range(100) if i % 2 == 0]
print(if_list)

  


