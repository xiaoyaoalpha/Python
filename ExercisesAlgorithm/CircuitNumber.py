##############################################################################
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 方法一
##############################################################################
'''
def JudgeCircuitNum(n):
    L1 = []
    for i in str(n):
        L1.append(i)
    L2 = L1[:]#创建副本，L2 = L1这样指向的是同一个列表
    L1.reverse()
    if L1 == L2:
        return True
    else:
        return False

def CreateCircuitNum_LessEqualMax(max):
    n = 1
    while n <= max:
        if JudgeCircuitNum(n) == True:
            yield n
        n = n + 1

num = int(input('Please input a number and will return all circuit numbers less than the number:'))
CircuitNumList = list(CreateCircuitNum_LessEqualMax(num))
print(CircuitNumList)
'''
##############################################################################
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 方法二，利用filter
##############################################################################
'''
def JudgeCircuitNum(n):
    L1 = []
    for i in str(n):
        L1.append(i)
    L2 = L1[:]#创建副本，L2 = L1这样指向的是同一个列表
    L1.reverse()
    if L1 == L2:
        return True
    else:
        return False

def CreateCircuitNum_LessEqualMax(max):
    L = list(range(1,max+1))
    return list(filter(JudgeCircuitNum,L))

num = int(input('Please input a number and will return all circuit numbers less than the number:'))
CircuitNumList = CreateCircuitNum_LessEqualMax(num)
print(CircuitNumList)
'''
##############################################################################
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 方法三，利用generator和filter
##############################################################################

def odd_iter():
    n = 1
    while True:
        yield n
        n = n + 1

def JudgeCircuitNum(n):
    L1 = []
    for i in str(n):
        L1.append(i)
    L2 = L1[:]#创建副本，L2 = L1这样指向的是同一个列表
    L1.reverse()
    if L1 == L2:
        return n

def circuit_numbers():
    it = odd_iter()
    while True:
        yield next(it)
        it = filter(JudgeCircuitNum,it)

num = int(input('Please input a number and will return all circuit numbers less than the number:'))
L = []
for n in circuit_numbers():
    if n < num:
        L.append(n)
    else:
        break
print(L)

##############################################################################
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 方法四，利用Str[::-1]判断
##############################################################################
'''
def JudgeCircuitNum(n):
    if isinstance(n,int):
        return str(n)==str(n)[::-1]
    else:
        return n==n[::-1]
'''