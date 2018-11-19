#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 16:41
# @Author  : zc
# @File    : functions.py

from appium import webdriver
import Safe.Autotest.Appium.IOS.desired_capabilities as desired_capabilities

class Functions(object):

    def __init__(self):
        desired_cap = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        # 启动app
        self.d = webdriver.Remote(uri, desired_cap)


    def do_swipe(self,x1,y1,x2,y2):
        '''
        # 滑动方法
        :return:
        '''
        self.d.execute_script("mobile: dragFromToForDuration",
                              {"fromX": x1, "fromY": y1, "toX": x2, "toY": y2, "duration": 0.5})


    def isExist(self,i):
        # 判断可不可以点击元素
        try:
            self.d.find_element_by_name(i).click()
            return True
        except:
            return False