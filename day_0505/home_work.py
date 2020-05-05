#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
6、使用字典推导式，把下列数据转换成字典
'''
lst = [("name", "xuepl"), ("age", 18), ("sex", "男")]
lst = {key: value for key, value in lst}
print(lst)
'''
7、定义一个类，实现读取文件中的json数据，把所有的key转成大写，再写入文件中
'''
import json


class JsonDemo():
    def __init__(self, file_path):
        self.file_path = file_path

    # 读取数据源
    def read_txt(self):
        with open(self.file_path, 'r+', encoding='utf-8') as f:
            return f.read()

    # 操作数据源
    def operate_json(self):
        data = self.read_txt()
        json1 = json.dumps(data)
        json2 = json.loads(json1)
        lst = {key.upper(): value for key, value in eval(json2).items()}
        return lst

    # 写入数据
    def write_data(self):
        with open("update_json_data.txt", 'a+', encoding="utf-8") as f:

            f.write(str(self.operate_json())+"\n")
            return f.read()


if __name__ == '__main__':
    jd = JsonDemo('json_data.txt')
    jd.write_data()
    with open("update_json_data.txt", 'a+', encoding='utf-8') as f:
        print(f.read())
