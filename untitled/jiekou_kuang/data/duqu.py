#!/usr/bin/python
# -*- coding:utf-8 -*-

import xlrd
def shuju():
    shuj=[]
    f=xlrd.open_workbook(r'C:\Users\wang\Desktop\jiekou.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        shuj.append(sheet.row_values(i))
    # print(shuj)

    return shuj
shuju()
def guidd():
    guid=[]
    f=xlrd.open_workbook(r'C:\Users\wang\Desktop\gd.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        guid.append(sheet.row_values(i))

    # print(guid)

    return guid

