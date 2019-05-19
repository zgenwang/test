#!/usr/bin/python
# -*- coding:utf-8 -*-
from jiekou_kuang.report.baogao import baogao
from src.testcase.testcase_1 import text
with open('a.txt','r') as f:
    bb=f.readlines()
if 'all' in bb:
    baogao('*')
else:
    baogao(bb)