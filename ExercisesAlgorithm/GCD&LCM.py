#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
# 方法一：利用分解因数法
################################################################################################

# from MyClass.SimpleTool import factorization
# import time
#
#
# def lcm(m, n):
#     m_prime_list, n_prime_list, divisor_list = factorization(m), factorization(n), []
#     m_list, n_list = m_prime_list[:], n_prime_list[:]
#     for divisor in m_prime_list:
#         if divisor in n_prime_list:
#             divisor_list.append(divisor)
#             n_prime_list.remove(divisor)
#     for divisor in divisor_list:
#         m_list.remove(divisor)
#         n_list.remove(divisor)
#     divisor_list = divisor_list + m_list + n_list
#     lcm_num = 1
#     for divivsor in divisor_list:
#         lcm_num = lcm_num * divivsor
#     return lcm_num
#
#
# def gcd(m, n):
#     m_prime_list, n_prime_list, divisor_list = factorization(m), factorization(n), []
#     for divisor in m_prime_list:
#         if divisor in n_prime_list:
#             divisor_list.append(divisor)
#             n_prime_list.remove(divisor)
#     gcd_num = 1
#     for divisor in divisor_list:
#         gcd_num = gcd_num * divisor
#     return gcd_num

################################################################################################
# 题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
# 方法二：利用欧几里德算法，效率比分解因式法高很多
################################################################################################


def gcd(m, n):
    while m != 0:
        m, n = n % m, m
    return n


def lcm(m, n):
    divisor = gcd(m, n)
    return int(m * n / divisor)


while True:
    m = input("please input the 1st number: ")
    n = input("please input the 2nd number: ")
    try:
        m, n = int(m), int(n)
    except ValueError:
        print("numbers should be integer!", end="\n\n")
    else:
        if m < 1 or n < 1:
            print("numbers should be greater than 0!")
        else:
            print("gcd is: %d" % gcd(m, n))
            print("lcm is: %d" % lcm(m, n), end="\n\n")
