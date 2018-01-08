"""
def fac(fac_x): #定义阶乘函数
    if not (isinstance(fac_x,(int))):
        raise TypeError('bad operand type')
    if fac_x>1:    
        fac_f=fac_x
        while fac_x>1:
            fac_x=fac_x-1
            fac_f=fac_f*fac_x
        return(fac_f)
    elif fac_x<0:
        return'参数有误导致阶乘结算出错！'
    else :
        return(1)

def triangles(tri_max): #利用阶乘算出每一个数，然后利用嵌套循环构造嵌套列表，即为杨辉三角
    tri_Lm = []
    tri_Ln = []
    tri_m = 0
    tri_n = 0
    for tri_m in range(tri_max): 
        for tri_n in range(tri_m+1):
            tri_r = int((fac(tri_m)/((fac(tri_m-tri_n))*fac(tri_n)))) #求出值即为杨辉三角第m层第n个数 
            tri_Ln.append(tri_r)
            tri_n = tri_n + 1
        tri_Lm.append(tri_Ln)
        tri_Ln = []
        tri_m = tri_m + 1
    return(tri_Lm)
        
level = int(input('请输入希望杨辉三角显示的层数：'))
for t in triangles(level):
    print(t)
"""
####################################用generator更方便#############################################

"""
 def triangles():
    L=[1]
    while True:
        yield L
        L = [sum(i) for i in (zip(L+[0],[0]+L))]
        '''由于杨辉三角第m行第n个数是m-1行第n-1和第m-1行第n个数的和，
        所以可以推导出第m行的所有元素组成的列表等于，
        第m-1行的列表+[0]和[0]+第m-1行的列表中所有元素之和组成的列表'''
        
def triangles():
    L=[1]
    while True:
        yield L
        L=L+[0]
        L1=[0]+L
        for i in range(len(L)):
            L[i]=L[i]+L1[i]
            #该生成方式与上面的方式思路一致，也是生成2个新列表然后每项元素的和组成的新列表组成杨辉三角

r = int(input('请输入希望杨辉三角显示的层数：'))
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == r:
        break
"""

####################################第二种generator方式#############################################

def triangles(max):
    L = [1]
    n = 0
    while n <= max:
        yield L
        L1 = L + [0]
        L2 = [0] + L
        L.append('') #将L扩展一位
        for i in range(len(L)):
            L[i] = L1[i] + L2[i]
        n = n + 1

line_num = int(input('please input the line number:'))
for line in triangles(line_num):
    print(line)
