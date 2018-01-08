#!/usr/bin/env python3
# -*- coding: utf-8 -*


def natural_generator(start_num):
    while True:
        yield start_num
        start_num = start_num + 1


def prime_generator():

    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    def _not_divisible(n):
        return lambda x: x % n > 0

    def primes():
        yield 2
        it = _odd_iter()
        while True:
            n = next(it)
            yield n
            it = filter(_not_divisible(n), it)
    return primes()


def fib_generator():
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a + b
        n = n + 1


def factorial(max_num):
    if max_num > 1:
        fac = max_num
        while max_num > 1:
            max_num -= 1
            fac = fac * max_num
        return fac
    elif max_num == 1:
        return 1


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


def fibonacci(max_num):
    n, a, b = 0, 0, 1
    fib_list = [1]
    for n in range(max_num):
        r = a + b
        a = b
        b = r
        fib_list.append(b)
    return fib_list


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
