#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目012：判断101-200之间有多少个素数，并输出所有素数。
"""


def test12():
    z = []
    for x in range(101, 201):
        for y in range(2, x):  # 素数为只能被1或者本身整除
            if x % y == 0:
                break
        else:  # else必须和for对应，否则break会结束循环
            z.append(x)
    print(z)
    print('素数的个数为:', len(z))


print(test12())
