#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目013：打印出所有的"水仙花数"，
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""


def test13():
    a = []
    for x in range(100, 1000):
        b = x // 100  # 百位
        c = x % 100 // 10  # 十位
        d = x % 10  # 个位
        if x == b ** 3 + c ** 3 + d ** 3:
            a.append(x)
    print(a)
    print('数量为：', len(a))


print(test13())
