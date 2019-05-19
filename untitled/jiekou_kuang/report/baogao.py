#!/usr/bin/python
# -*- coding:utf-8 -*-
from jiekou_kuang.report import HTMLTestRunner
import unittest
from jiekou_kuang.jiekou_test.test_denglu import guojiaa
from jiekou_kuang.jiekou_test.test_denglu import geren
from jiekou_kuang.jiekou_test.test_denglu import binglii
# from jiekou_kuang.jiekou_test.test_denglu import qwe
def baogao(name):


        suit = unittest.TestSuite()
        for i in name:
        #文件路径  通配符
                dis=unittest.defaultTestLoader.discover(r'F:\PycharmProjects\untitled\jiekou_kuang\jiekou_test',pattern='test_{}.py'.format(i.strip()))
                for j in dis:
                        suit.addTest(j)
        #将测试用例添加到测试套件中
        # suit.addTest(qwe('test_1'))
        # suit.addTest(qwe('test_2'))
        #将qwe类中所有以test开头的函数都添加到测试套件中
        # suit.addTest(unittest.makeSuite(qwe))
        #打开一个空文件
        f = open(r'F:\PycharmProjects\untitled\jiekou_kuang\report\baogao.html','wb')
        #定义测试报告信息
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='庄根望',description='结果如下')
        runner.run(suit)
        f.close()
if __name__=='__main__':
        pass
# baogao()
def baogao2():
        suit = unittest.TestSuite()
        # 文件路径  通配符
        # dis = unittest.defaultTestLoader.discover(r'F:\PycharmProjects\untitled\jiekou_kuang\jiekou_test',pattern='test_*.py')
        # for i in dis:
        #         suit.addTest(i)
        # 将测试用例添加到测试套件中
        suit.addTest(geren('test_c'))
        suit.addTest(geren('test_x'))
        # 将qwe类中所有以test开头的函数都添加到测试套件中
        # suit.addTest(unittest.makeSuite(geren))
        # 打开一个空文件
        f = open(r'F:\PycharmProjects\untitled\jiekou_kuang\report\baogao2.html', 'wb')
        # 定义测试报告信息
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下')
        runner.run(suit)
        f.close()
# baogao2()
def baogao3():
        suit=unittest.TestSuite()
        suit.addTest(unittest.makeSuite(guojiaa))
        f=open(r'F:\PycharmProjects\untitled\jiekou_kuang\report\baogao3.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下')
        runner.run(suit)
        f.close()
# baogao3()
def baogao4():
        suit=unittest.TestSuite()
        suit.addTest(unittest.makeSuite(binglii))
        f = open(r'F:\PycharmProjects\untitled\jiekou_kuang\report\baogao4.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下')
        runner.run(suit)
        f.close()
# baogao4()


