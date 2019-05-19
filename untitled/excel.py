#!/usr/bin/python
# -*- coding:utf-8 -*-
# import xlwt
# # with open('b.txt','r',encoding='utf-8') as f:
# #     a=f.readlines()
# # f=xlwt.Workbook()
# # sheet=f.add_sheet('数据')
# # for i in range(len(a)):
# #     k=a[i].split(',')
# #     for j in range(len(k)):
# #         sheet.write(i,j,k[j])
# # f.save('a.xls')
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# c=sheet.nrows
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(c):
#         i=sheet.row_values(i)
#         for j,k in enumerate(i):
#             if j==len(i)-1:
#                 f.write(k)
#             else:
#                 f.write(k+',')
# import time
# a=input('请输入年份:')
# b=a.split(' ')
# c=[]
# for i in b:
#     c.append(int(i))
# if c[0]%4==0:
#     if c[0]%100==0:
#         if c[0]%400==0:
#             print('yes')
#         else:
#             print('no')
#     else:
#         print('yes')
# else:
#     print('no')
#
# k =time.strptime('{} {} {}'.format(c[0],c[1],c[2]),'%Y %m %d')
# print('今天星期{}'.format(k[-3]+1))
# print('今年的第{}天'.format(k[-2]))
# import time
# c=[]
# a=input('请输入年份:')
# b=time.strptime(a,'%Y-%m-%d')
# for i in b:
#     c.append(i)
# c=tuple(c)
# print(c)
# d=time.mktime(c)
# d=d-86400
# t=time.localtime(d)
# g=time.strftime('%Y-%m-%d',t)
# print(g)
from xlutils.copy import copy
import xlrd
import xlwt
import requests
import json
# class  zhilian():
#     def qingqiu(self):
#         a='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件&kt=3&_v=0.54754575&x-zp-page-request-id=9702e63516a24d59a5b31793e376aa3e-1554174510657-110708'
#         oo={'Host': 'fe-api.zhaopin.com'
#         'User-Agent:' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#         'Accept:' 'application/json, text/plain, */*'
#         'Accept-Language:' 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
#         'Accept-Encoding:' 'gzip, deflate, br'
#         'Referer:' 'https://sou.zhaopin.com/?jl=538&kw=%E8%BD%AF%E4%BB%B6&kt=3'
#         'Origin:' 'https://sou.zhaopin.com'
#         'Connection:' 'keep-alive'
#         }
#         b=requests.get(a,headers=00)
#         c=b.content.decode('utf-8')
#         asd=json.loads(c)
#         return  asd
#     def  guolv(self,c):
#         r = []
#         rr = []
#         rrr = []
#         rrrr = []
#         rrrrr = []
#         for i in range(90):
#             z=(c['data']['results'][i]['jobName'])
#             zz=(c['data']['results'][i]['updateDate'])
#             zzz=(c['data']['results'][i]['city']['display'])
#             zzzz=(c['data']['results'][i]['workingExp']['name'])
#             zzzzz=(c['data']['results'][i]['jobTag']['searchTag'])
#             r.append(z)
#             rr.append(zz)
#             rrr.append(zzz)
#             rrrr.append(zzzz)
#             rrrrr.append(zzzzz)
#         return r,rr,rrr,rrrr,rrrrr
#     def save(self,n,nn,nnn,nnnn,nnnnn):
#         try:
#             ff=xlrd.open_workbook('zhilian.xls')
#             sheet1=ff.sheets()[0]
#             num=sheet1.nrows
#             new=copy(ff)
#             sheet=new.get_sheet(0)
#             for i,j in enumerate(n):
#                 sheet.write(num+i,0,j)
#                 sheet.write(num+i,1,nn[i])
#                 sheet.write(num+i,2,nnn[i])
#                 sheet.write(num+i,3,nnnn[i])
#                 sheet.write(num+i,4,nnnnn[i])
#                 new.save('zhilian.xls')
#         except:
#             ff=xlwt.Workbook()
#             sheet=ff.add_sheet('zhaoping')
#             sheet.write(0,0,'岗位')
#             sheet.write(0,1,'日期')
#             sheet.write(0,2,'地址')
#             sheet.write(0,3,'工作经历')
#             sheet.write(0,4,'福利')
#             for i,j in enumerate(n):
#                 sheet.write(i+1,0,j)
#                 sheet.write(i+1,1,nn[i])
#                 sheet.write(i+1,2,nnn[i])
#                 sheet.write(i+1,3,nnnn[i])
#                 sheet.write(i+1,4,nnnnn[i])
#                 ff.save('zhilian.xls')
#
#
#
# zl=zhilian()
# e=zl.qingqiu()
# t,tt,ttt,tttt,ttttt=zl.guolv(e)
# print(t,tt,ttt,tttt,ttttt)
# zl.save(t,tt,ttt,tttt,ttttt)




