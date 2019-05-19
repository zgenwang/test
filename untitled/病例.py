#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import HTMLTestRunner
import unittest
class bingli(unittest.TestCase):
    def bl(self):

        url = "http://120.132.8.33:9000/api/Account/GetAllDiseaseInfo"

        payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n"
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "64681b3b-2e69-4ff0-aa2d-2a8c5a7150f8,06ddf171-02bc-404f-8c1b-5b7d0858a8ed",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "152",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers)
        res=response.json()
        return res

        # print(response.text)
    def test_bing(self):
        aa=self.bl()
        self.assertEqual(aa["data"]["diseaseHistory"][0]["name"],"冠心病",)
    def test_li(self):
        bb=self.bl()
        self.assertNotEqual(bb["code"],1)
if __name__=='__main__':
    # unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(bingli))
    f = open(r'F:\PycharmProjects\untitled\bingli.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='庄根望', description='结果如下')
    runner.run(suit)
    f.close()