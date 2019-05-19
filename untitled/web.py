#!/usr/bin/python
# -*- coding:utf-8 -*-
#下载模块 selenium
from selenium import webdriver
from time import sleep
#定义打开的浏览器
dr = webdriver.Firefox()
# dr.get('https://www.baidu.com')
# sleep(2)

#层级定位：先定位一个顶层元素，再定位这个元素下面的元素,多用于复杂的定位场景
# dr.get('https://www.ctrip.com/')
# aa=dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
# for i in aa:
#     i.click()
#     sleep(2)
#
# aa = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in aa:
#     i.click()
#     sleep(2)







#请求网页
#扣扣空间
# 点击退出的时候
# dr.get('https://www.baidu.com')
# dr.get('https://qzone.qq.com/')

#弹出框获取
# dr.get('file:///C:/Users/wang/Desktop/abc.html')
# dr.find_element_by_xpath('/html/body/input').click()
#将控制器切换到到弹出框
# ww=dr.switch_to_alert()
# sleep(2)
#获取弹出框上的文本
# print(ww.text)
#点击确定
# ww.accept()
#点击取消
# ww.dismiss()
# ww.send_keys('zhaung')
# sleep(1)
# ww.accept()
# sleep(2)
#切换到框架  id，name
# dr.switch_to.frame('login_frame')

#退出框架,退出到最初的页面
# dr.switch_to_default_content()
#切换到上一级的框架
# dr.switch_to.parent_frame()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a').click()

# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys(1737123574)
# dr.find_element_by_id('p').send_keys('19972002.zgw')
# sleep(2)
# dr.find_element_by_id('img_out_1737123574').click()



# iframe 网页框架
# sleep(5)
# dr.find_element_by_id('tb_logout').click()

# dr.find_element_by_class_name('ui-icon icon-logout').click()

# aa = dr.switch_to.alert()
# print(aa.text)



#定位到退出按钮


#扣扣邮箱
dr.get('https://mail.qq.com/cgi-bin/loginpage')
sleep(1)
dr.switch_to.frame('login_frame')
sleep(2)
# dr.find_element_by_class_name('switch_btn').click()
# sleep(1)
# dr.find_element_by_id('uin_del').click()
# sleep(1)
# dr.find_element_by_id('u').send_keys(1737123574)
# dr.find_element_by_id('p').send_keys('19972002.zgw')
# dr.find_element_by_id('login_button').click()
dr.find_element_by_id('img_out_1737123574').click()
sleep(2)
# dr.switch_to.frame('actionFrame')
dr.switch_to.default_content()
sleep(2)
dr.find_element_by_xpath('//*[@id="composebtn"]').click()




# sleep(2)
# dr.find_element_by_xpath('//*[@id="composebtn"]').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/form[2]/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/a').click()
# dr.find_element_by_id('subject').send_keys(123)
# sleep(1)
# dr.find_element_by_css_selector('body').send_keys(456)






# dr.get('https://jd.com')

#通过id定位

# dr.find_element_by_id('kw').send_keys('python')
# dr.find_element_by_id('su').click()
#为了区分跟python中的class 所有叫classname
#单个定位的时候保证class值是唯一的,不唯一可以取下标号
# dr.find_elements_by_class_name('mnav')[1].click()
# sleep(2)
#通过name定位
# dr.find_element_by_name('wd').send_keys('python')
#通过link_text定位,保证文本的唯一性
# dr.find_element_by_link_text('新闻').click()
# partial link text 模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()
# tag_name 定位 通过标签页的名称定位
# dr.find_element_by_tag_name()
# xpath(路径标记语言) 路径定位
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('数学')
# css 层叠样式表定位
# dr.find_element_by_css_selector('#kw').send_keys('python')

#动作： send_keys()输入  click()点击
# #回到上一次打开的网页
# dr.back()
# sleep(2)
# #前进
# dr.forward()
# #获取网页标题,一般用来作断言，判断请求到的网页的标题是否符合预期结果
# print(dr.title)
# # 获取请求的网址
# print(dr.current_url)
# #设置浏览器窗口大小
# dr.set_window_size(400,400)
# #设置浏览器的窗口位置
# dr.set_window_position(400,400)
# #最大化浏览器
# dr.maximize_window()
# #最小化浏览器
# dr.minimize_window()


#关闭浏览器
# dr.quit()



#豆瓣
# dr.get('https://www.douban.com/')# 1号窗口
# sleep(1)


#获取第一个窗口标识(句柄)
# print(dr.current_window_handle)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click() #二号窗口
# sleep(2)
#浏览器本身无法决定什么时候打开哪一个窗口,按照窗口打开顺序标号(唯一)
#切换窗口
# dr.switch_to_window()
#获取所有窗口的标识
# ww = dr.window_handles
#切换窗口
# dr.switch_to_window(ww[-1])
# print(dr.title)



#京东
# dr.get('https://www.jd.com')
# sleep(2)
# dr.find_element_by_class_name('link-login').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# sleep(2)
# dr.find_element_by_id('loginname').send_keys(18272981597)
# dr.find_element_by_id('nloginpwd').send_keys('199783.zgw')
# dr.find_element_by_id('loginsubmit').click()
# sleep(10)
#
# dr.find_element_by_class_name('cate_menu_lk').click()
# sleep(5)
# ww = dr.window_handles
# print(ww)
# sleep(2)
# dr.switch_to_window(ww[-1])
# sleep(2)
# print(dr.title)
# dr.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/button/i').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img').click()
# sleep(8)
# aa = dr.window_handles
# print(aa)
# sleep(2)
# dr.switch_to_window(aa[-1])
# sleep(3)
# dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()





















