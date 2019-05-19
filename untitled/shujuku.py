#!/usr/bin/python
# -*- coding:utf-8 -*-
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
    # def save(self,m,mm,mmm,mmmm):
    #     import pymysql
    #     conn=pymysql.connect(host='192.168.1.11',
    #                  port=3306,
    #                  user='root',
    #                  passwd='123456')
    #     abc=conn.cursor()
    #     abc.execute('use douban;')
    #     conn.commit()
    #     for i, j in enumerate(m):
    #             abc.execute('insert into douban values("{}","{}","{}","{}");'.format(j,mm[i],mmm[i],mmmm[i]))


# abc=conn.cursor()
# abc.execute()
for rr in range(25,125,25):

    tu=douban()
    ab=tu.fasongqingqiu(rr)
    print(tu.guolv(ab))
    # x,xx,xxx,xxxx=tu.guolv(ab)
    # tu.save(x,xx,xxx,xxxx)
