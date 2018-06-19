#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目009：暂停一秒输出。
"""
def test09():
    import time
    a = time.time()
    time.sleep(1)
    b = time.time()
    print(b - a)

print(test09())