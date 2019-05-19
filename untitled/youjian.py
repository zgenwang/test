#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
conn=pymysql.connect(host='192.168.1.13',port=3306,user='root',passwd='123456')
abc=conn.cursor()
abc.execute('use bosss')
abc.execute('select * from bo')
a=abc.fetchall()
import xlwt
v=[]
vv=[]
vvv=[]
vvvv=[]
vvvvv=[]
for i in a:
    v.append(i[0])
    vv.append(i[1])
    vvv.append(i[2])
    vvvv.append(i[3])
    vvvvv.append(i[4])
ff=xlwt.Workbook()
sheet=ff.add_sheet('boss')
sheet.write(0,0,'职位')
sheet.write(0,1,'薪资')
sheet.write(0,2,'地址')
sheet.write(0,3,'经验')
sheet.write(0,4,'融资情况')
for i,j in enumerate(v):
    sheet.write(i+1,0,j)
    sheet.write(i+1,1,vv[i])
    sheet.write(i+1,2,vvv[i])
    sheet.write(i+1,3,vvvv[i])
    sheet.write(i+1,4,vvvvv[i])
ff.save('e.xls')


