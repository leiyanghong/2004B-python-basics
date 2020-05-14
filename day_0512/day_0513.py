''''''
import threading
import time
import requests

'''
使用线程池完成以下场景
1个线程准备接口用例数据
10个线程执行接口用例
ps：执行接口用例的场景，使用print函数打印出接口用例数据来模拟，接口用例数据，自己随便找个接口设计即可。
'''


class ThreadRequests(threading.Thread):

    def run(self):
        for i in range(100):
            res = requests.post('http://httpbin.org/post')
            print("Thread-{}--第{}次请求".format(self.name, i + 1))


def main():
    s_time = time.time()
    th = [ThreadRequests() for j in range(10)]
    for i in th:
        i.start()
        for j in th:
            j.join()
            e_time = time.time()
            print('平均时间：{}'.format((e_time - s_time) / 1000))


main()