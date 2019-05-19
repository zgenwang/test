#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# a=sheet.nrows
# for p in range(len(a)):
#     i=sheet.row_values(p)

class qwe(unittest.TestCase):
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
     aa=self.denglu(15993835273,111111)
     self.assertEqual(aa['code'],0)

 def test_2(self):
     bb=self.denglu(1599383527,111111)
     self.assertNotEqual(bb['code'],0)

 def test_3(self):
     cc=self.denglu(15993835273,11111)
     self.assertNotEqual(cc['code'],0)
if __name__ == '__main__':
 unittest.main()