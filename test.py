#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh


# mydict = {"ticket":"A25B2E2A-69A1-4325-9B94-ED2AB3393D6C","encrypt":"","groupId":5191,"sign":"5E47971BBE475D1A206738DAF8A4511F","cmd":"order.partrefund.push","source":"61628","body":"{\"addition_reason\":\"\",\"delivery_fee\":{\"shop_rate\":0,\"user_rate\":0},\"order_id\":\"2126598687722675268\",\"reason\":\"\\u5546\\u6237\\u540c\\u610f\\u9000\\u5355\",\"reason_type\":\"1202\",\"refund_id\":\"9349959209409\",\"refund_price\":1,\"refund_products\":[{\"custom_sku_id\":\"1240377\",\"gm_ids\":[],\"is_free_gift\":0,\"name\":\"\\u805a\\u8363 \\u5b89\\u795e\\u8865\\u8111\\u6db2 10ml*12\\u652f\",\"number\":1,\"product_feature\":[],\"shop_ele_refund\":0,\"sku_id\":\"15851261672253743\",\"sub_biz_order_id\":\"592753797013200994\",\"total_refund\":1,\"upc\":\"6939212262927\"}],\"status\":20,\"type\":2}","version":"3","timestamp":"1589421127"}
# d = [keys + "=" + str(values) for keys, values in mydict.items()]
# print("&".join(d))


import threading

con = threading.Condition()


def job1():
    con.acquire()
    print("JOB1：床前明月光")
    con.notify_all()  # 唤醒正在等待(wait)的线程

    con.wait()  # 等待对方回应消息，使用wait阻塞线程，等待对方通过notify唤醒本线程
    print("JOB1：举头看明月")
    con.notify_all()  # 唤醒对方
    con.release()


def job2():
    con.acquire()
    con.wait()
    print("JOB2:疑似地上桑")
    con.notify_all()
    con.wait()
    print("JOB2:低头思故乡")
    con.notify_all()
    con.release()






if __name__ == "__main__":
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t2.start()  # 此处注意顺序，先t2,否则双方都处于wait状态，程序卡死
    t1.start()
    t1.join()
    t2.join()

    import queue

    q = queue.Queue()
    q.put('a')
    q.put('b')
    print(q.get())

