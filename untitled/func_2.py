#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml

with open(r'F:\PycharmProjects\untitled\aa.yaml','r',encoding='utf-8') as f:
    qq = yaml.load(f,Loader=yaml.FullLoader)

def sc(driver):
    text = driver.dr.find_elements_by_class_name('android.widget.TextView')
    print(text)
    return text
def wd(driver):
    text1 = driver.dr.find_elements_by_class_name('android.widget.TextView')
    print(text1)
    return text1

