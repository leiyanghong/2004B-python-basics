''''
写一个生成手机号的方法，要求，1开头第二位非1和2的11位手机号
'''

import random

def random_tell():
    one = 1
    two = random.choice('3456789')
    three = random.randint(10000,99999)
    four = random.randint(1000,9999)
    tell = str(one)+str(two)+str(three)+str(four)
    return tell
print(random_tell())

