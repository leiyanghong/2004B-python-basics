# Sequences and hashes
# 序列和散列操作
# 序列索引
str1 = "果芽软件"
print(str1[0])
print(str1[-1])

# 序列切片
str2 = "果芽测开学院"
# 取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str2[0:2])
# 隔 1 个字符取一个字符，区间是整个字符串
print(str2[::2])
# 取整个字符串，此时 [] 中只需一个冒号即可
print(str2[:])

# 序列相加
print("果芽" + "测开" + "学院")

# 序列相乘
st = '果芽测开学院'
print(st * 3)

# 检查元素是否包含在序列中,如果在该序列中,返回true,没有返回false
st = '果芽测开学院'
print('开' in st)

'''
Python提供了几个内置函数，可用于实现与序列相关的一些常用操作。
'''
values = (1, 2, 3, 5, 4, 6, 7)
# 计算序列长度
print(len(values))
# 找出序列中的最大元素
print(max(values))
# 找出序列中的最小元素
print(min(values))
# 将序列转换为列表。
print(list(values))
# 将序列转换为字符串。
print(str(values))
# 计算元素和
print(sum(values))
# 对元素进行排序。
print(sorted(values))
# 反向序列中的元素。
print(list(reversed(values)))
# 将序列组合为一个索引序列，多用在 for 循环中。
print(list(enumerate(values)))
# count 统计字符串出现的次数  count(sub,start,end )
count = "21309120301928490328409380578979"
count1 = '0'  # 定义搜索的子字符串
print("0出现了:", count.count(count1, 0, len(count)), "次")  # 定义搜索范围的索引
# find检测字符串中否包含某子串
print(count.find(count1,0,len(count)))
# index()检测字符串闹钟是否包含某子串  当指定的字符串不存在时，index() 方法会抛出异常。
print(count.index(count1,0,len(count)))
