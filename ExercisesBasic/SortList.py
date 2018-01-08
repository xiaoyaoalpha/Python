# -*- coding: utf-8 -*-

################################################################################################
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted()对上述列表分别按名字排序，再按成绩降序排序，方法一
################################################################################################

def stuSortByName(item):
    return item[0]

def stuSortByGrade(item):
    return item[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(list(sorted(L ,key=stuSortByName)))
print(list(sorted(L ,key=stuSortByGrade,reverse=True)))

################################################################################################
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted()对上述列表分别按名字排序，再按成绩降序排序，方法二
################################################################################################

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L, key = lambda student: student[0])
L2 = sorted(L, key = lambda student: student[1], reverse=True)
print(L1)
print(L2)