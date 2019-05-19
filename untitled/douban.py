#!/usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# # import re
# # class  douban(object):
# #     def fasongqingqiu(self,page):
# #         url='https://movie.douban.com/top250?start={}&filter='.format(page)
# #         head={
# #             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;66.0) Gecko / 20100101Firefox / 66.0'
# #         }
# #         res=requests.get(url,headers=head)
# #         html=res.content.decode('utf-8')
# #         return html
# #     def guolv(self,abc):
# #         lianjie=[]
# #         ming=[]
# #         patt=re.compile('<img width="100"(.*?)</a>',re.S)
# #         itmes=patt.findall(abc)
# #         for i in itmes:
# #             new=re.compile(r' src="(.*?)" class="">')
# #             aaa=new.findall(i)
# #             lianjie.append(aaa[0])
# #         kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
# #         name=kk.findall(abc)
# #         for j in name:
# #             ming.append(j)
# #             return lianjie,ming
# #     def save(self,shuju,mingzi):
# #         for a,i in enumerate(shuju):
# #             res=requests.get(i)
# #             qq=res.content
# #             z=mingzi[a]
# #             with open('{}.jpg'.format(z),'ab')as f:
# #                 f.write(qq)
# # tu=douban()
# # for  ll in range(0,125,25):
# #     ab=tu.fasongqingqiu(ll)
# #     tu.guolv(ab)
# #     shu,m=tu.guolv(ab)
# #     tu.save(shu,m)
#  tu=tupian()
# for  ll in range(0,125,25):
#     ab=tu.fasongqingqiu(ll)
#     tu.guolv(ab)
#     shu,m=tu.guolv(ab)
#     tu.save(shu,m)


# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie=[]
#         ming=[]
#         patt=re.compile(r'<img width="100" (.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(len(items))
#         for i in items:
#             new=re.compile(r'src="(.*?)"')
#             aaa=new.findall(i)
#             lianjie.append(aaa[0])
#         kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         name=kk.findall(abc)
#         for j in name:
#             ming.append(j)
#             c=dict(zip(ming,lianjie))
#         return c
#     def save(self,shuju):
#         #需要请求图片的链接
#         for a,i in shuju.items():
#             res=requests.get(i)
#             #注：接收响应的结果只能用content，因为图片是二进制
#             qq = res.content
#             # z=mingzi[a]
#             with open('{}.jpg'.format(a),'ab') as f:
#                 f.write(qq)
#
# tu=tupian()
# for  ll in range(0,125,25):
#     ab=tu.fasongqingqiu(ll)
#     # abc=tu.guolv(ab)
#     shuju=tu.guolv(ab)
#     # print(shu,m)
#     tu.save(shuju)
# # import requests
# # import re
import requests

url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","countryGuid":"2fdd90a6-25f2-11e9-a4d7-0242ac120003"}

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
    'Postman-Token': "af4d5098-1851-4939-ae60-ce21d60f9223,571c25ad-2e0f-4a0b-a2c4-8ad0afd44c6d",
    'Host': "120.132.8.33:9000",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

res=response.json()
print(res)


