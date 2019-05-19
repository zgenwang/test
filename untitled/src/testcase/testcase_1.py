#!/usr/bin/python
# -*- coding:utf-8 -*-
from src.func.func_1 import foo,wb,qq,mima
from appium import webdriver
from time import sleep
import unittest
from HTMLTestRunner import HTMLTestRunner
from src.aaa import REPORT_PIR
from src.testcase.log import get_logger

# 给日志一个变量 g是全局变量
g = get_logger(name='testcase_1.py')


#测试脚本
class text(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
                a = {
                        "device": "android",
                        "platformName": "Android",
                        "platformVersion": "9",
                        "deviceName": "b6858ab5",
                        "appPackage": "com.qk.butterfly",
                        "appActivity": ".main.LauncherActivity",
                        "noReset": "True"
                }
                cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
                sleep(5)
        g.info('建立连接')
        @classmethod
        def tearDownClass(cls):
                cls.dr.quit()
        g.info('断开连接')
#测试用例代码
        def test_1(self):
                g.info('执行测试用例1')
                text = foo(self.dr)
                self.assertEqual(text,'微信')

                #验证微信的用例

        def test_2(self):
                g.info('执行测试用例2')
                text = wb(self.dr)
                self.assertEqual(text,'微博')

        def test_3(self):
                g.info('执行测试用例3')
                text = qq(self.dr)
                self.assertEqual(text,'QQ')

        def test_4(self):
                g.info('执行测试用例4')
                text = mima(self.dr)
                self.assertEqual(text,'密码')

#运行测试脚本，生成测试报告
if __name__ == '__main__':
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(text))
        r_path = r'F:\PycharmProjects\untitled\src\report\a.html'
        #将路径写死
        # r_path_1 = REPORT_PIR 'HTML'
        # suit.addTest(text('test_1'))
        # suit.addTest(text('test_2'))
        # suit.addTest(text('test_3'))
        # suit.addTest(text('test_4'))
        with open(r'F:\PycharmProjects\untitled\src\a.html', 'wb')  as f:
                runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下',verbosity=2)
                runner.run(suit)










