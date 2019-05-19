#!/usr/bin/python
# -*- coding:utf-8 -*-
# import time
# # a=time.time()
# # print(a)
# # 以元祖的格式显示本地时间等信息
# # # 默认本地时间
# # a=time.localtime(13413451333)
# # # 以本地化时间显示
# # b=time.strftime('%Y-%m-%d %H:%M:%S %w',a)
# # print(b)
# # 将元祖时间转换为时间戳
# # a=(1988,8,8,8,8,8,8,8,8,)
# # b=time.mktime(a)
# # print(b)
# # a=time.strptime('2012-2-2','%Y-%m-%d')
# # print(a)
# # 休眠
# # for i in range(9):
# #     print(i)
# #     time.sleep(2)
# # a=input('请输入年 月 日:')
# # b=a.split(' ')
# # c=[]
# # for i in b:
# #     c.append(int(i))
# # if c[0]%4==0:
# #     if c[0]%100==0:
# #         if c[0]%400==0:
# #             print('yes')
# #         else:
# #             print('no')
# #     else:
# #         print('yes')
# # else:
# #     print('no')
# #
# # k=time.strptime('{} {} {}'.format(c[0],c[1],c[2]),'%Y %m %d' )
# # print('星期{}'.format(k[-3]+1))
# # print('一年中的第{}'.format(k[-2]))
# import time
# a=input('请输入年份:')
# b=time.strptime(a,'%Y-%m-%d')
# # c=[]
# # for i in b:
# #     c.append(i)
# # c=tuple(c)
# # print(c)
# d=time.mktime(b)
# e=d-86400
# f=time.localtime(e)
# g=time.strftime('%Y-%m-%d',f)
# print(g)
# a=int(input('>>>'))
# b=0
# c=1
# for i in range(1,a+1):
#     c=c*i
#     b=b+c
# print(b)
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(a)
# a=input('>>>')
# for i in range(len(a)-1):
#     if a[i] !=a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')
a=input('>>>')
b=a[::-1]
c=0
for i in range(len(b)):
    for j in range(10):
        if str(j)==b[i]:
            c=c+j*10**i
print(c)
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for k in a:
#             if i !=j and i!=k and j != k:
#                 print(i,j,k)
# a=[str(x) for x in range(10)]+[chr(x) for x in range(97,103)]
# b=int(input('>>>'))
# c=[]
# while True:
#     d=b%16
#     b=b//16
#     c.append(a[d])
#     if b==0:
#         break
# c.reverse()
# c=''.join(c)
# print(c)
# def a(b,c):
#     b=tuple(b)
#     c=int(c)
#     for j,k in range(len(b)):
#         if j+k==c:
#             print(j,k)
#
# print(a((2,3),5))
# def xx(a,b):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==b:
#                 print(a[i],a[j],b)
# xx((1,2,3,4,6,7),6)
# import  re
# a='Qweq23q2q'
# p = re.compile('q(.*?)q',re.I)
# c=p.findall(a)
# print(c)
# import requests
# import re
# for i in range(1,5):
#     a='https://www.qiushibaike.com/text/page/{}/'.format(i)
#     oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#
#     }
#     b=requests.get(a,headers=oo)
#     c=b.content.decode('utf-8')
#     e=re.compile('<div class="content">(.*?)</span>',re.S)
#     q=e.findall(c)
#     t=re.compile('<h2>(.*?)</h2>',re.S)
#     zz=t.findall(c)
#     o=[]
#     ooo=[]
#     for i in q:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         o.append(i)
#     for qq in zz:
#         qq=qq.replace('/n','')
#         ooo.append(qq)
#     for x in range(len(o)):
#         o.insert(x*2,ooo[x])
#     with open('b.txt', 'a', encoding='utf-8-sig') as f:
#         for j in o:
#             f.write(j+'\n')
#             aa=f.readlines()
#             bb=aa.split('/n')
#             import xlwt
#             ff=xlwt.Workbook()
#             sheet=ff.add_sheet('数据')
















