# coding=utf-8
# ___author___ = 'xy'

################################################################################################
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# 定义最基本的类，默认属性是width和heigh，再定义类的方法resolution()进行封装，外部不只能调用，但是不知道内部如何实现该方法。
# 但是这种方法无法保护属性，而且无法检查参数。
################################################################################################
'''
class Screen(object):
    def __init__(self,width,heigh):
        self.width = width
        self.heigh = heigh

    def resolution(self):
        return self.width * self.heigh

screen = Screen(1024,768)
screen.width = 1152
print(screen.resolution()) #结果是1152*768
'''
################################################################################################
# 在以上基础修改，加入访问限制，方法是在属性名称前加2个下划线，将其变成私有变量，只能内部访问。
################################################################################################
'''
class Screen(object):
    def __init__(self,width,heigh):
        self.__width = width
        self.__heigh = heigh

    def resolution(self):
        return self.__width * self.__heigh

screen = Screen(1024,768)
#print(screen.__width) #抛出异常“AttributeError: 'Screen' object has no attribute '__width'”
screen.__width = 1152
print(screen.resolution()) #结果是1024*768，无法更改属性screen.__width的值
screen._Screen__width = 1152
print(screen.resolution()) #结果是1152*768，因为python解释器对外把screen.__width改写成screen._Screen__width了，所以依然可以这样来访问，但是这不符合python代码书写规范，强烈不建议
'''
################################################################################################
# 在以上基础修改，通过加入get_方法可以读取属性值，加入set_方法来加入参数检查。
################################################################################################
'''
class Screen(object):
    def __init__(self,width,heigh):
        self.__width = width
        self.__heigh = heigh

    def get_width(self):
        return self.__width

    def set_width(self,value):
        if not isinstance(value,int):
            raise ValueError ('Width must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError ('Width must between 0 and 10000!')
        self.__width = value

    def get_heigh(self):
        return self.__heigh

    def set_heigh(self,value):
        if not isinstance(value,int):
            raise ValueError ('Heigh must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError ('Heigh must between 0 and 10000!')
        self.__heigh = value

    def resolution(self):
        return self.__width * self.__heigh

screen = Screen(1024,768)
print(screen.width)
print(screen.__width) #因为screen.__width是私有属性，所以无法读取属性值
print(screen.get_width()) #通过get_width方法读出属性值
screen.__width = 1152 #无法修改screen.__width属性值
screen.set_width(1152) #通过set_width方法修改属性值
print(screen.resolution()) #结果是1152*768
screen.set_width(-3)
print(screen.get_width()) #抛出错误“ValueError: Width must between 0 and 10000!”
'''
################################################################################################
# 由于调用方法类似于调用函数，使用起来不太方便。在不改变class Student的情况下将方法改写成属性
# property()函数的函数原型是property(fget=None,fset=None,fdel=None,doc=None)，所以可以对get,set,del,doc四种方法进行重写
################################################################################################
'''
class Screen(object):
    def __init__(self,width,heigh):
        self.__width = width
        self.__heigh = heigh

    def get_width(self):
        return self.__width

    def set_width(self,value):
        if not isinstance(value,int):
            raise ValueError ('Width must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError ('Width must between 0 and 10000!')
        self.__width = value

    def get_heigh(self):
        return self.__heigh

    def set_heigh(self,value):
        if not isinstance(value,int):
            raise ValueError ('Heigh must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError ('Heigh must between 0 and 10000!')
        self.__heigh = value

    def resolution(self):
        return self.__width * self.__heigh

    # property 函数将get_和set_方法指向属性，然后可以像调用属性那样调用方法
    width = property(get_width,set_width)
    heigh = property(get_heigh,set_heigh)

screen = Screen(1024,768)
print(screen.width) #1024，可以对对象属性进行get操作
screen.width = 1152
print(screen.width) #1152，可以对对象属性进行set操作
'''
################################################################################################
# 或者用装饰器 @property对其进行改写
################################################################################################

class Screen(object):
    def __init__(self,width,heigh):
        self.__width = width
        self.__heigh = heigh

    @property #利用@property装饰get_width方法，将其改写成属性可以直接调用
    def width(self):
        return self.__width

    @width.setter #@xxx.setter是固定写法，将set方法改写成可以直接调用
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('Width must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError('Width must between 0 and 10000!')
        self.__width = value

    @property
    def heigh(self):
        return self.__heigh

    @heigh.setter
    def heigh(self,value):
        if not isinstance(value, int):
            raise ValueError('Heigh must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError('Heigh must between 0 and 10000!')
        self.__heigh = value

    @property #改写resolution，可以直接将其变成属性来调用取值
    def resolution(self):
        return self.__heigh * self.__width

screen = Screen(1024,768)
#screen.width = 1152
#screen.heigh = 864
print(screen.width) #1152
print(screen.heigh) #864
print(screen.resolution) #1152*864
assert screen.resolution == 786432, '1024 * 768 = %d ?' % screen.resolution