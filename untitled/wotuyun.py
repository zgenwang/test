#!/usr/bin/python
# -*- coding:utf-8 -*-
# from appium import webdriver
# import unittest
#
# from time import sleep
# a={
#       "device": "android",
#       "platformName": "Android",
#       "platformVersion": "9",
#       "deviceName": "b6858ab5",
#       "appPackage": "com.alltuu.android",
#       "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
#       "noReset": "True"
#     }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=a)
# sleep(10)
                  # return dr
  # def denglu(self):
  #   sleep(10)
  #
  #   q=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.EditText')
  #   q[0].clear()
  #   q[0].send_keys(15093060665)
  #   q[1].clear()
  #   q[1].send_keys(123456)
  #   qq=self.dr.find_elements_by_class_name('android.view.ViewGroup')
  #   print(len(qq))
  #   qq[14].click()
# a = dr.find_element_by_id('android:id/content').find_element_by_class_name('android.widget.TextView').text
# print(a)
# a = dr.find_elements_by_class_name('android.widget.ImageView')
# print(a)
# aa=a[15].text
# a[9].click()
# print(aa)
from func_2 import sc,wd
from appium import webdriver
from time import sleep
import unittest
from HTMLTestRunner import HTMLTestRunner
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
    def test_1(self):

        a = self.dr.find_elements_by_class_name('android.widget.TextView')
        print(a)
        aa = a[16].text
        self.assertEqual(aa,'闪传')
    def test_2(self):
        a = self.dr.find_elements_by_class_name('android.widget.TextView')
        aaa = a[17].text
        self.assertEqual(aaa,'我的')

if __name__ == '__main__':
      suit = unittest.TestSuite()
      suit.addTest(unittest.makeSuite(lj))
      with open(r'F:\PycharmProjects\untitled\aaaa.html', 'wb')  as f:
            runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下', verbosity=2)
            runner.run(suit)
    # unittest.main()



