#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_
"""''
题目016：输出指定格式的日期。
"""


def test16():
    import time
    print(time.time())  # 时间戳 1498539133.655
    print(
        time.localtime())  # 时间元祖 tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1,
    # tm_yday=178, tm_isdst=0
    print(time.asctime())
    print(time.strftime('%Y-%m-%d %H-%M-%S'), time.localtime())

    st = time.strptime('2018/1/23', '%Y/%m/%d')
    date = time.strftime('%Y-%m-%d', st)
    print(date)

    import datetime
    dt1 = datetime.datetime.fromtimestamp(1517302458)
    print(dt1, type(dt1))
    dt2 = datetime.datetime.now()
    print(dt2)
    print('相差%d天零%.1f个小时' % ((dt2 - dt1).days, (dt2 - dt1).seconds / 60 / 60))


print(test16())
