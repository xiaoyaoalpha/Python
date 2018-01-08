#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################
# Python对协程的支持是通过generator实现的。
# 在generator中，不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
################################################################################################
def countdown(n):
    print ("Counting down from", n)
    while n >= 0:
        print("===============")
        newvalue = (yield n)
        print('newvalue:',newvalue)
        print('n:',n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

c = countdown(5)
for x in c:
    print ('x:',x)
    if x == 5:
        c.send(4)
        c.send(2)

################################################################################################
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高
################################################################################################
import asyncio

def consumer(r):
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

@asyncio.coroutine
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        l = c.send(n)
        print('[PRODUCER] Consumer return: %s' % l)
    c.close()

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
task = produce(consumer(''))
loop.run_until_complete(task)
loop.close()

################################################################################################
# 小例子：
################################################################################################
import asyncio

def double_gen():
    receive = 0
    while True:
        n = yield receive
        n = n * 2
        print("double = ", n)
        receive = n

@asyncio.coroutine
def natural_gen(gen, starter, max):
    gen.send(None)
    n = 0
    while n < max:
        print("natural number is: ", starter)
        n = gen.send(starter)
        starter = n + 1
    gen.close()

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = natural_gen(double_gen(),3,1000)
loop.run_until_complete(tasks)
loop.close()

################################################################################################
# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
################################################################################################
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

################################################################################################
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
################################################################################################
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

################################################################################################
# 编写一个HTTP服务器，分别处理以下URL：
# / - 首页返回b'<h1>Index</h1>'；
# /hello/{name} - 根据URL参数返回文本hello, %s!。
################################################################################################
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()