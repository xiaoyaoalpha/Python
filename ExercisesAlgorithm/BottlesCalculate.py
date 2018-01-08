#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 一元钱一瓶汽水，喝完后两个空瓶换一瓶汽水。问：你有n元钱，最多可以喝到几瓶汽水？比如4元钱，可以喝7瓶.
################################################################################################


def bottle_calc(bottle_start, bottle_end, bottle_empty):
    while bottle_start > 0:
        bottle_end = bottle_end + bottle_start
        a, b = divmod(bottle_start, 2)
        bottle_empty = bottle_empty + b
        bottle_start = a
        if bottle_empty > 1:
            m, n = divmod(bottle_empty, 2)
            bottle_empty = n
            bottle_start = bottle_start + m
    else:
        return bottle_start, bottle_end, bottle_empty

money = int(input('请输入钱数：'))
x = bottle_calc(money, 0, 0)
print('花费 %d 元，可以喝 %d 瓶汽水，最后还剩 %d 个空瓶' % (money, x[1], x[2]))
