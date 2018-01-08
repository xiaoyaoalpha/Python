################################################################################################
# 装饰器 decorator
# 场景一，添加标记
################################################################################################

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"

# a = hello()
# print(a)


################################################################################################
# 装饰器 decorator
# 场景二，添加log
################################################################################################

import functools

def log(x):
    def decorator(func,text=x):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            func(*args, **kw)
            print('%s() End\n' % func.__name__)
            return
        return wrapper
    #这里判断x是否可被调用
    #针对@log('excute'): date()=log('excute')(date)，x='excute'不可被调用，则log('excute')返回的是函数decorator。
    #针对@log: now()=log(now)，x='now()'可以被调用，则log(now)返回的是decorator(now,'Call')
    return decorator(func=x,text='Call') if callable(x) else decorator

@log
def now():
    print('2017-07-28 Friday')

@log('excute')
def date():
    print('2017-07-28')

# now()
# date()

################################################################################################
# 装饰器 decorator
# 场景三，添加计时器
################################################################################################
import time

# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper(*args, **kwargs):
        start = time.clock()
        print(func(*args, **kwargs))
        end = time.clock()
        print('used:%f'%(end - start))
    # 将包装后的函数返回
    return wrapper

@timeit
def foo():
    print('in foo()')

# foo()