#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目014：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
def test14():
    import math
    num = int(input('输入一个整数:'))
    arr = []
    while num > 1:
        for x in range(2, int(math.sqrt(num)) + 1):
            if num % x == 0:
                arr.append(x)
                num = num//x
                break
        else:
            arr.append(num)
            break
    print(arr)
print(test14())