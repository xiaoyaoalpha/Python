# coding=utf-8
# ___author___ = 'xy'

##############################################################################
# 打印菱形
# 方法一
##############################################################################

line = int(input('请输入行数:'))
if line <= 0:
    print('输入值不正确！')
if line % 2 == 1:
    for a in range(line):
        if 0 <= a <= int((line - 1) / 2):
            for b in range(int((line + 1) / 2 + a)):
                if b > int((line - 1) / 2 - 1 - a):
                    print('*', end="")
                else:
                    print('\000', end="")
            print("")
        else:
            for b in range(int(line - a + (line - 1) / 2)):
                if b > int((line - 1) / 2 - line + a):
                    print('*', end="")
                else:
                    print('\000', end="")
            print("")
elif line % 2 == 0:
    for a in range(line):
        if 0 <= a <= int(line / 2 - 1):
            for b in range(int(line / 2 + a)):
                if b > int(line / 2 - 2 - a):
                    print('*', end="")
                else:
                    print('\000', end="")
            print("")
        else:
            for b in range(int(line - a + (line - 1) / 2)):
                if b > int(a - 1 - line / 2):
                    print('*', end="")
                else:
                    print('\000', end="")
            print("")


##############################################################################
# 打印菱形
# 方法二
##############################################################################

"""
LineNum = int(input('Please input the line number:'))
if LineNum%2==1:
    #构造矩阵
    Matrix = []
    MatrixLine = []
    for i in range(LineNum):
        Matrix.append([i])
        MatrixLine.append([i])
        Matrix[i] = MatrixLine
    # 利用四条线画出菱形，菱形内每个点都打印*，菱形外每个点打印_
    for y in range(LineNum):
        for x in range(LineNum):
            if (y>=-x+int((LineNum-1)/2) and y<=-x+int((LineNum-1)/2*3) and y>=x-int((LineNum-1)/2) and y<=x+int((LineNum-1)/2)):
                Matrix[y][x] = '*'
            else:
                Matrix[y][x] = '\000'
        NewLine = ''.join(Matrix[x]) #列表中的内容转化为字符串
        print(NewLine)
elif LineNum%2==0:
    #构造矩阵
    Matrix = []
    MatrixLine = []
    for j in range(LineNum-1):
        MatrixLine.append([j])
    for i in range(LineNum):
        Matrix.append([i])
        Matrix[i] = MatrixLine
    # 利用四条线画出菱形，菱形内每个点都打印*，菱形外每个点打印_
    for y in range(LineNum):
        for x in range(LineNum-1):
            if (y>=-x+int((LineNum-2)/2) and y<=-x+int((LineNum-2)/2*3+1) and y>=x-int((LineNum-2)/2) and y<=x+int((LineNum-2)/2+1)):
                Matrix[y][x] = '*'
            else:
                Matrix[y][x] = '\000'
        NewLine = ''.join(Matrix[x]) #列表中的内容转化为字符串
        print(NewLine)
"""