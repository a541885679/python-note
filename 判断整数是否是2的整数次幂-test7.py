#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_

def test07():
    x = int(input('请输入一个整数:'))
    y = x & x - 1  # 1 & 0 == 0
    if y == 0:
        print('%d是2的整数次幂' % x)
    else:
        print('%d不是2的整数次幂' % x)


print(test07())
