# 1、使用字典推导式将下面字符串格式的数据，改成字典类型的数据
cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042;BAIDUID=B1005C9BC2EB28;sugstore=0;_cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_1sm=2;BDORZ=B490B5EBF6F3CD402'
cook = dict([i.split("=") for i in cook_str.split(";")])
print(cook)




# 2、 请描述什么是可迭代对象？什么是迭代器？ 迭代器和生成器的区别？
'''
迭代对象:可以使用for循环遍历的对象,我们称之为可迭代对象.
迭代器:迭代器可以看作是一个特殊的对象，每次调用该对象时会返回自身的下一个元素，从实现上来看，一个迭代器对象必须是定义了__iter__()方法和next()方法的对象。
生成器:如果函数中有yield我们称之为生成器
'''
# 3、设计一个调用一次返回文件中一行数据的生成器
def read_txt(file_path):
    with open(file_path,"r+",encoding='utf-8') as f:
        for i in f.readlines():
            yield i
read = read_txt("file.txt")
# 用__next__()内置函数会在每次循环中调用，该方法返回文件的下一行,如果到达结尾(EOF),则触发 StopIteration
print(read.__next__())
print(read.__next__())
print(read.__next__())
print(read.__next__())
# 如果到达结尾(EOF),则触发 StopIteration
# print(read.__next__())
# 循环读取文件的内容
for i in read_txt("file.txt"):
    print(i)




