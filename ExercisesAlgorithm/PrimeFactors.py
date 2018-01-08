#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
################################################################################################


def eratosthenes(num):
    i = 0
    prime_list = list(range(2, num + 1))
    while prime_list[i] ** 2 < prime_list[-1]:
        count = 0
        for j in range(i + 1, len(prime_list)):
            if prime_list[j] % prime_list[i] == 0:
                prime_list[j] = 0
                count += 1
        prime_list.sort()
        prime_list = prime_list[count:]
        i += 1
    return prime_list


# use while circulation
def factorization(num):
    prime_list = eratosthenes(num)
    div_list = []
    while num != 1:
        for prime in prime_list:
            if num % prime == 0:
                div_list.append(prime)
                num = int(num / prime)
    else:
        div_list.sort()
        return div_list


# use recursion
# def factorization(num):
#     prime_list = eratosthenes(num)
#     div_list = []
#     def rec(n):
#         for prime in prime_list:
#             if n % prime == 0:
#                 div_list.append(prime)
#                 n = int(n / prime)
#                 break
#         return div_list if n == 1 else rec(n)
#     return rec(num)

def formater(num):
    div_list = fac_prime(num)
    for index, divisor in list(enumerate(div_list)):
        divisor = str(divisor)
        div_list[index] = divisor
    div_str = ' * '.join(div_list)
    num_str = str(num)
    formula_str = num_str + " = " + div_str
    return formula_str

try:
    number = int(input("please input the number: "))
except Exception as e:
    print("Exception:", e)
else:
    if number <= 1:
        print("month should be an integer and above 1")
    else:
        print(formater(number))
