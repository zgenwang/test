#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
#面向对象
class  Ds(unittest.TestCase):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "b6858ab5",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    # def setUp(self):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
        sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


    def test_1(self):

        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView') .text

        #断言
        self.assertEqual(text,'微信')

    def test_2(self):

        text2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView') .text
        self.assertEqual(text2,'微博')

    def test_3(self):

        text3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView') .text

        self.assertEqual(text3,'QQ')

    def test_4(self):

        text4 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView') .text

        self.assertEqual(text4,'密码')


    # def tearDown(self):



if __name__== '__main__':
        unittest.main()
    # def __init__(self):
    #     #建立连接的函数
    #     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
    #     sleep(5)

#     def check_text(self):
#         #获取微信函数
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView') .text
#         print(text)
#         return text
#
#     #关闭app的函数
#     def close_app(self):
#         self.dr.quit()
#
# if __name__ == '__main__':
#     go = Ds() #创建一个DS类的实例,赋值给变量go
#     #调用Ds类的方法
#     go.check_text()
#     go.close_app()