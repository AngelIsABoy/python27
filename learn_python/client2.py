#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入socket库：
import socket
import time
import urllib2
timeout = 20
socket.setdefaulttimeout(timeout)
#创建一个socket：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = urllib2.urlopen('www.sina.com.cn')
data = request.read()
# #建立连接：
# s.connect(('www.sina.com.cn', 80))
# #发送数据
# s.send('GET /HTTP/1.1\r\nHOST:www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
    # #每次最多接收1k字节：
    # d = s.recv(2048)
    # if d:
        # buffer.append(d)
    # else:
        # break
# data = ''.join(buffer)
#关闭连接
s.close()

header, html = data.split('\r\n\r\n',1)
print header
#把接收的数据写入文件：
with open('G:\python27\learn_python\sina.html','wb') as f:
    f.write(html)