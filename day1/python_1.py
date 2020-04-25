#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
1、使用for循环反序输出字符串"abcdefghijklmnopqrstuvwxyz"
'''

def daoxu():
    str = "abcdefghijklmnopqrstuvwxyz"
    str2 = ''
    for i in str:
        str2 = i + str2
    print(str2)




'''
写出下列递归函数的伪代码：
'''
d = {"name":"leiyh","sex":"男","age":"18","人物信息":['leiyh','男',18],"元组":(0,1,2,3,4)}

'''
第一次遍历:
search("leiyh")
search("男")
search("18")
search(['leiyh','男',18])
第二次遍历:
第二次遍历的是人物信息字段下的数组
search("leiyh")
search("男")
search(18)
'''

def search(d):
    # 判断是否是字典,满足遍历
    if isinstance(d,dict):
        # 遍历获取key: 'name', 'sex', 'age', '人物信息' 用key值遍历获取value
        for key in d:
            # 每次遍历之后都会重新调用search()函数对里层的value重新判断是否是字典或者数组
            search(d[key])
    # if条件不满足,就判断d是否是数组
    elif(isinstance(d,list)):
        # 遍历获取d字典所有key
        for i in d:
            # 引用key 重新调用search()函数 重新判断d字典属性 d字典第二次判断的key是:人物信息
            search(i)
    # 判断是否是元组,满足获取该元组里面所有value
    elif(isinstance(d,tuple)):
        for i in d:
            # 递归自调用遍历
            search(i)
    # 直到上述条件都不满足输出打印d字典
    else:
        print(d)


'''
编写一个过滤掉列表中空字符串和空值的方法 ，并返回过滤后的list
效果：
方法传入[’’,‘hello’,None,‘python’] 返回[‘hello’,‘python’]
'''

def lis(l):
    s = []
    # 遍历传入的参数,拿到每一个值
    for i in l:
        # 判断每个值是否为空 是否为None
        if i == '' or i is None:
            # 满足就通过,不打印
            pass
        else:
            # 反之就追加到s数组里
            s.append(i)
    # 返回处理之后追加的s数组
    return s
l = lis(['','hello',None,'python'])
print(l)

'''
4、编写一个计算一个元祖中所有数据和的方法，并把计算结果返回
'''
def sum_tuple(tu):
    sum = 0
    for i in tu:
        sum += i
    return sum
print(sum_tuple(tu = (1,2,3,4,5,6,7,8)))