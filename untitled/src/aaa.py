#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
# 获取当前.py文件的绝对路径
a = os.path.dirname(os.path.abspath(__file__))
print(a)
#项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#日志目录
LOG_DIR = BASE_DIR + '/logs/'
#报告目录
REPORT_PIR = BASE_DIR + '/repore/'
#源文件目录
SRC_DIR = BASE_DIR + '/src/'
#测试用例目录
TEST_CASE = BASE_DIR + '/testcase/'
#页面方法目录
FUNC = BASE_DIR + '/func/'
# 公共目录
UNTIL = BASE_DIR + '/until/'
# from appium import webdriver
# from time import sleep
# a = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "9",
#         "deviceName": "b6858ab5",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
# }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(18272981597)
# #清除输入框中的数据
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(18272981597)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('199783.zgw')
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# print(a)
# sleep(2)
# a[3].click()
# size = dr.get_window_size()
# #获取当前屏幕的分辨率
# x1 = size['width'] * 0.5  # x坐标 50
# y1 = size['height'] * 0.25  # 起始y坐标 50
# y2 = size['height'] * 0.75  # 150
# for i in range(2):
#     dr.swipe(x1, y2, x1, y1)
# dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
# dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
# dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
# dr.quit()

# for i in a:
#     print(i.text)
