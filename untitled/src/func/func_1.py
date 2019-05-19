#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
from appium import webdriver
with open(r'F:\PycharmProjects\untitled\src\element\a.yaml','r',encoding='utf-8') as fb:
   # a = yaml.load(fb) 使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data = yaml.load(fb)
# print(item_data)

# dr='xxx'
def foo(driver):
    # dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    # driver=dr
    text = driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    print(text)
    return text
def wb(driver):
    # dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    # driver=dr
    text1 = driver.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
    print(text1)
    return text1
def qq(driver):
    # dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    # driver=dr
    text2 = driver.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
    print(text2)
    return text2
def mima(driver):
    # dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    # driver=dr
    text3 = driver.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
    print(text3)
    return text3