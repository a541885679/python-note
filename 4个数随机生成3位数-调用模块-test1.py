#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
import itertools
temp_arr = list(itertools.permutations([1, 2, 3, 4], 3))
arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
print(arr)
print(len(arr))