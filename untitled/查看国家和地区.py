#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import requests
class guojia(unittest.TestCase):
    def diqu(self):

        url = "http://120.132.8.33:9000/api/Others/GetCountryList"

        payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n\r\n"
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "69b77552-5ca9-4ba6-9ae4-3e1cb689daf4,ef1a6b84-3574-4fb7-ad3a-db18b6801c3d",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "154",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers)
        res=response.json()
        # print(res)
        return res


        # print(response.text)
    def test_guo(self):
        aa=self.diqu()

        self.assertEqual(aa['data']['A'][0]['guid'],"2fdd7d26-25f2-11e9-a4d7-0242ac120003")

    def test_jia(self):
         bb=self.diqu()
         self.assertNotEqual(bb['code'],1)

if __name__=='__main__':
    # unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(guojia('test_1'))
    suit.addTest(guojia('test_2'))
    # suit.addTest(unittest.makeSuite(guojia))
    f=open(r'F:\PycharmProjects\untitled\a.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='庄根望',description='结果如下')
    runner.run(suit)
    f.close()



