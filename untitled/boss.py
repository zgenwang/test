#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import xlrd
import xlwt
from xlutils.copy import copy
import re
class  boss(object):
    def qingqiu(self,page):
        url='https://www.zhipin.com/c101020100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&page={}&ka=page-2'.format(page)
        head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,qqq):
        a=re.compile('<div class="job-title">(.*?)</div>',re.S)
        aa=a.findall(qqq)
        b = re.compile(r'<span class="red">(.*?)</span>',re.S)
        bb=b.findall(qqq)
        c=re.compile(r'<div class="info-detail"></div>(.*?)</div>',re.S)
        cc=c.findall(qqq)
        vvv=[]
        ddd=[]
        eeee=[]
        for i in cc:
            v=re.compile(r'<p>(.*?)<em class="vline">',re.S)
            vv=v.findall(i)
            vvv.append(vv)
        for i in cc:
            d=re.compile(r'</em>(.*?)<em class="vline">',re.S)
            dd=d.findall(i)
            ddd.append(dd)
        e=re.compile(r'<div class="company-text">(.*?)</div>',re.S)
        ee=e.findall(qqq)
        for j in ee:
            eee=re.compile(r'</em>(.*?)<em',re.S)
            o=eee.findall(j)
            eeee.append(o)

        return aa,bb,vvv,ddd,eeee
    def save(self,m,mm,mmm,mmmm,mmmmm):
        try:
            ff=xlrd.open_workbook('boss.xls')
            sheet1=ff.sheets()[0]
            num=sheet1.nrows
            new=copy(ff)
            sheet=new.get_sheet(0)
            for i,j in enumerate(m):
                sheet.write(num+i,0,j)
                sheet.write(num+i,1,mm[i])
                sheet.write(num+i,2,mmm[i])
                sheet.write(num+i,3,mmmm[i])
                sheet.write(num+i,4,mmmmm[i])
                new.save('boss.xls')
        except:
            ff=xlwt.Workbook()
            sheet=ff.add_sheet('molv')
            sheet.write(0,0,'岗位')
            sheet.write(0,1,'薪资')
            sheet.write(0,2,'地区')
            sheet.write(0,3,'经验')
            sheet.write(0,4,'融资情况')
            for i,j in enumerate(m):
                sheet.write(i+1,0,j)
                sheet.write(i+1,1,mm[i])
                sheet.write(i+1,2,mmm[i])
                sheet.write(i+1,3,mmmm[i])
                sheet.write(i+1,4,mmmmm[i])
                ff.save('boss.xls')
bo=boss()
for i in range(6):
    r=bo.qingqiu(i)
    rr,rrr,rrrr,rrrrr,rrrrrr=bo.guolv(r)
    bo.save(rr,rrr,rrrr,rrrrr,rrrrrr)
f=xlrd.open_workbook('boss.xls')
sheet=f.sheets()[0]
import pymysql
conn=pymysql.connect(host='192.168.1.13',port=3306,user='root',passwd='123456')
abc=conn.cursor()
abc.execute('create database bosss;')
abc.execute('use bosss;')
abc.execute('create table bo(q char(255),qq char(255),qqq char(255),qqqq char(255),qqqqq char(255));')
h=sheet.nrows
for i in range(1,h):
    i=sheet.row_values(i)
    abc.execute('insert into bo values ("{}","{}","{}","{}","{}");'.format(i[0],i[1],i[2],i[3],i[4]))
abc.execute('select * from bo')
a=abc.fetchall()
b=len(a)
import smtplib
import email.mime.multipart
import email.mime.text
if b>1000:
    fr='18272981597@163.com'
    res='1737123574@qq.com'
    server='smtp.163.com'
    passwd='199783zgw'
    message=email.mime.multipart.MIMEMultipart()
    message['From']=fr
    message['To']=res
    message['subject']='python'
    text='hello'
    tex=email.mime.text.MIMEText(text)
    message.attach(tex)
    smtplib123=smtplib.SMTP_SSL(server,465)
    smtplib123.login(fr,passwd)
    smtplib123.sendmail(fr,res,message.as_string())
else:
    print('hello')













