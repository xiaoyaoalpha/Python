#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################################################

# 比如我们用户拥有一个这样的数据结构，每一个对象是拥有三个元素的tuple。
# 使用namedtuple方法就可以方便的通过tuple来生成可读性更高也更好用的数据结构。

from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print(website,end=" ")
    print("name=" + website.name, end=" ")
    print("url=" + website.url, end=" ")
    print("founder=" + website.founder)

##########################################################################

# list对象的这两种用法的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈 线性上升。
# 而使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque。
# 下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环的加载动画。

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

##########################################################################

# 下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数

from collections import Counter

s = "A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.".lower()
c = Counter(s)
# 获取出现频率最高的5个字符
t = Counter(c.most_common(5))
print(c)

##########################################################################

# 在Python中，dict这个数据结构由于hash的特性，是无序的，这在有的时候会给我们带来一些麻烦，
# 幸运的是，collections模块为我们提供了OrderedDict，当你要获得一个有序的字典对象时，用它就对了。
# OrderedDoct 可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    @property
    def capacity(self):
        if self._capacity == 0:
            print("ha")
            raise KeyError('Dictionary is empty')
        else:
            return self._capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            try:
                last = self.popitem(last=False)
            except KeyError as e:
                print("except: ", e)
            finally:
                print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

o_dict = LastUpdatedOrderedDict(2)
o_dict.__setitem__("name","KobeBryant")
o_dict.__setitem__("number","8")
o_dict.__setitem__("number","24")
o_dict.__setitem__("team","LA Lakers")
print(o_dict)

##########################################################################

# 如果使用defaultdict，只要你传入一个默认的工厂方法，那么请求一个不存在的key时，
# 便会调用这个工厂方法使用其结果来作为这个key的默认值。

from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)

# not return error, will return default value []
print(result['middle'])
