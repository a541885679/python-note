#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
 题目005：输入三个整数x,y,z，请把这三个数由小到大输出
 """


def test05():
    print('请输入三个整数')
    x = input('输入第一个数字:')
    y = input('输入第二个数字:')
    z = input('输入第三个数字:')
    l = [x, y, z]
    arr = sorted(l)  # 从小到大排序
    arr1 = sorted(l, reverse=True)  # 从大到小排序
    print(arr)
    print(arr1)


print(test05())
