# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # leiyh
#
# import threading
#
#
# # 定义线程要调用的方法
# def action(*add):
#     for i in add:
#         # threading.current_thread() 返回当前执行的线程
#         # getName() 获取当前执行该程序的线程名
#         # 输出打印遍历每次执行的线程名字 + 每次遍历的参数
#         print(threading.current_thread().getName() + " " + i )
#
# # 定义为线程方法传入的参数
# my_tuple = ("http://stu.guoyasoft.com",
#             "http://www.guoyasoft.com",
#             "http://www.guoyasoft.com:8001")
#
# # # 创建线程
# # # threading.Thread 创建一个线程,传入方法和参数
# # thread = threading.Thread(target=action,args=my_tuple)  # target给定一个任务的方法名 args给target指定方法传递的参数
# # # 启动线程
# # thread.start()
# # thread.join()
#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in my_tuple:
#             action(i)
#
#
# t1 = MyThread()
# t1.start()
# t1.join()
#
# # def test_add():
# #     # print("当前执行的线程{}----".format(threading.current_thread()))
# #     # print("正在运行的所有线程:{}".format(threading.enumerate()))
# #     # print("正在运行的线程数量:{}".format(threading.active_count()))
# #     s = 0
# #     for i in range(1000):
# #         s = s + i
# #     print(s)
#
# # thread = threading.Thread(target=test_add)
# # thread2 = threading.Thread(target=test_add)
# # thread.start()
# # thread2.start()
# # # join( [timeout] ) 阻塞当前线程,默认等待指定的线程执行结束  timeout是阻塞时间,超过规定时间就停止阻塞
# # thread.join()
# # thread2.join()
# # print("当前执行的线程{}----".format(threading.current_thread()))
# # print("主线程结束")
#
# # # 重写Thread类,在run方法里面去执行任务
# # class MyThread(threading.Thread):  # 继承threading.Thread
# #     def run(self):  # 重写run方法,待执行的任务
# #         test_add()
# #
# #
# # t1 = MyThread()
# # t2 = MyThread()
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
import queue
import threading
import time

# # 守护线程
# def test_add():
#     print("当前执行的线程{}----".format(threading.current_thread()))
#     # print("正在运行的所有线程:{}".format(threading.enumerate()))
#     # print("正在运行的线程数量:{}".format(threading.active_count()))
#     s = 0
#     for i in range(1000):
#         time.sleep(0.01)
#         s = s + i
#     print(s)
#
#
# t1 = threading.Thread(target=test_add)
# t1.daemon = True  # 表示当前线程就是t1的守护线程 ,当设置了守护线程,如果主线程运行结束,t1子线程也就结束运行
# t1.start()
# time.sleep(1)
# print("主线程结束")


# # 互斥锁
# a = 0
# lock = threading.Lock()  # 创建一把锁 互斥锁
# def add_one():
#     lock.acquire()  # 加锁,已锁定 其他线程就无法加锁成功
#     try:
#         global a
#         for i in range(10000000):
#             b = a + 1
#             # raise NameError("线程挂掉了")  # 如果程序挂掉之后会无法对锁进行释放,会出现死锁的情况,所以要用try finally 防止程序出错脚本无法运行的问题
#             # time.sleep(0.001)  # 阻塞线程运行
#             a = b
#     finally:
#         lock.release()  # 结束锁定,其他锁就能使用
#
#
# # 创建5个线程
# thread_list = [threading.Thread(target=add_one) for i in range(5)]
# for i in thread_list:
#     i.start()
# for i in thread_list:
#     i.join()
# print(a)


# # 线程锁的概念-不要用多把锁,很容易造成死锁的情况
# a = 0
# lock1 = threading.Lock()  # 创建一把锁 互斥锁
# lock2 = threading.Lock()  # 创建一把锁 互斥锁
# def add_one():
#     print("线程{}进入方法add_one".format(threading.current_thread()))
#     lock1.acquire()  # 加锁,已锁定 其他线程就无法加锁成功
#     lock2.acquire()  # 加锁,已锁定 其他线程就无法加锁成功
#     print("线程{}开始计算".format(threading.current_thread()))
#     lock1.release()  # 结束锁定,其他锁就能使用
#     time.sleep(0.1)  # 线程1 lock2 锁定
#     lock1.acquire()
#     global a
#     for i in range(10000000):
#         b = a + 1
#         a = b
#     lock2.release()
#     lock1.release()
#     print("线程{}退出方法".format(threading.current_thread()))
#
# # 创建5个线程
# thread_list = [threading.Thread(target=add_one) for i in range(5)]
# for i in thread_list:
#     i.start()
# for i in thread_list:
#     i.join()
# print(a)

# con = threading.Condition()  # 实例化类,该类默认自带互斥锁功能
# '''
# 生产者:1个人往锅里放丸子
# 消费者:3个人负责吃丸子
# '''
# ball = []
#
# # 定义生产者
# def set_data():
#     for i in range(10):
#         con.acquire()  # 加锁
#         for j in range(20):
#             ball.append("丸子")
#         print('放了{}个丸子进去,吃货们快来吃吧~'.format(len(ball)))
#         con.notify_all()  # 通知所有的等待线程从wait()方法后的语句开始运行
#         con.wait()  # wait首先会释放当前锁,并进入阻塞状态
#
# # 定义消费者
# def get_data():
#     while True:
#         con.acquire()  # 加锁,其他人都别动
#         time.sleep(0.5)  # 每隔0.5s拿一次丸子
#         if len(ball) == 0:  # 判断锅里有没有丸子,如果有就去拿丸子,没有就把其它线程唤醒,把锁释放掉,进入休眠状态
#             print("锅里没丸子了")
#             con.notify_all()  # 通知他们把丸子弄过来
#             con.wait()  # 等待通知,弄过来之后才执行后面的代码  wait首先会对锁住的线程解锁,然后再等待
#         else:
#             ball.pop()  # 移除列表中的一个元素,默认最后一个元素
#             print("吃货{}夹走了一个丸子,锅里还剩下{}个丸子".format(threading.current_thread(),len(ball)))
#         con.release()  # 释放,我夹完了,你们可以夹了.
#
#
# product = threading.Thread(target=set_data)  # 创建了一个生产者线程
# custmers = [threading.Thread(target=get_data) for i in range(3)]  # 创建了3个消费者线程
# product.start()  # 启动生产者线程,生产丸子
# # 启动3个消费者线程去循环吃丸子
# for i in custmers:
#     i.start()
# product.join()  # 阻塞线程,等待当前生产者生产完消费者才能吃


# '''
# 队列:queue 实现线程通信
# Event:实现线程通信
# '''
# product_env = threading.Event()
# customer_env = threading.Event()
#
# q = queue.Queue(maxsize=10)  # 创建一个队列 指定队列长度
#
#
# # 定义生产者
# def set_data():
#     for i in range(10):
#         for j in range(20):
#             if q.full():  # 判断队列是否已满,满的返回true,不满就返回false
#                 print('当前有{}个丸子进去,吃货们快来吃吧~'.format(q.qsize()))  # q.qsize返回队列中数据的个数
#                 customer_env.set()  # 通知消费者赶紧来吃丸子  唤醒所有处于等待状态的线程
#                 product_env.clear()  # 调用 wait() 方法来阻塞当前线程
#                 product_env.wait()  # 等待消费者过来夹丸子
#             else:
#                 q.put("丸子")  # 没满,就把"丸子"放入队列中
#
# # 定义消费者
# def get_data():
#     while True:
#         time.sleep(0.5)  # 每隔0.5s拿一次丸子
#         if q.empty():  # empty()判断是否为空,为空返回true 没有就把其它线程唤醒,把锁释放掉,进入休眠状态
#             print("锅里没丸子了")
#             product_env.set()  # 通知生产者把丸子放好  唤醒所有处于等待状态的线程
#             customer_env.clear()  # 等待生产者把丸子放好 调用 wait() 方法来阻塞当前线程
#             customer_env.wait()  # 阻塞当前线程 clear 和wait方法一般要共同使用
#         else:
#             q.get()  # 往队列里面拿第一个数据,如果拿不到会一直卡住,如果拿到就会一直往下走
#             print("吃货{}夹走了一个丸子,锅里还剩下{}个丸子".format(threading.current_thread(),q.qsize())) # q.qsize返回队列中数据的个数
#
#
# product = threading.Thread(target=set_data)  # 创建了一个生产者线程
# custmers = [threading.Thread(target=get_data) for i in range(3)]  # 创建了3个消费者线程
# product.start()  # 启动生产者线程,生产丸子
# # 启动3个消费者线程去循环吃丸子
# for i in custmers:
#     i.start()
# product.join()  # 阻塞线程,等待当前生产者生产完消费者才能吃


from concurrent.futures.thread import ThreadPoolExecutor

'''
线程池
'''
product_env = threading.Event()
customer_env = threading.Event()

q = queue.Queue(maxsize=10)  # 创建一个队列 指定队列长度


# 定义生产者
def set_data(d=None):
    for i in range(10):
        for j in range(20):
            if q.full():  # 判断队列是否已满,满的返回true,不满就返回false
                print('当前有{}个丸子进去,吃货们快来吃吧~'.format(q.qsize()))  # q.qsize返回队列中数据的个数
                customer_env.set()  # 通知消费者赶紧来吃丸子  唤醒所有处于等待状态的线程
                product_env.clear()  # 调用 wait() 方法来阻塞当前线程
                product_env.wait()  # 等待消费者过来夹丸子
            else:
                q.put("丸子")  # 没满,就把"丸子"放入队列中
    return '没丸子了,别吃了'

# 定义消费者
def get_data(d=None):
    while True:
        time.sleep(0.5)  # 每隔0.5s拿一次丸子
        if q.empty():  # empty()判断是否为空,为空返回true 没有就把其它线程唤醒,把锁释放掉,进入休眠状态
            print("锅里没丸子了")
            product_env.set()  # 通知生产者把丸子放好  唤醒所有处于等待状态的线程
            customer_env.clear()  # 等待生产者把丸子放好 调用 wait() 方法来阻塞当前线程
            customer_env.wait()  # 阻塞当前线程 clear 和wait方法一般要共同使用
        else:
            q.get()  # 往队列里面拿第一个数据,如果拿不到会一直卡住,如果拿到就会一直往下走
            print("吃货{}夹走了一个丸子,锅里还剩下{}个丸子".format(threading.current_thread(), q.qsize()))  # q.qsize返回队列中数据的个数

# '''
# submit() 给线程添加需要执行的任务 激活线程池中的线程
# result() 获取线程的返回值
# shutdown() 结束线程池
# '''
# #  1. 实例化线城池对象,线城池里面包含1个线程生产者任务;包含3个消费者任务
# pool = ThreadPoolExecutor(max_workers=4)
# # 往线程池里面扔添加需要执行的任务，并且激活线程池中的线程 返回的是一个对象(_base.Future())
# product_future = pool.submit(set_data)
# # 往线程池里面添加3个消费者的任务
# customer_future1 = pool.submit(get_data)
# customer_future2 = pool.submit(get_data)
# customer_future3 = pool.submit(get_data)
# # result()获取线程的返回值
# print(product_future.result())
# # 结束线程池
# pool.shutdown()


# '''
# map() 启动多个线程 以异步方式对参数执行map处理
# '''
# #  1. 实例化线城池对象,线城池里面包含1个线程生产者任务;包含3个消费者任务
# pool = ThreadPoolExecutor(max_workers=4)
# # 启动1个生产者线程
# product = pool.map(set_data,(None,))
# # 启动3个消费者线程 ,传入几个参数,map()会根据传入几个参数去循环执行set_data()
# customer = pool.map(get_data,(None,None,None))
# # 用next()获取返回值 如果用map()启动线程必须要用next()获取返回值
# print(next(product))
# pool.shutdown()


'''
IO密集型 多线程快,适合读文件,数据库操作
'''
# import threading
#
# import time
# def count():
#     s = 0
#     for i in range(10000):
#         time.sleep(0.001) # 使用sleep模拟IO操作
#         s += i
#
# t1 = threading.Thread(target=count)
# t2 = threading.Thread(target=count)
# start = time.time()
# count()
# count()
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# end = time.time()
# print(end-start)


# '''
# CPU密集型  适合单线程 应用场景一般在生成大量的数据时
# '''
# import threading
#
# import time
# def count():
#     s = 0
#     for i in range(100000000):
#         s += i
#
# t1 = threading.Thread(target=count)
# t2 = threading.Thread(target=count)
# start = time.time()
# count()
# count()
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# end = time.time()
# print(end-start)