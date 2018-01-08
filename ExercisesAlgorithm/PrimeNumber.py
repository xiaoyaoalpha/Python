#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# 判断2个数字之间有多少个素数，并输出所有素数。
################################################################################################


# 利用埃式算法
def eratosthenes(max_num):
    i = 0
    prime_list = list(range(2, max_num + 1))
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


def output_prime(start_num, end_num):
    prime_list = eratosthenes(end_num)
    for prime in prime_list:
        if prime < start_num:
            prime_list.remove(prime)
    print("There are %d primes between %d and %d" % (len(prime_list), start_num, end_num))
    for prime in prime_list:
        print(prime)

while True:
    m = input("please input the start number: ")
    n = input("please input the end number: ")
    try:
        m, n = int(m), int(n)
    except ValueError:
        print("numbers should be integer!", end="\n\n")
    else:
        if m > n:
            print("start number should be equal to or less than end number!", end="\n\n")
        elif m < 2:
            print("start number should be greater than 2!", end="\n\n")
        else:
            output_prime(m, n)
            print("")
