#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
import xlrd
import HTMLTestRunner
def shuju():
    shuj=[]
    f=xlrd.open_workbook(r'C:\Users\wang\Desktop\jiekou.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        shuj.append(sheet.row_values(i))
    print(shuj)

    return shuj





class qwe(unittest.TestCase):
    qq=shuju()
    print(qq)
    def denglu(self,user,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(user,password)
        headers = {
        'Content-Type': "application/json",
        'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
        'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
        'Language': "zh_CN",
        'APIVersion': "3.0",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "c7eade18f88247d88ffdbdfb0b062ad4",
        'Host': "120.132.8.33:9000",
        'accept-encoding': "gzip, deflate",
        'content-length': "150",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        res=response.json()
        return res

    def test_1(self):
        aa=self.denglu(int(self.qq[0][0]),int(self.qq[0][1]))
        self.assertEqual(aa['code'],0)

    def test_2(self):
        for i in range(2,5):
         bb=self.denglu(int(self.qq[i][0]),int(self.qq[i][1]))
         self.assertNotEqual(bb['code'],0)


if __name__ == '__main__':
    # 创建一个测试套件
    # suit = unittest.TestSuite()
#     #将测试用例添加到测试套件中
#     suit.addTest(qwe('test_1'))
#     suit.addTest(qwe('test_2'))
#     #将qwe类中所有以test开头的函数都添加到测试套件中
#     suit.addTest(unittest.makeSuite(qwe))
#     #打开一个空文件
#     f = open('abc.html','wb')
#     #定义测试报告信息
#     runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='庄根望',description='结果如下')
#     runner.run(suit)
#     f.close()

    unittest.main()

