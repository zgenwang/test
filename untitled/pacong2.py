#!/usr/bin/python
# -*- coding:utf-8 -*-
# import xlwt
# import xlrd
# from xlutils.copy import copy
# a=[x for x in range(25)]
# b=[x for x in range(50,75)]
# r=[x for x in range(100,125)]
# g=[x for x in range(150,175)]
# try:
#     ff=xlrd.open_workbook('aaa.xls')
#     sheet1=ff.sheets()[0]
#     num=sheet1.nrows
#     new_f=copy(ff)
#     sheet=new_f.get_sheet(0)
#     for i,j in enumerate(r):
#         sheet.write(num+i,0,j)
#         sheet.write(num+i,1,g[i])
#     new_f.save('aaa.xls')
# except:
#     ff=xlwt.Workbook()
#     sheet=ff.add_sheet('糗事')
#     sheet.write(0,0,'作者')
#     sheet.write(0,1,'段子')
#     for i,j in enumerate(a):
#         sheet.write(i+1,0,j)
#         sheet.write(i+1,1,b[i])
#         ff.save('aaa.xls')
# import requests
# import re
# class diany(object):
#     def qingqiu(self,a):
#         url='https://movie.douban.com/top250?start={}&filter='.format(25*i)
#         head={'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         a=re.compile('<img width="100" alt="(.*?)"',re.S)
#         bb=a.findall(abc)
#         b=re.compile('src="(.*?)" class="">')
#         d=b.findall(abc)
#         e=dict(zip(bb,d))
#         print(e)
#         return e
#     def save(self,shu):
#         for i,j in shu.items():
#             res=requests.get(j)
#             qq=res.content
#             # with open('{}.jpg'.format(i),'ab') as f:
#             #     f.write(qq)
# tu=diany()
# for i in range(5):
#     ab=tu.qingqiu(i)
#     e=tu.guolv(ab)
#     # tu.save(e)
import requests
from xlutils.copy import copy
import xlwt
import xlrd
import re
class douban(object):
    def fasongqingqiu(self,page):
        url='https://movie.douban.com/top250?start={}&filter='.format(page)
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'

        }
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,abc):
        a=re.compile('<img width="100" alt="(.*?)"',re.S)
        b = a.findall(abc)
        c=re.compile(r'导演:(.*?)&nbsp;&nbsp;',re.S)
        d=c.findall(abc)
        e=re.compile(r'<div class="star">(.*?) </div>',re.S)
        f=e.findall(abc)
        aa=re.compile(r'property="v:average">(.*?)</span>',re.S)
        bb=aa.findall(abc)
        cc=[]
        for i in f:
            h=re.compile('<span>(.*?)</span>',re.S)
            j=h.findall(i)
            cc.append(j[0])
        return b,d,cc,bb
    def save(self,m,mm,mmm,mmmm):
        import pymysql
        conn=pymysql.connect(host='192.168.1.120',
                             port=3306,
                            user='root',
                            passwd='123456')
        #创建游标 类似vim光标
        abc=conn.cursor()
        # abc.execute('create database python_test;')
        abc.execute('use python_test')
        # try:
        # for i,j in enumerate(m):
        #     abc.execute('create table douban(电影名称 char(255),导演 char(255),评价 char(255),评分 char(255));')
        for i, j in enumerate(m):
            print(j,mm[i],mmm[i],mmmm[i])
            # abc.execute('insert into douban values("{}","{}","{}","{}");'.format(j, mm[i], mmm[i], mmmm[i]))
        # except:
        #     for i, j in enumerate(m):
        #         abc.execute('insert into douban values("{}","{}","{}","{}");'.format(j,mm[i],mmm[i],mmmm[i]))



        # try:
        #     ff=xlrd.open_workbook('movie.xls')
        #     sheet1=ff.sheets()[0]
        #     num=sheet1.nrows
        #     new=copy(ff)
        #     sheet=new.get_sheet(0)
        #     for i,j in enumerate(m):
        #         sheet.write(num+i,0,j)
        #         sheet.write(num+i,1,mm[i])
        #         sheet.write(num+i,2,mmm[i])
        #         sheet.write(num+i,3,mmmm[i])
        #         new.save('movie.xls')
        # except:
        #     ff=xlwt.Workbook()
        #     sheet=ff.add_sheet('dianying')
        #     sheet.write(0,0,'电影名称')
        #     sheet.write(0,1,'导演')
        #     sheet.write(0,2,'评价人数')
        #     sheet.write(0,3,'评分')
        #     for i,j in enumerate(m):
        #         sheet.write(i+1,0,j)
        #         sheet.write(i+1,1,mm[i])
        #         sheet.write(i+1,2,mmm[i])
        #         sheet.write(i+1,3,mmmm[i])
        #         ff.save('movie.xls')

for rr in range(25,125,25):

    tu=douban()
    ab=tu.fasongqingqiu(rr)
    x,xx,xxx,xxxx=tu.guolv(ab)
    tu.save(x,xx,xxx,xxxx)
