#!/usr/bin/python
# -*- coding:utf-8 -*-
# c=int(input('>>>'))
# print()
# for i in  range(1,51):
#     for j in range(1,101):
#         for a in range(1,201):
#             b=1/2
#             if i*2+j+b*a ==100 and i*4+j*2+a==200:
#                 print(i,j,a)
# try:
#     a=15
#     print(a)
# except  Exception as d:
#     print(d)
# else:
#     print(123)
# finally:
#     print('hello')
# a=int(input('>>>'))
# if a>3:
#     raise NameError('hello')
# else:
#     raise TypeError('123')
# 十六进制转十进制
# a=[str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
# b=int(input('>>>'))
# f=[]
# while True:
#    c=b%16
#    b=b//16
#    print(c,b)
#    f.append(a[c])
#    print(f)
#    if b==0:
#       break
# f.reverse()
# f="".join(f)
# print("0x{}".format(f))
# c=b.content.decode('utf-8')
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# f=d.findall(c)
# dd=re.compile('<h2>(.*?)</h2>',re.S)
# fff=dd.findall(c)
# ff=[]
# ffff=[]
# for i in f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
# for j in fff:
#     j=j.replace('\n','')
#     ffff.append(j)
# for x in range(len(ff)):
#     ff.insert(x*2,ffff[x])
# with open('c.txt','w',encoding='utf-8')as g:
#     for i in ff:
#         g.write(i+'\n')
# import xlwt
# with open('a.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('shuju')
# for i in range(len(a)):
#     k=a[i].split(',')
#     for j in range(len(k)):
#         sheet.write(i,j,k[j])
#         ff.save('a.xls')
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# c=sheet.nrows
# with open('d.txt','w',encoding='utf-8') as g:
#     for i in range(c):
#         i=sheet.row_values(i)
#         for j,k in enumerate(i):
#             if j==len(i)-1:
#                 g.write(k)
#             else:
#                 g.write(k+',')
import os
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,i*j),end='')
#     print()
import os
import xlwt
# f=open('v.txt','w+r',encoding='utf-8')
# for i in range(10):
#     f.write(str(i))
#     f.write('\n')
#     f.read()
# os.remove('v.txt')
# with open('v.txt','r',encoding='utf-8')as ff:
#     ff.read()
with open('a.txt','r',encoding='utf-8') as f:
    a=f.readlines()
b=len(a)
print(b)







