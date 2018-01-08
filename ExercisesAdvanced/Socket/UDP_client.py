#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 建立连接:
for data in [b'Michael', b'Tracy', b'Sarah', b'Quit']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()