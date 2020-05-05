#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
2、合并下列两个列表，并对列表中的数据去重
'''
a = [1, 2, 3, 4, 5, 6, 7]
b = [5, 6, 7, 8, 9, 10]
print(list(set(a + b)))

'''
3、过滤掉下列列表中的负值
'''
a = [2, 3, 4, -1, -2]
# 利用列表推导式 简化代码实现for循环 if判断
b = [i for i in a if i > 0]
print(b)





