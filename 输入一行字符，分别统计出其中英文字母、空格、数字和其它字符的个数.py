#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目017：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


def test17():
    s = input('input a string:\n')
    letters, space, digit, others = 0, 0, 0, 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = %d, space = %d, digit = %d, others = %d' % (letters, space, digit, others))


print(test17())

