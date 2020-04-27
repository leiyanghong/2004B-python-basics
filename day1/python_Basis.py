#!/usr/bin/python3

'''
编程练习之统计字符
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
'''
def statistical_characters():
    # 获取需要处理的数据
    # str = input('请输入英文字母+空格+数字+其它字符的数据:')
    str = 'wqeoqwehoqwQWQWQWQ1231232423    !@^!%#&^@*#'
    # 初始化字母,数字,空格,其它符号,存到字典中
    dic = {'字母': 0, '数字': 0, '空格': 0, '其它符号': 0}
    # 遍历数据判断是否符合要求,满足自增1
    for i in str:
        # isalpha() 判断每次i的值是否为英文字母
        if i.isalpha():
            dic['字母'] += 1
            # isspace()判断每次i的值是否为空格
        elif i.isspace():
            dic['空格'] += 1
            # isalnum()判断每次i的值是否为数字
        elif i.isalnum():
            dic['数字'] += 1
            # 反之100%满足该条件
        else:
            dic['其它符号'] += 1
    # 打印最终的数据
    print(dic)
statistical_characters()

'''
编程小练习之完数
一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数
思路:第一步，将所有因子追加到一个列表中，第二步，将符合条件的数字打出来
'''

# 声明一个空数组
l = [ ]
# 外层for遍历获取1-1000的值
for n in range (1,1000):
    # 里层for根据外层for遍历  # 判断n%a是否余0 满足追加到l数组中
    for a in range (1,n):
        if n%a ==0:
            l.append(a)
    # 判断l数组的和跟n是否相等
    if sum(l)==n:
        # 满足打印输出l数组
        print (l)
        # 满足打印输出n变量
        print (n)
    # 清空list,做接下来的循环追加
    l = []

