#
#
# # type()
#
# '''
# 加载自定义类：
# 把自定义类给到type.__call__()处理，返回了一个对象。并把对象赋值给MyMeta
# type.call()
# MyMeta.__new__(name,bases,dict)
# MyMeta.__init__(name,bases,dict)
#
#
# Test对象实例化：
# Test("1",2)
# MyMeta.__call__("1",2)
# object.__new__("1",2)
# object.__init__("1",2)
#
#
#
# '''
#
# class MyMeta(type):
#
#     def __new__(cls, name,bases,dct):
#         d = {}
#         for key in dct:
#             if (not key.startswith('__')):
#                 d[key.upper()] = dct[key]
#             else:
#                 d[key] = dct[key]
#         dct = d
#         return super().__new__(cls,name,bases,dct)
#
#
#
#
#
# class Test(object,metaclass=MyMeta):
#     aaa=''
#
#     pass
#
#
# print(Test.__dict__)
#
#
import gevent
import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from gevent import monkey



q = queue.Queue(100)
con = threading.Condition()
monkey.patch_all()

def set_data(data = None):
    con.acquire()
    for i in range(10000):
        if (q.full()):
            print("放了100个数据，队列满了")
            con.notify_all()
            con.wait()
            con.acquire()
        else:
            q.put("数据{}".format(i))
    else:

        for i in range(10):
            if q.full():
                print("队列满了，等一会再放")
                con.notify_all()
                con.wait()
                con.acquire()
                q.put(False)
                print("放入一个结束标记".format(i))
            else:
                q.put(False)
                print("放入一个结束标记{}".format(i))
        con.notify_all()
        con.wait(0.1)
        print("生产者退出")



def get_data(data = None):
    while True:
        print("线程{}，加锁".format(threading.current_thread()))
        # sleep(0.01)
        con.acquire()
        if(q.empty()):
            print("队列空了，等会再拿")
            con.notify_all()
            con.wait()
        else:
            res = q.get()
            print("线程{}，获取数据{}".format(threading.current_thread(),res))
            if not res:
                con.wait(0.1)
                break
            con.release()
    print("线程{}，结束".format(threading.current_thread()))

'''
使用线程池实现
'''
pool1 = ThreadPoolExecutor(max_workers=11)

pool1.submit(set_data)

[pool1.submit(get_data) for i in range(10)]

pool1.shutdown()

'''
使用协程池实现
'''
create = gevent.spawn(set_data,q)
customers  = [gevent.spawn(get_data,q) for j in range(10)]

create.join()
gevent.joinall(customers)
