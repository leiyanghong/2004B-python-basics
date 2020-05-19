import requests
import gevent
from gevent import monkey
import time


'''
协程：gevent
协程存在于线程之中，线程默认不会等待协程执行，
spawn:开启协程（第一个参数为协程要执行的任务）
join:让线程等待协程执行
'''

monkey.patch_all()

def work1():
    for i in range(100):
        print('这个是work1')
        requests.get('http://www.baidu.com')
        time.sleep(0.1)


def work2():
    for i in range(100):
        requests.get('http://www.baidu.com')
        print('这个是work2')
        time.sleep(0.1)


g1=gevent.spawn(work1)
g2=gevent.spawn(work2)

g1.join()
g2.join()