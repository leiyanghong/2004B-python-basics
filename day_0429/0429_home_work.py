#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
1、合并下列两个字典：
a = {"Content-type":'application/json'}
b={"token":'sdisidfisjfiasifdmaisdfi'}
'''
# 合并两个字典
a = {"Content-type": 'application/json'}
b = {"token": 'sdisidfisjfiasifdmaisdfi'}

# 方法1
dic1 = {}
dic1.update(a)
dic1.update(b)
print("第一种方法:", dic1)
# 方法2
dic2 = dict(**a, **b)
print("第二种方法:", dic2)
# 方法3
dic3 = {}
for keys, values in a.items():
    dic3[keys] = values
for keys, values in b.items():
    dic3[keys] = values
print("第三种方法:", dic3)

'''
2、把下列字典转成字符串格式
a = {"username":'薛鹏垒',"password":'123456'}
'''
a = {"username": '薛鹏垒', "password": '123456'}
print('转换之后的字典属性为:', type(str(a)))

'''
根据下列数据，输出下列表格
d = {"苹果":6,"桔子":3.2,"香蕉":2.5,"葡萄":14.8,"红提":15,"西瓜":1.5}
表格格式要求：
1、表格总宽度30个字符
2、项目列宽度20个字符，表格内容左对齐
3、价格列宽度10个字符，价格保留两位小数，且居中
'''
d = {"苹果": 6, "桔子": 3.2, "香蕉": 2.5, "葡萄": 14.8, "红提": 15, "西瓜": 1.5}
print("=====" * 6)
d2 = {"项目": "价格"}
for keys, values in d2.items():
    print("{:<20s}{:^10.2s}".format(keys, values))  # # 项目列宽度20 内容左对齐 价格列宽度10  保留两位小数，且居中
# print("{:<20s}""{:^10s}".format("项目","价格"))  # 项目列宽度20 内容左对齐 价格列宽度10  保留两位小数，且居中
print("-----" * 6)
for keys, values in d.items():
    print("{:<20s}{:^10.2f}".format(keys, values))  # # 项目列宽度20 内容左对齐 价格列宽度10  保留两位小数，且居中
