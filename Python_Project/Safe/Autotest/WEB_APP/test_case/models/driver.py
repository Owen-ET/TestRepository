#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/28 14:48
# @Author  : zc
# @File    : driver.py

from selenium import webdriver

def browser():
    '''
    # 浏览器启动
    :return: Chrome
    '''
    return webdriver.Chrome()
