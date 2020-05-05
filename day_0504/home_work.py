#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
4、使用列表推导式+join方法把下列字典转成键值对
'''
d = {"username": 'xuepl', "sex": '男', "age": 18}
d = [keys + "=" + str(values) for keys, values in d.items()]
print(" ".join(d))

'''
5、使用列表推导式过滤掉长度小于3的字符串，并将剩下的字符串转换成大写字母
'''
lst=["1","2","3","4","8","weeff","bdskjk","nsdjj"]
lst1 = [i.upper() for i in lst if len(i)>3]
print(lst1)


