#!/usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# # class Qiushi(object):
# #     def hanshu(self):
# for i in range(1,5):
#     a='https://www.qiushibaike.com/text/page/{}/'.format(i)
#     oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#
#     }
#     b=requests.get(a,headers=oo)
#     c = b.content.decode('utf-8')
# # 过滤想要的内容
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     f=d.findall(c)
#     dd=re.compile('<h2>(.*?)</h2>',re.S)
#     fff=dd.findall(c)
#     ff=[]
#     ffff=[]
#     for i in f:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
#     for v in fff:
#         v=v.replace('/n','')
#         ffff.append(v)
#     for x in range(len(ff)):
#         ff.insert(x*2,ffff[x])
#     with open('d.txt','w',encoding='utf-8') as g:
#         for i in ff:
#             g.write(i)
import requests
import re
class Tupian(object):
    def 发送请求(self,page):
        url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
        head={
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;66.0) Gecko / 20100101Firefox / 66.0'
        }
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html

    def 过滤(self,abc):
        lianjie=[]
        patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
        items=patt.findall(abc)
        for i in items:
            news_a=re.compile(r'<img src="(.*?)"',re.S)
            aaa=news_a.findall(i)
            lianjie.extend(aaa)
        return lianjie
    def save(self,shu):
        global bc
        #图片是个链接，请求图片的链接，将相应保存
        for a,i in enumerate(shu):
            res=requests.get('https:'+i)
            #接受相应的结果只能用content
            qq=res.content
            with open('{}.jpg'.format(bc),'ab')as f:
                f.write(qq)
            bc+=1

tu=Tupian()
bc=0
for i in range(1,6):
    ab=tu.发送请求(i)
    sh=tu.过滤(ab)
    tu.save(sh)
print(bc)


