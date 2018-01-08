#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
################################################################################################


def judge_daff(daff_num):
    for number in str(daff_num):
        daff_num = daff_num - int(number)**3
    return True if daff_num == 0 else False


def daffodil(start_num, end_num):
    daff_list = []
    for i in range(start_num, end_num + 1):
        if judge_daff(i) is True:
            daff_list.append(i)
    return daff_list

while True:
    m = input("please input the start number: ")
    n = input("please input the end number: ")
    try:
        m, n = int(m), int(n)
    except ValueError:
        print("numbers should be integer!", end="\n\n")
    else:
        if m > n:
            print("start number should be equal to or less than end number!")
        elif m < 0:
            print("start number should be greater than 0!")
        else:
            print(daffodil(m, n))
        print("")
