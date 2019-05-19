#!/usr/bin/python
# -*- coding:utf-8 -*-
#导入appium模块中的webdriver
#面向过程
from appium import webdriver
from time import sleep
#测试脚本与appium服务器进行连接的参数数据
# d = {
#   "device": "android",
#   "platformName": "Android",
#   "platformVersion": "9",
#   "deviceName": "b6858ab5",
#   "appPackage": "com.qk.butterfly",
#   "appActivity": ".main.LauncherActivity",
#   "noReset": "True"
# }

#测试脚本是appium服务器与手机建立连接的过程
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(10.0)
#元素是id，就使用id定位方法
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()

#获取微信的文字
#先定位上一级，再定位下面的元素，没有id，找class属性，这是元素的多级定位
# text=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView') .text
# text2=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# text3=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# text4=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# print(text,text2,text3,text4)
#插入等待时间,休眠几秒
# sleep(3.0)
# send_keys()输入的是字符串
#什么时候可以用send_keys?
# 1 向手机输入框内输入数据的时候
# 2 clickable --->> true
# # 2 clickable ---》true
# # 3 enabled ---》 true
# # 4 foucsable --》 true
# mima=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18272981597')
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('199783.zgw')
#
# denglu=dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#
# sleep(5)
#退出app，包括后台进程也关掉

#查看登录后的效果
# sleep(10)
# dr.quit()
# import unittest
# import json
# import HTMLTestRunner
# import requests
# class guojia(unittest.TestCase):
#     def diqu(self):
#
#         url = "http://120.132.8.33:9000/api/Others/GetCountryList"
#
#         payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n\r\n"
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'User-Agent': "PostmanRuntime/7.11.0",
#             'Accept': "*/*",
#             'Cache-Control': "no-cache",
#             'Postman-Token': "69b77552-5ca9-4ba6-9ae4-3e1cb689daf4,ef1a6b84-3574-4fb7-ad3a-db18b6801c3d",
#             'Host': "120.132.8.33:9000",
#             'accept-encoding': "gzip, deflate",
#             'content-length': "154",
#             'Connection': "keep-alive",
#             'cache-control': "no-cache"
#             }
#
#         response = requests.request("GET", url, data=payload, headers=headers)
#         res=response.json()
#         print(res)
#         return res
#
#
#         # print(response.text)
#     def test_1(self):
#         aa=self.diqu()
#         self.assertEqual(aa['code'],0)
#
#     def test_2(self):
#          bb=self.diqu()
#          self.assertNotEqual(bb['code'],1)
#
# if __name__=='__main':
#     unittest.main()
#  2019/5/10 14:33:19
# http://222.143.34.190:8081/jyweb
# 张路生 2019/5/12 16:59:25
# from appium import webdriver
# from time import sleep
#
# d={
#   "device": "android",
#   "platformName": "Android",
#   "platformVersion": "9",
#   "deviceName": "b6858ab5",
#   "appPackage": "com.ss.android.ugc.aweme",
#   "appActivity": ".main.MainActivity",
#   "noReset": "True"
# }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# dr.find_element_by_id('com.ss.android.ugc.aweme:id/an8').click()
#
# dr.find_element_by_id('android:id/content').click()
# sleep(2.0)
# dr.find_element_by_class_name('android.support.v4.view.DmtViewPager$MyAccessibilityDelegate').click()
# sleep(2.0)
# dr.quit()
from appium import webdriver
#抖音
from time import sleep
import unittest

from appium import webdriver
import time

a = {
  "device": "android",
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "b6858ab5",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity",
  "noReset": "True"
}
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
while True:
      sleep(3)
      size = dr.get_window_size()
      x1 = size['width'] * 0.5
      y1 = size['height'] * 0.25
      y2 = size['height'] * 0.75
      for i in range(2):
            dr.swipe(x1, y2, x1, y1)
      time.sleep(5)


