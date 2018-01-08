#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子对数为多少？
################################################################################################


# 分析该问题可知每个月的兔子对数符合斐波那契数列
def rabbits_number(month):
    n, a, b = 1, 0, 1
    if month == 1:
        return 1
    else:
        while n <= month - 1:
            r = a + b
            a = b
            b = r
            n += 1
        return b

try:
    _month = int(input("please input the month:"))
except Exception as e:
    print("Exception:", e)
else:
    if max <= 0:
        print("month should be an integer and above 0")
    else:
        print("month: %d, rabbits: %d" % (_month, rabbits_number(_month)))
