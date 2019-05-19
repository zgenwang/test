#!/usr/bin/python
# -*- coding:utf-8 -*-
# from appium import webdriver
# from time import sleep
#
#
# class DS(object):
#
#     # 测试脚本与appium服务器进行连接的参数数据
#     d = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "9",
#         "deviceName": "b6858ab5",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
#
#     # 建立连接的函数
#     def __init__(self):
#
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
#         sleep(3)
#
#     #跳转至手机号/密码登录页面函数
#
#     def tiao_zhuan(self):
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#
#     def login(self,phone,password):
#
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
#
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(3)
#         # self.dr.find_element_by_name('android.widget.RelativeLayout').click()
#         # self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
#
#     # 检查那四个文字的函数/方法
#     # def check_text(self):
#
#         # 获取微信文字
#         # text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         # print(text)
#         # return text
#
#     # 关闭app的函数
#     def close_app(self):
#         self.dr.quit()
#
#
# if __name__ == '__main__':
#     go = DS()  # 创建一个DS类的实例，赋值给变量go
#     # 调用DS类的方法
#
#     go.tiao_zhuan()
#     go.login('18272981597','199783.zgw')
#     # go.check_text()
#     #关闭手机app
#     # go.close_app()
from time import sleep
import unittest
from appium import webdriver
class ce(unittest.TestCase):
    a = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "b6858ab5",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    # @classmethod
    # def setUpClass(cls):
    #     cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    def join(self,name,password):
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        sleep(2)

        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(2)
        print('准备登陆')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)
    # def test_1(self):
    #     self.join('18272981597','199783.zgw')
    #     sleep(2)
    #     print('开始断言')
    #     text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
    #     self.assertEqual(text,'热门')



    #app退出登录
    def logout(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        print(a)
        sleep(5)
        a[3].click()
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
        self.dr.quit()




    # @classmethod
    # def tearDownClass(cls):
        # cls.dr.quit()
# if __name__ == '__main__':
    # unittest.main()

go=ce()
go.join('18272981597', '199783.zgw')
sleep(2)
go.logout()
