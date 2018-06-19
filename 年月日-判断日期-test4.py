#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
# '''''
# 题目004：输入某年某月某日，判断这一天是这一年的第几天？
# '''

def test4():
  '''''
     【个人备注】：知道python有时间元组这一概念，这道题完全不需要计算。
    时间元组包含九个属性
    tm_year     年
    tm_mon      月(1~12)
    tm_mday     日(1~31)
    tm_hour     时(0~23)
    tm_min      分(0~59)
    tm_sec      秒(0~61, 60或61是闰秒)
    tm_wday     星期(0~6, 0是周一)
    tm_yday     第几天(1~366, 366是儒略历)
    tm_isdst    夏令时(平时用不到)
    '''

import time
date = input('输入时间:')
st = time.strptime(date, '%Y-%m-%d')  # 时间文本转化成时间元祖
num1 = st.tm_yday
num2 = st.tm_wday

if num2 == 0:
    print('今天是星期一')
elif num2 == 1:
    print('今天是星期二')
elif num2 == 2:
    print('今天是星期三')
elif num2 == 3:
    print('今天是星期四')
elif num2 == 4:
    print('今天是星期五')
elif num2 == 5:
    print('今天是星期六')
elif num2 == 6:
    print('今天是星期日')
else:
    print('日期错误')

print('今天是这一年的第%d天' % num1)

print(test4())
