#!/usr/bin/python
# -*- coding:utf-8 -*-
from jiekou_kuang.config.qingqiu import bingli
from jiekou_kuang.config.qingqiu import guojia
import unittest
from jiekou_kuang.config.qingqiu import jiekou_qingqiu
from jiekou_kuang.data.duqu import shuju
from jiekou_kuang.config.qingqiu import gerenxinxi
from jiekou_kuang.data.duqu import guidd

class qwe(unittest.TestCase):
    denglu=jiekou_qingqiu().denglu
    shuju=shuju()
    def test_1(self):
        qq=self.denglu(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(qq['code'],0)
    def test_2(self):
        for i in range(1,len(self.shuju)):
            ww=self.denglu(int(self.shuju[i][0]),int(self.shuju[i][1]))
            self.assertNotEqual(ww['code'],0)
# if __name__=='__main__':
    # unittest.main()
class geren(unittest.TestCase):
    chaxun=gerenxinxi().chaxun
    guid=guidd()
    def test_c(self):
        e=self.chaxun(self.guid[0][0],self.guid[0][1])
        self.assertEqual(e['code'],0)
    def test_x(self):
        for i in range(1,len(self.guid)):
            ee=self.chaxun(self.guid[i][0],self.guid[i][1])
            self.assertEqual(ee['code'],0)
# if __name__=='__main__':
    # unittest.main()
class guojiaa(unittest.TestCase):
    diqu=guojia().diqu
    def test_guo(self):
        aa=self.diqu()

        self.assertEqual(aa['data']['A'][0]['guid'],"2fdd7d26-25f2-11e9-a4d7-0242ac120003")

    def test_jia(self):
         bb=self.diqu()
         self.assertNotEqual(bb['code'],1)

# if __name__=='__main__':
    # unittest.main()
class binglii(unittest.TestCase):
    bl=bingli().bl
    def test_bing(self):
        aa=self.bl()
        self.assertEqual(aa["data"]["diseaseHistory"][0]["name"],"冠心病",)
    def test_li(self):
        bb=self.bl()
        self.assertNotEqual(bb["code"],1)
if __name__=="__main__":
    unittest.main()




