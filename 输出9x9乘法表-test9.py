#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
def test08():
    for x in range(1, 10):
        for y in range(1, x + 1):
            print('%d*%d = %d' % (x, y, x * y), end=' ')
        print()


print(test08())
