#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:26
# @Author  : zc
# @File    : driver.py

from selenium import webdriver

class Browser():

    def browser(self):
        return  webdriver.Chrome()