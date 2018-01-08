# coding=utf-8
# ___author___ = 'xy'

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        print(func(*args, **kwargs))
        end = time.clock()
        print('used:%f' % (end - start))
    return wrapper


@timeit
def eratosthenes1(max_num):
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


@timeit
def eratosthenes2(max_num):

    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    def _not_divisible(n):
        return lambda x: x % n > 0

    def primes():
        yield 2
        it = _odd_iter()  # 初始序列
        while True:
            n = next(it)  # 返回序列的第一个数
            yield n
            it = filter(_not_divisible(n), it)

    prime_list = []
    for i in primes():
        if i <= max_num:
            prime_list.append(i)
        else:
            break
    return prime_list


@timeit
def eratosthenes3(n):
    prime_list = [i for i in range(2, n + 1)]
    p = 0
    while True:
        for i in prime_list[p + 1:]:
            if i % prime_list[p] == 0:
                prime_list.remove(i)
        if prime_list[p] ** 2 >= prime_list[-1]:
            break
        p += 1
    return prime_list


@timeit
def eratosthenes4(max_num):
    def judge_prime(p):
        flag = True
        for m in range(2, p - 1):
            if p % m == 0:
                flag = False
        return flag
    n = 2
    prime_list = []
    while n <= max_num:
        if judge_prime(n) is True:
            prime_list.append(n)
        n = n + 1
    return prime_list


@timeit
def eratosthenes5(max_num):
    def judge_prime(n):
        flag = True
        for m in range(2, n - 1):
            if n % m == 0:
                flag = False
        return flag
    prime_list = list(range(2, max_num + 1))
    return list(filter(judge_prime, prime_list))

num = 20000
e1 = eratosthenes1(num)
e2 = eratosthenes2(num)
e3 = eratosthenes3(num)
e4 = eratosthenes4(num)
e5 = eratosthenes5(num)
print(e1)
print(e2)
print(e3)
print(e4)
print(e5)
