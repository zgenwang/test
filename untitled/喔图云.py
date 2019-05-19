#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

from time import sleep
class  lj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        a={
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "b6858ab5",
            "appPackage": "com.alltuu.android",
            "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
            "noReset": "True"
            }
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=a)
        sleep(10)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
                  # return dr
    # def denglu(self):
    #     sleep(10)
    #
    #     q=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.EditText')
    #     q[0].clear()
    #     q[0].send_keys(15093060665)
    #     q[1].clear()
    #     q[1].send_keys(123456)
    #     qq=self.dr.find_elements_by_class_name('android.view.ViewGroup')
    #     print(len(qq))
    #     qq[14].click()

    def test_1(self):

        a = self.dr.find_elements_by_class_name('android.widget.TextView')
        print(a)
        aa = a[16].text
        self.assertEqual(aa,'闪传')
    def test_2(self):
        a = self.dr.find_elements_by_class_name('android.widget.TextView')
        aaa = a[17].text
        self.assertEqual(aaa,'我的')
# lj.denglu()
if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite
    suit.addTest(unittest.makeSuite(lj))
    #     suit.addTest(lj('test_1'))
        # suit.addTest(lj('test_2'))
    with open(r'F:\PycharmProjects\untitled\aaaa.html', 'wb')  as f:
        runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下', verbosity=2)
        runner.run(suit)