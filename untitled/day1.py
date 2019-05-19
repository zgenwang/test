#!/usr/bin/python
# -*- coding:utf-8 -*-
# a="hello 我叫%s,今年%d岁"
# b=input('请输入你的名字')
# d=int(input("请输入年龄"))
# c =a %(b,d)
# print(c)
# a = "sfas sdsads sads"
# b = a.index("d")
# print(b)

# a=["F","QQQ","AAA","aa","xx"]
# a.append([1000])
# b=a.copy()
# a[-1].append([21,13])
# a[-1][1].append(1314)
# print(a)
# print(b)
# a={21,22,31,11,2,1,3,5,20,222,333,44444,11111}
# a.add("qwqw")
# a.remove(21)
# a.pop()
# print(a)
# a={'name':('xiaoming','xiaoxiao'),'age':21}
# a['name']=123
# b={"wah":"123"}
# a.update(b)
# print(a)
# a=input("请输入值")
# a=int(a)
# if a >= 90 and a<=100:
#     print("优秀")
# elif 90<=a>=80:
#     print("良好")
# elif 80>a>=70:
#     print("及格")
# else:
#     print("不及格")
# a=int(input("请输入值："))
# if a%3==0 and a%2==0:
#         print("hello world")
# elif a%3==0:
#     print("world")
# elif a%2==0:
#      print("hello")
# else:
# #     print(123)
# a=input("请输入字符串：")
# if (a[-1])=="c":
#     if (a[0])=="a" and (a[0])=="A":
#         print("110")
#     else:
#         print(130)
# elif (a[0]=="a"):
#     print(120)
# else:
#     print(250)
# sum=0
# for i in  range(1,101 ):
#     sum=sum+i
# print(sum)
# for i in range(1,10):
#     if i==7:
#         continue
#     print(i)
# else:
#     print("hello")
# a=0
# for i in range(100):
#     if i%2 ==0:
#         a=a-i
#     else:
#         a=a+i
# print(a)
# import random
# a= random.randint(1,10)
# print("有3次机会")
# for i in range(1,4):
#     b=int(input(">>>"))
#     if b > a:
#         print("大了,还有{}次机会 ".format(3-i))
#     elif b < a:
#         print("小了,还有{}次机会" .format(3-i))
#     else:
#         print("正确")
#         break
# a=[11,99,88,77,66,55,33,22,44]
# b,c=[],[]
# for i in a:
#     if i > 55:
#         b.append(i)
#     else:
#         c.append(i)
# # print(b,c)
# p=[2]
# for i in range(2,101):
#   for temp in range(2,i):
#     if i%temp==0:
#       break
#       print('i=',i,'temp=',temp)
#     elif temp==i-1:
#       p.append(i)
# print('\n以下打印质数：')
# print(p)
# a=0
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i == j:
#         a=a+i
# print(a)
# for i in range(1,9):
#     for j in range(0,9):
#         for a in range(0,9):
#             if (i**3+j**3+a**3==i*100+j*10+a):
#                 print(i*100+j*10+a)



# for i in range(1,1000):
#     a=0
#     for j in range(1, i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(a)
# 水仙花数
# for i in range(100,1000):
#     a=i//100 %10
#     b=i//10 %10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)
# b=int(input(">>>"))
# while b >20:
#     print("hello")
#     b -=1
# a=0
# b=1
# while b<101:
#     a +=b
#     b +=1
# print(a)
# while True:
# #     c=[]
# #     a=input('请输入数据，以逗号隔开：')
# #     if '-' in a:
# #         break
# #     else:
# #         b=a.split(',')
# #         for i in  b:
# #             c.append(int(i))
# #         d=sum(c)/len(c)
# #         print('平均成绩为{}'.format(d))
# #         for j in  c:
# #             if d > j:
# #                 print('低于平均分的学生成绩为{}'.format(j))
# a=0
# for i in  range(2,100):
#     for j in  range(2,i):
#         if i%j==0:
#             break
#     else:
#         a += i
# print(a)
# a=int(input('>>>'))
# for i in range(a - 20 ):
#     print('hello')
# for i in range(1, 10):
#     for j in  range(1,i+1):
#         print('{}x{}={}\t' .format(i,j, i*j),end= ' ')
#     print()
# a=int(input('请输入一个数字：'))
# b=1
# c=0
# for i in range(1,a+1):
#     b=b*i
#     c+=b
# print(c)
# print(b)
# 选择法
# a=input('>>>以逗号为分割:')
# b=a.split(',')
# for i in  range(0,len(b)):
#     for j in  range(i+1,len(b)):
#         if int(b[i])> int(b[j]):
#             b[i],b[j]=b[j],b[i]
# print(b)
# 冒泡法
# def 函数(b):
#     # a=input('>>>')
#     # b=a.split(',')
#     for i in range(1,len(b)):
#         for j in  range(0,len(b)-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#     print(b)
# 函数([12,11,10])
# a=3
# b=4
# def qqq():
#     global a
#     a=4
#     b=3
#     print(a,b)
# qqq()
# print
# c=[]
# a=input('请输入三条边：')
# b=a.split(',')
# for i in b:
#     c.append(int(i))
#     c.sort()
# if c[2] <c[1]+c[0]:
#     if c[2]**2 > c[0]**2 + c[1]**2:
#         print('钝角')
#     elif c[2]**2 < c[0]**2 + c[1]**2:
#         print('锐角')
#     elif c[2]**2 == c[0]**2 + c[1]**2:
#         print('直角')
# else:
#     print('输入有误')
# a=input('>>>')
# b=len(a)
# c=0
# d=b-1
# while c <=d:
#     if a[c]==a[d]:
#         c+=1
#         d-=1
#     else:
#         break
# if c > d:
#     print('是')
# else:
#     print('不是')
# a=[1,2,3,4,2,3]
# b=[]
# for i in a:
#     for i not in b
# def su(b):
#     a=0
#     for i in  range(1,b+1):
#         a+=i
#     print(a)
#     return a
# su(100)
# b=su(100)
# print(b)
# a,b=divmod(16,16)
# print(a,b)
# str
# import day2
# q=day2.qq()
# q.rr()





# c  = lambda x,y : x * y
# if __name__=='_main_':
#     print('hello')
# print('123')
# for i in range(100,1000):
#     a=i//100%10
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)
import pymysql
with open('a.txt','r',encoding='utf-8') as f:
    a=f.read()
    a = a.split('\n')
conn = pymysql.connect(host="192.168.1.107", port=3306, user='root', password='123456')
qwe = conn.cursor()
qwe.execute('use bosss;')
qwe.execute('create table zyq(招呼 char(10),表白 char(10),哼哼 char(10));')
for i in a:
    i = i.split(',')
    print(i)
    qwe.execute('insert into zyq values("{}","{}","{}");'.format(i[0],i[1],i[2]))



























































