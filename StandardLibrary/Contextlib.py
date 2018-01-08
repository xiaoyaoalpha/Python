
#########################################################################

# 任何对象，只要正确实现上下文管理，就可以使用with语句。
# 实现上下文管理是通过 __enter__ 和 __exit__ 这两个方法实现的。
# 例如，下面的class实现了这两个方法：

# class AutoTest(object):
#     def __init__(self, testcase):
#         self.testcase = testcase
#
#     def __enter__(self):
#         print('Before testing')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End testing')
#
#     def auto_test(self):
#         print('Test %s...' % self.testcase)
#
# with AutoTest("Create Datacenter") as t:
#     t.auto_test()

#########################################################################

# 编写 __enter__ 和 __exit__ 仍然很繁琐，
# 因此Python的标准库 contextlib 提供了更简单的写法，
# 上面的代码可以改写为

from contextlib import contextmanager

class AutoTest(object):
    def __init__(self, testcase):
        self.testcase = testcase

    def auto_test(self):
        print('Test %s...' % self.testcase)

@contextmanager
def autorun(testcase):
    print('Before testing')
    t = AutoTest(testcase)
    yield t
    print('End testing')

with autorun("Create Datacenter") as t:
    t.auto_test()