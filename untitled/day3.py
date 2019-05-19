#!/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('>>>以逗号隔开')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)
a=[('游艇',188),('电脑',4000),('鼠标',30),('美女',998)]
for i,j in enumerate(a):
    print(i+1,j)
b=0 #余额
c=[] #购物车
while True:
    b=input("请输入您的工资：")
    if(b.isdigit()):
        b=int(b)
        while True:
            id=input("请输入商品ID:")
            if id==121:
                print(c)
            if id.isdigit():  #是数字
                id=int(id)-1
                if(id>=0 and id<len(a)):
                    if b>=a[id][1]:
                        c.append(a[id])
                        b-=a[id][1]
                        print('退出并结算请输入q')
                        print(c)
                    elif b < a[id][1]:
                        print("您的余额不足！还差{},请充值".format(a[id][1]-b))
                        money=int(input('请输入充值金额'))
                        b+=money
                        print("充值成功，余额为{}".format(b))
                else:
                    print("商品不存在")
            elif id=='q':
                print("您购买的商品有：%s,您的余额为%s"%(c,b))
                exit()
            else:
                print("商品ID格式不正确")
        break
    else:
        print("您的工资格式不正确！")
