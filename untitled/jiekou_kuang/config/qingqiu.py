#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
from jiekou_kuang.data.duqu import guidd
from jiekou_kuang.data.duqu import shuju
class jiekou_qingqiu(unittest.TestCase):
    # qq=shuju()
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
if __name__=='__main__':
    shu=shuju()
    for i in range(len(shu)):
        # print(shu)
        aa = jiekou_qingqiu().denglu(int(shu[i][0]),int(shu[i][1]))
        # print(aa)
class gerenxinxi():
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
if __name__=='__main__':
    guid=guidd()
    for i in range(len(guid)):
        a=gerenxinxi().chaxun(guid[i][0],guid[i][1])
        print(a)
# gerenxinxi()
class guojia():
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
class bingli():
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
        res = response.json()
        # print(res)
        return res
# bingli().bl()