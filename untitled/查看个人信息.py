#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import HTMLTestRunner
import unittest
import requests
import xlrd
def guidd():
    guid=[]
    f=xlrd.open_workbook(r'C:\Users\wang\Desktop\gd.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        guid.append(sheet.row_values(i))

    print(guid)

    return guid
guidd()


class qingqiu(unittest.TestCase):
    zz=guidd()
    def chaxun(self,guid_1,guid_2):


        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = '{"accountGuid":"%s","countryGuid":"%s"}' % (guid_1,guid_2)

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'accessToken': "71d57dbbb35e442e8656f024a3981b67",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "d23668a5-490e-4f04-8b4e-7836c8c034e8,dba43197-426f-49d5-8a2e-48113af1f29b",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res=response.json()
        return res

        # print(response.text)
    def test_1(self):
        qq=self.chaxun(self.zz[0][0],self.zz[0][1])
        self.assertEqual(qq['code'],0)
    def test_2(self):
        aa=self.chaxun(self.zz[1][0],self.zz[1][1])
        self.assertNotEqual(aa['code'],1)
if __name__=='__main__':
#     suit=unittest.TestSuite()
#     suit.addTest(unittest.makeSuite(qingqiu))
#     f=open('aaa.html','wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='庄根望',description='结果如下')
#     runner.run(suit)
#     f.close()
    unittest.main()