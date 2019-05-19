#!/usr/bin/python
# -*- coding:utf-8 -*-
# import os
# # b=os.popen('ping 192.168.1.22')
#
# # a=os.listdir('.')
# # for i in a:
# #     if i.endswith('py'):
# #         print(i)
# # ab=os.path.split(r'C:\Users\wang\Desktop\a.txt')
# # print(ab)
# # a=os.path.isdir(r'C:\Users\wang\Desktop\a.txt')
# # print(a)
# import paramiko
# # while True:
# #     a=input('>>>')
# #     ssh123=paramiko.SSHClient()
# #     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     ssh123.connect(hostname='192.168.1.22',
# #                port=22,
# #                username='root',
# #                password='123456')
# #     stuin,stuout,stuerr=ssh123.exec_command(a)
# #     print(stuout.read().decode())
# #     ssh123.close()
# #     if a == 'exit':
# #         ssh123.close()
# #         break
# #传输文件
# # ssh123=paramiko.Transport(('192.168.1.22',22))
# # ssh123.connect(username='root',password='123456')
# # sftp=paramiko.SFTPClient.from_transport(ssh123)
# # sftp.put('day1.py','/home/day1.py')
# # ssh123.close()
# # while True:
# #     import smtplib
# #     import email.mime.multipart
# #     import email.mime.text
# #     fr='18272981597@163.com'
# #     shou='1106589021@qq.com'
# #     server='smtp.163.com'
# #     passwd='199783zgw'
# #     message=email.mime.multipart.MIMEMultipart()
# #     message['From']=fr
# #     message['To']=shou
# #     message['Subject']='您有一封邮件，请注意查收'
# #     text='愚人节快乐ya ! \n 嗯哼嗯哼蹦叉叉'
# #     txt=email.mime.text.MIMEText(text)
# #     # 添加附件
# #     att2 = email.mime.text.MIMEText(open(r'C:\Users\wang\Desktop\timg.jpg', 'rb').read(), 'base64', 'utf-8')
# #     att2["Content-Type"] = 'application/octet-stream'
# #     att2["Content-Disposition"] = r'attachment; filename="C:\Users\wang\Desktop\timg.jpg"'
# #     ## 头部字段
# #     message.attach(att2)
# #
# #     message.attach(txt)
# #     smtp123=smtplib.SMTP_SSL(server,465)
# #     smtp123.login(fr,passwd)
# #     smtp123.sendmail(fr,shou,message.as_string())
# #     smtp123.close()
# #客户端
# import socket
# #创建套接字
# while True:
#     sock=socket.socket()
#     #不需要绑定ip，建立连接
#     #服务器的ip和端口号
#     sock.connect(('127.0.0.1',8000))
#     #发送请求
#     msg=input('>>>>')
#     sock.send(msg.encode('utf-8'))
#     reg=sock.recv(1024)
#     #接收响应
#     print(reg.decode('utf-8'))
#     #断开连接
#     sock.close()
# #UDP客户端
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #不需要建立连接
# host = ('127.0.0.1',80)
# msg='你吃饭了吗'
# s.sendto(msg.encode('utf-8'),host)
# reg=s.recv(1024)
# print(reg.decode('utf-8'))
# s.close()
from flask import Flask,render_template,request
app = Flask(__name__)
print(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username in ["zhangsan","lisi"] and  password=="123":
            return "<h1>welcome, %s !</h1>" %username
        else:
            return "<h1>login Failure !</h1>"
    else:
        return "<h1>login Failure !</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1',5000)

