#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
class qingqiu():
        dr = webdriver.Firefox()
        dr.get('https://www.jd.com')
        sleep(2)

        def denglu(self):
            self.dr.find_element_by_class_name('link-login').click()
            sleep(2)
            self.dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
            sleep(2)
            self.dr.find_element_by_id('loginname').send_keys(18272981597)
            self.dr.find_element_by_id('nloginpwd').send_keys('199783.zgw')
            self.dr.find_element_by_id('loginsubmit').click()
            sleep(10)
        def shangpin(self):
            self.dr.find_element_by_class_name('cate_menu_lk').click()
            sleep(5)
            ww = self.dr.window_handles
            print(ww)
            sleep(2)
            self.dr.switch_to_window(ww[-1])
            sleep(2)
            print(self.dr.title)
            self.dr.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/button/i').click()
            sleep(2)
            self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]').click()
            sleep(2)
            self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img').click()
            sleep(8)
        def gouwuche(self):
            aa = self.dr.window_handles
            sleep(2)
            self.dr.switch_to_window(aa[-1])
            sleep(3)
            self.dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()


qq=qingqiu()
qq.denglu()
qq.shangpin()
qq.gouwuche()











