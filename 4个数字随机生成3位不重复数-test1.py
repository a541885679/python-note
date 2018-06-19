#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
def test1():
    arry = []
    for x in range(1, 5):
        for y in range(1, 5):
            for z in range(1, 5):
                num = x * 100 + y * 10 + z
                if x != y and x != z and y != z and num not in arry:
                    arry.append(num)
                    print(x, y, z)
    print(len(arry))
    print(arry)
print(test1()) 