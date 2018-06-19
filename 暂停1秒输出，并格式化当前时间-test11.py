#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目010：暂停1秒输出，并格式化当前时间。
"""


def test10():
    import time
    a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # time.localtime()时间戳转化成时间元祖
    print(a)
    time.sleep(1)  # 设置暂停输出时间为1秒
    b = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # time.localtime()时间戳转化成时间元祖
    print(b)


print(test10())
