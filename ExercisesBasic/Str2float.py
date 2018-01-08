# -*- coding: utf-8 -*-
# ___author___ = 'xy'

##############################################################################
# 将string转换为float
# 写法一
##############################################################################
'''
from functools import reduce

def str2float(s):
    #找出小数点在s中的位数，赋予变量point。这里加判断的意义就是如果输入值不包含小数点，会将其赋予0。稍后原数除以10^0会自动在后面加0，因为python的除法得出的值是float型
    if s.find('.')>-1:
        point = len(s)-s.find('.')-1
        s = s.replace('.','')
    else:
        point = 0
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        return x*10+y
    return reduce(fn,map(char2num,s))/pow(10,point)

s = input('请输入一个数字：')
print(str2float(s))
'''
##############################################################################
# 将string转换为float
# 写法二
##############################################################################
from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2float(s):
    if '.' in s:
        return reduce(lambda x, y: x * 10 + y, map(char2num, s.replace('.', ''))) / (10 ** ((len(s) - 1) - (s.index('.'))))
    else:
        return reduce(lambda x, y: x * 10 + y, map(char2num, s)) / 1

s = str(input('please input a number:'))
print(str2float(s))
