#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

import threading


# 定义线程要调用的方法
def action(*add):
    for i in add:
        # threading.current_thread() 返回当前执行的线程
        # getName() 获取当前执行该程序的线程名
        # 输出打印遍历每次执行的线程名字 + 每次遍历的参数
        print(threading.current_thread().getName() + " " + i )

# 定义为线程方法传入的参数
my_tuple = ("http://stu.guoyasoft.com",
            "http://www.guoyasoft.com",
            "http://www.guoyasoft.com:8001")

# 创建线程
# threading.Thread 创建一个线程,传入方法和参数
thread = threading.Thread(target=action,args=my_tuple)
# 启动线程
thread.start()

# for i in range(5):

