# coding=utf-8
# ___author___ = 'xy'

################################################################################################
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# 方法一，利用字符串操作函数 title()
################################################################################################
"""
L = ['adam', 'LISA', 'barT']
def StringTitle(s):
    s1 = s.title()
    return s1
NewL = list(map(StringTitle,L))
print(NewL)
"""
################################################################################################
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# 方法二，不利用字符串操作函数 title()，构造大小写转换字典及函数
################################################################################################
#创建大小写字母列表
List_LowerCase = [x for x in 'abcdefghijklmnopqrstuvwxyz']
List_UpperCase = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

#构造创建字典函数
def CreateDict(x,y):
    return (x,y)

#利用创建字典函数构造大小写字符对应字典
Dict_Low2Up = dict(list(map(CreateDict,List_LowerCase,List_UpperCase)))
Dict_Up2Low = dict(list(map(CreateDict,List_UpperCase,List_LowerCase)))

#构造字符串全字母大写函数
def Str_Upper(s):
    L = list(s)
    for n,k in enumerate(L):
        if k in Dict_Low2Up:
            L[n] = Dict_Low2Up[k]
    return ''.join(L)

#构造字符串全字母小写函数
def Str_Lower(s):
    L = list(s)
    for n,k in enumerate(L):
        if k in List_UpperCase:
            L[n] = Dict_Up2Low[k]
    return ''.join(L)

#构造字符串首字母大写函数
def Str_Title(s):
    L = list(s)
    for n, k in enumerate(L):
        if k in List_UpperCase:
            L[n] = Dict_Up2Low[k]
    if L[0] in Dict_Low2Up:
        L[0] = Dict_Low2Up[L[0]]
    return ''.join(L)

#构造字符串所有字符转换大小写函数
def Str_SwapCase(s):
    L = list(s)
    for n, k in enumerate(L):
        if k in List_UpperCase:
            L[n] = Dict_Up2Low[k]
        elif k in List_LowerCase:
            L[n] = Dict_Low2Up[k]
    return ''.join(L)

L = ['adam', 'LISA', 'barT']
NewL = []
for s in L:
    NewL.append(Str_Title(s))
print(NewL)