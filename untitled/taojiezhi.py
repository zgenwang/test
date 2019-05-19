#!/usr/bin/python
# -*- coding:utf-8 -*-
#服务器
import socket
#创建一个套接字，创建一个有发送能力和接受能力的对象
#默认使用tcp   (SOCK_STREAM)    UDP(SOCK_DGRAM)
#使用的是iPv4和tcp协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip地址和端口
s.bind(('127.0.0.1',8000))#接受的是个元组
#监听服务有没有开启
s.listen(3)
while True:
    #:接收建立连接  第一个参数是建立连接的信息  第二个参数是客户端的ip和端口号
    client,addr=s.accept()
    #接收客户端发送的请求
    msg=client.recv(1024)
    print(client)
    print(addr)
    print(msg.decode('utf-8'))
    reg=input(">>>")
    client.send(reg.encode('utf-8'))
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',80))
# while True:
#     #第一个参数，客户端的请求数据
#     client,addr=s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     msg='hello'
#     s.sendto(msg.encode('utf-8'),addr)


