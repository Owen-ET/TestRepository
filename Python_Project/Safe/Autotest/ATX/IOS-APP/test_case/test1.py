#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:54
# @Author  : zc
# @File    : test1.py


# import wda
import time
# u = wda.Client("http://localhost:8100")
# print(u.status())
# u.session("com.apple.Preferences")
# time.sleep(3)


import wda

c = wda.Client('http://localhost:8100')

s = c.session('com.chen.CityMineSafetyOne')

s(name='home btn newtask',className='Button').tap()
# 任务类型
# s(label=u"home arrow news",index=1).tap()
size = s.window_size()
# # s.tap(size[0]*0.252,size[1]*0.54,2.0)
# s.swipe(size[0]*0.5, size[1]*0.8, size[0]*0.5, size[1]*0.72, 0.5)
# s(name='确定',className='Button').tap()
# 检查单位
# s(name=u"home arrow news",index=2).tap()
# s(name=u"下一级",index=1).tap()
# s(name='区域1',className='StaticText').tap()
# 隐患类型：交通
# s(name=u"home arrow news",index=3).tap()
# s.swipe(size[0]*0.5, size[1]*0.8, size[0]*0.5, size[1]*0.72, 0.5)
# s(name='确定',className='Button').tap()
# 隐患描述
# s(type="TextView").set_text("交通违法！")
# s(name='收起键盘',className='Button').tap()
# 照片
# s(name='addtask btn add pic',className='Button').tap()
# for i in range(4):
#     s.swipe(size[0]*0.55, size[1]*0.6, size[0]*0, size[1]*0.6)
# s(label=u"btn unselected", name=u"btn unselected", type="Button", index=1).tap()
# s(name='确定(1)',className='Button').tap()
# 违反制度管理
# s(name='违反制度管理').tap()
# wfzdList = ['违反消防相关制度', '违反员工行为规范']
# for i in wfzdList:
#     s(name=i).tap()
# s(label=u"login btn back").tap()
# 向上拖动
s.swipe(size[0]*0.5,size[1]*0.85,size[0]*0.5,size[1]*0.12)
# 整改期限
# s(name=u"home arrow news", index=4).tap()
# s.swipe(size[0]*0.75, size[1]*0.82, size[0]*0.75, size[1]*0.766)
btn = s(label=u"提交").text
print(btn)


