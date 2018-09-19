#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/17 17:15
# @Author  : zc
# @File    : text.py
a=1

if a == None:
    print(r"abc\' is \n123")
else:
    print(not 3>4 or not 9>1)
    print(14%3)
    print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))
    print("小明的成绩提高了:%.1f%%" %((85-72)/85*100))
    print("=================数组list、tuple====================")

list = ['aa','zc','bb']
list.insert(1,'bb')
print(list)
#删除指定位置的值
list.pop(1)
print(list)
#获取二维数组的值
list.insert(1,['11','22'])
print(list[1][1])

tuple = ('3','2','1',['aa','bb'],'3')
print(tuple.index('3',1,5))
tuple[3][1] = 'cc'
print(tuple)

L= [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])